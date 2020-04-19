"""
Modèle dynamique d'un système autonome
"""
import numpy as np
from matplotlib.widgets import Slider, Button
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from tools.phase_diag import PhaseDiag
from tools.cnds_initiales import Initials


class DynamicModel:
    """Evolution dynamique d’un système autonome"""
    def __init__(self, modl, figsize=(10, 6)):
        self._modl = modl
        self._figsize = figsize

    @property
    def modl(self):
        return self._modl

    @modl.setter
    def modl(self, value):
        self._modl = value

    @property
    def figsize(self):
        return self._figsize

    @figsize.setter
    def figsize(self, value):
        self._figsize = value

    def __str__(self):
        return self.title

    def plot(self, cndzr, stylebis, xaxis, yaxis, taxis,
             axcolor='lightgoldenrodyellow'):
        """
        Affiche le modèle avec des sliders pour faire varier les paramètres
        """
        # Préparation figure et axes
        fig, ax = plt.subplots(figsize=self.figsize)
        plt.subplots_adjust(bottom=0.50, top=0.90)

        axis_params = [
            plt.axes([0.1, 0.40 - 0.05*i, 0.8, 0.03],
                     facecolor=axcolor) for i in range(
                     len(self.modl.params) + len(self.modl.symb))]

        # Sliders
        cnd0 = cndzr.cords
        sliders = {}
        # Conditions initiales
        order = len(self.modl.symb)
        for s, axis in zip(self.modl.symb, axis_params[:order]):
            sliders[s + '0'] = Slider(
                axis, s + '0', 0, 2, valinit=cnd0[self.modl.symb.index(s)])
        # Paramètres
        for p, axis in zip(self.modl.params, axis_params[order:]):
            sliders[p] = Slider(axis, p, 0, 2, valinit=self.modl.params[p])

        # Calcul des trajectoires
        tdisc = np.linspace(taxis.start, taxis.end, taxis.size_subdiv)
        trj = odeint(self.modl.get_rhs(), cnd0, tdisc)
        p0, = ax.plot(tdisc, trj[:, 0], cndzr.get_style(),
                      label=self.modl.labels[0])
        p1, = ax.plot(tdisc, trj[:, 1], stylebis.get_lineStyle(),
                      label=self.modl.labels[1])

        # Paramétrage axe principal
        ax.set_xlim(xaxis.start, xaxis.end)
        ax.set_ylim(yaxis.start, yaxis.end)
        ax.grid(True)
        ax.legend()
        ax.set_title(self.modl.title)
        ax.set(xlabel=xaxis.label, ylabel=yaxis.label)

        # Fonction pour actualiser le plot
        def update(val):
            cndzr.cords = tuple([sliders[s + '0'].val for s in self.modl.symb])
            for p in self.modl.params:
                self.modl.params[p] = sliders[p].val
            try:
                trj = odeint(self.modl.get_rhs(), cndzr.cords, tdisc)
                p0.set_ydata(trj[:, 0])
                p1.set_ydata(trj[:, 1])
                fig.canvas.draw_idle()
            except Exception:
                pass

        # Activation des sliders
        for s in sliders.values():
            s.on_changed(update)

        # Reset button
        resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
        resetbutton = Button(resetax, 'Reset', color=axcolor,
                             hovercolor='0.975')

        def reset(event):
            for s in sliders.values():
                s.reset()

        resetbutton.on_clicked(reset)

        # Phase diag button
        phasediagax = plt.axes([0.1, 0.025, 0.2, 0.04])
        phasediagbutton = Button(phasediagax, 'Diagramme de phases',
                                 color=axcolor, hovercolor='0.975')

        def phasediag(event):
            cnds = Initials()
            cnds.append(cndzr.cords, cndzr.param)
            diag = PhaseDiag(figsize=self.figsize)
            diag.portrait(self.modl, cnds, xaxis, yaxis, taxis,
                          exprtpng=False, showfield=True)

        phasediagbutton.on_clicked(phasediag)

        plt.show()
