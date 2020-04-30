"""
Evolution d'un système autonome
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


class Evolution:
    """Gestion de l'évolution d’un système autonome"""
    def __init__(self, title="Evolution du modèle en fonction du temps",
                 figsize=(10, 6)):
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

    def plot(self, modl, cndszr, xaxis, yaxis, taxis,
             name="evol_model", exprtpng=False):
        """
        Représente les composantes du système différentiel
        en fonction du temps
        """
        # Préparation figure et axes
        fig = plt.figure(1, figsize=self.figsize)
        nbAxes = len(yaxis)
        axes = [fig.add_subplot(nbAxes, 1, i + 1) for i in range(nbAxes)]
        superpose = nbAxes == 1     # Superposition si un seul axe y donné

        # Calcul des trajectoires
        tdisc = np.linspace(taxis.start, taxis.end, taxis.size_subdiv)
        cndszero = cndszr.cnds
        for cnd in cndszero:
            cnd0 = cnd.cords
            trj = odeint(modl.get_rhs(), cnd0, tdisc)
            if superpose:   # Cas superposition
                for i in range(trj.shape[1]):
                    axes[0].plot(tdisc, trj[:, i], cnd.get_style(),
                                 label=modl.str_cndzr() + str(cnd0))
            else:           # Cas graphiques séparés
                i = 0
                for ax in axes:
                    ax.plot(tdisc, trj[:, i], cnd.get_style(),
                            label=modl.str_cndzr() + str(cnd0))
                    i += 1

        # Paramétrages axes
        i = 0
        for ax in axes:
            ax.set_xlim(xaxis.start, xaxis.end)
            ax.set_ylim(yaxis[i].start, yaxis[i].end)
            ax.grid(True)
            ax.legend()
            if superpose:
                ax.set_title(self.title)
                ax.set(xlabel="Temps", ylabel=", ".join(modl.symb))
            else:
                ax.set_title(f"{modl.labels[i]} en fonction du temps")
                ax.set(xlabel="Temps", ylabel=modl.symb[i])
            i += 1

        plt.tight_layout()
        plt.show()

        if exprtpng:
            figname = name + ".png"
            figname.replace(' ', '_')
            fig.savefig("img/" + figname)
