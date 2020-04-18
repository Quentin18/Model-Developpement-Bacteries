"""
Evolution d'un système autonome
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


class Analyse:
    """Gestion de l'évolution d’un système autonome"""

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

    def plot(self, modl, cndszr, taxis, ls, leg):
        """
        Représente la variation de temps de croisement entre X et S en fonction de S0
        """
        # Préparation figure et axes

        # Calcul des trajectoires
        tdisc = np.linspace(taxis.start, taxis.end, taxis.size_subdiv)
        cndszero = cndszr.cnds
        tlist = []
        for cnd in cndszero:
            cnd0 = cnd.cords
            trj = odeint(modl.get_rhs(), cnd0, tdisc)
            i = 0
            for cp in trj:
                cp[0] = round(cp[0], 2)
                cp[1] = round(cp[1], 2)
                if cp[0] == cp[1]:
                    tlist.append(tdisc[i])
                    break
                i += 1

        fig, ax = plt.subplots()
        ax.plot(ls, tlist)
        plt.xlabel(leg, fontsize=12)
        plt.ylabel('Temps', fontsize=12)
        plt.tick_params(labelsize=12)
        ax.set_title(f"Temps de croisement entre S et X en fonction de {leg}")
        plt.show()
