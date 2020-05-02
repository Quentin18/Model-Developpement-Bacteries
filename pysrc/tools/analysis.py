"""
Analyse d'un système autonome
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


class Analysis:
    """Analyse d'un système autonome"""
    def __init__(self, title="Analyse", figsize=(10, 6)):
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

    def plot_evol_param(self, modl, param, values, cndszr, xaxis, yaxis,
                        taxis, exprtpng=False):
        """
        Montre l'influence d'un paramètre pour le modèle
        """
        # Préparation figure et axes
        fig = plt.figure(1, figsize=self.figsize)
        cndszero = cndszr.cnds
        num_values = len(values)
        num_cndzr = len(cndszero)
        axes = [fig.add_subplot(num_cndzr, num_values, i + 1)
                for i in range(num_values * num_cndzr)]

        # Calcul des trajectoires
        tdisc = np.linspace(taxis.start, taxis.end, taxis.size_subdiv)
        val_init_param = modl.params[param]
        num_ax = 0
        for cnd in cndszero:
            cnd0 = cnd.cords
            for v in values:
                modl.params[param] = v
                trj = odeint(modl.get_rhs(), cnd0, tdisc)
                ax = axes[num_ax]
                for i in range(trj.shape[1]):
                    ax.plot(tdisc, trj[:, i], cnd.get_style())
                ax.set_xlim(xaxis.start, xaxis.end)
                ax.set_ylim(yaxis.start, yaxis.end)
                ax.grid(True)
                ax.set_title(f"{modl.str_cndzr()}{str(cnd)}, {param} = {v}")
                num_ax += 1

        modl.params[param] = val_init_param

        plt.tight_layout()
        plt.show()

        if exprtpng:
            figname = f"evol_param_{param}.png"
            fig.savefig("img/" + figname)