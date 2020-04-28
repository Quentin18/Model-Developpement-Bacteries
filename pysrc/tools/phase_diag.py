"""
Portrait des phases d'un système autonome
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from tools.field import Field


class PhaseDiag:
    """Gestion du portrait des phases d’un système autonome"""
    def __init__(self, title="Portrait des phases", figsize=(10, 6)):
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

    def portrait(self, modl, cndszr,
                 xaxis, yaxis, taxis,
                 exprtpng=False, showfield=True):
        # Préparation graphique
        fig, phases = plt.subplots(figsize=self.figsize)

        # Paramétrages graphiques globaux
        plt.xlim(xaxis.start, xaxis.end)
        plt.ylim(yaxis.start, yaxis.end)

        # Paramétrages repère
        phases.grid(True)
        phases.set_title(self.title)
        phases.set(xlabel=modl.labels[0], ylabel=modl.labels[1])

        # Calcul des trajectoires
        tdisc = np.linspace(taxis.start, taxis.end, taxis.size_subdiv)
        cndszero = cndszr.cnds
        for cnd in cndszero:
            cnd0 = cnd.cords
            trj = odeint(modl.get_rhs(), cnd0, tdisc)
            phases.plot(trj[:, 0], trj[:, 1], cnd.get_style(),
                        label=modl.str_cndzr() + str(cnd))

        # Champ des gradients
        if showfield:
            field = Field()
            field.plot(modl, xaxis, yaxis)

        plt.legend()
        plt.tight_layout()
        plt.show()

        if exprtpng:
            figname = self.title.lower() + ".png"
            figname = figname.replace(" ", "_")
            fig.savefig("img/" + figname)
