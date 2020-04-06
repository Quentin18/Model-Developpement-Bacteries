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

    def plot(self, modl, cndszr, xaxis, yaxis, taxis, exprtpng=False):
        """
        Représente les composantes du système différentiel
        en fonction du temps
        """
        # Préparation figure et axes
        fig = plt.figure(1, figsize=self.figsize)
        ax1 = fig.add_subplot(211)
        ax2 = fig.add_subplot(212)
        axes = {ax1: yaxis[0], ax2: yaxis[1]}

        # Calcul des trajectoires
        tdisc = np.linspace(taxis.start, taxis.end, taxis.size_subdiv)
        cndszero = cndszr.cnds
        for cnd in cndszero:
            cnd0 = cnd.cords
            trj = odeint(modl.get_rhs(), cnd0, tdisc)
            ax1.plot(tdisc, trj[:, 0], cnd.get_style(), label=str(cnd0))
            ax2.plot(tdisc, trj[:, 1], cnd.get_style(), label=str(cnd0))

        # Paramétrages axes
        for ax in axes:
            ax.set_xlim(xaxis.start, xaxis.end)
            ax.set_ylim(axes[ax].start, axes[ax].end)
            ax.grid(True)
            ax.legend()
            ax.set_title(f"{axes[ax].label} en fonction du temps")
            ax.set(xlabel="Temps", ylabel=axes[ax].label)

        plt.tight_layout()
        plt.show()

        if exprtpng:
            figname = modl.title + ".png"
            figname = figname.replace(" ", "_")
            fig.savefig("img/" + figname)
