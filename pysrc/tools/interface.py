"""
Modèle dynamique du système autonome des bactéries
"""


import numpy as np
from matplotlib.widgets import Slider, Button
import matplotlib.pyplot as plt
from scipy.integrate import odeint


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

        ax_S0 = plt.axes([0.1, 0.40, 0.8, 0.03], facecolor=axcolor)
        ax_X0 = plt.axes([0.1, 0.35, 0.8, 0.03], facecolor=axcolor)
        ax_mu = plt.axes([0.1, 0.30, 0.8, 0.03], facecolor=axcolor)
        ax_L = plt.axes([0.1, 0.25, 0.8, 0.03], facecolor=axcolor)
        ax_k = plt.axes([0.1, 0.20, 0.8, 0.03], facecolor=axcolor)
        ax_m = plt.axes([0.1, 0.15, 0.8, 0.03], facecolor=axcolor)
        ax_delta = plt.axes([0.1, 0.10, 0.8, 0.03], facecolor=axcolor)

        # Sliders
        cnd0 = cndzr.cords
        s_S0 = Slider(ax_S0, 'S0', 0, 2, valinit=cnd0[0])
        s_X0 = Slider(ax_X0, 'X0', 0, 2, valinit=cnd0[1])
        s_mu = Slider(ax_mu, 'Mu', -2, 2, valinit=self.modl.mu)
        s_L = Slider(ax_L, 'L', -2, 2, valinit=self.modl.L)
        s_k = Slider(ax_k, 'k', -2, 2, valinit=self.modl.k)
        s_m = Slider(ax_m, 'm', -2, 2, valinit=self.modl.m)
        s_delta = Slider(ax_delta, 'delta', 0, 2, valinit=self.modl.delta)

        # Calcul des trajectoires
        tdisc = np.linspace(taxis.start, taxis.end, taxis.size_subdiv)
        trj = odeint(self.modl.get_rhs(), cnd0, tdisc)
        p0, = ax.plot(tdisc, trj[:, 0], cndzr.get_style(),
                      label=self.modl.label1)
        p1, = ax.plot(tdisc, trj[:, 1], stylebis.get_lineStyle(),
                      label=self.modl.label2)

        # Paramétrage axe principal
        ax.set_xlim(xaxis.start, xaxis.end)
        ax.set_ylim(yaxis.start, yaxis.end)
        ax.grid(True)
        ax.legend()
        ax.set_title(self.modl.title)
        ax.set(xlabel=xaxis.label, ylabel=yaxis.label)

        # Fonction pour actualiser le plot
        def update(val):
            cnd0 = (s_S0.val, s_X0.val)
            self.modl.mu = s_mu.val
            self.modl.L = s_L.val
            self.modl.k = s_k.val
            self.modl.m = s_m.val
            self.modl.delta = s_delta.val
            trj = odeint(self.modl.get_rhs(), cnd0, tdisc)
            p0.set_ydata(trj[:, 0])
            p1.set_ydata(trj[:, 1])
            fig.canvas.draw_idle()

        # Activation des sliders
        s_S0.on_changed(update)
        s_X0.on_changed(update)
        s_mu.on_changed(update)
        s_L.on_changed(update)
        s_k.on_changed(update)
        s_m.on_changed(update)
        s_delta.on_changed(update)

        # Reset button
        resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
        button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

        def reset(event):
            s_S0.reset()
            s_X0.reset()
            s_mu.reset()
            s_L.reset()
            s_k.reset()
            s_m.reset()
            s_delta.reset()

        button.on_clicked(reset)

        plt.show()
