"""
Evolution d'un système autonome
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


class Evolution:
    """Gestion de l'évolution d’un système autonome"""
    def __init__(self, title="Evolution", figsize=(10, 6)):
        self._title = title
        self._figsize = figsize

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def figsize(self):
        return self._figsize

    @figsize.setter
    def figsize(self, value):
        self._figsize = value

    def __str__(self):
        return self.title

    def plot(self, modl, cndszr,
             xaxis, yaxis, taxis,
             exprtpng=False):
        # Préparation graphique
        fig, evol = plt.subplots(figsize=self.figsize)

        # Paramétrages graphiques globaux
        plt.xlim(xaxis.start, xaxis.end)
        plt.ylim(yaxis.start, yaxis.end)

        # Paramétrages repère
        evol.grid(True)
        evol.set_title(self.title)
        evol.set(xlabel=xaxis.label, ylabel=yaxis.label)

        # Calcul des trajectoires
        tdisc = np.linspace(taxis.start, taxis.end, taxis.size_subdiv)
        cndszero = cndszr.cnds
        for cnd in cndszero:
            cnd0 = cnd.cords
            trj = odeint(modl.get_rhs(), cnd0, tdisc)
            evol.plot(tdisc, trj[:, 0], cnd.get_style(), label=str(cnd0))
            evol.plot(tdisc, trj[:, 1], cnd.get_style(), label=str(cnd0))

        plt.legend()
        plt.show()

        if exprtpng:
            figname = modl.title + ".png"
            figname = figname.replace(" ", "_")
            fig.savefig("img/" + figname)
