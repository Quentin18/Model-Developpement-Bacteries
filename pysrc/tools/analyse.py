"""
Analyse du système autonome des bactéries
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mdl.model_bacteries import Bacteries


class Analyse:
    """Gestion de l'évolution du système autonome des bactéries"""
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

    def plotSX(self, modl, cndszr, taxis, ls, leg):
        """
        Représente la variation de temps de croisement entre X et S
        en fonction de S0
        """

        # Calcul des trajectoires
        tdisc = np.linspace(taxis.start, taxis.end, taxis.size_subdiv)
        cndszero = cndszr.cnds
        tlist = []
        # Cherche les points d'intersections S et X
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

    def plotMu(self, L, k, m, delta, cndszr, taxis, epsilon):
        """
        Représente les temps caractéristiques de S0/X0 en fonction de mu
        """
        MU = np.arange(0, 1, 0.001).tolist()
        tdisc = np.linspace(taxis.start, taxis.end, taxis.size_subdiv)
        cndszero = cndszr.cnds
        fig, ax = plt.subplots()
        for cnd in cndszero:
            tlistS = []
            tlistX = []
            cnd0 = cnd.cords
            for mu in MU:
                modl = Bacteries(mu, L, k, m, delta)
                trj = odeint(modl.get_rhs(), cnd0, tdisc)
                i = 1
                ptBreak = 0
                for cp in trj[:-1]:
                    if abs(trj[i][0] - cp[0]) <= epsilon:
                        tlistS.append(tdisc[i])
                        ptBreak += 1
                    if abs(trj[i][1] - cp[1]) <= epsilon:
                        tlistX.append(tdisc[i])
                        ptBreak += 1
                    if ptBreak == 2:
                        break
                    i += 1
            ax.plot(MU, tlistS,
                    label=f"Temps caractéristique de S avec {str(cnd0)}")
            ax.plot(MU, tlistX,
                    label=f"Temps caractéristique de X avec {str(cnd0)}")

        plt.xlabel('mu', fontsize=12)
        plt.ylabel('Temps', fontsize=12)
        ax.legend(loc='upper left', shadow=True)
        plt.tick_params(labelsize=10)
        ax.set_title("Temps de caractéristique de S et X en fonction de mu")
        plt.show()

    def plotL(self, mu, k, m, delta, cndszr, taxis, epsilon):
        """
        Représente les temps caractéristiques de S0/X0 en fonction de L
        """
        L = np.arange(-1, 2, 0.001).tolist()
        tdisc = np.linspace(taxis.start, taxis.end, taxis.size_subdiv)
        cndszero = cndszr.cnds
        fig, ax = plt.subplots()
        for cnd in cndszero:
            tlistS = []
            tlistX = []
            cnd0 = cnd.cords
            for l in L:
                modl = Bacteries(mu, l, k, m, delta)
                trj = odeint(modl.get_rhs(), cnd0, tdisc)
                i = 1
                ptBreak = 0
                for cp in trj[:-1]:
                    if abs(trj[i][0] - cp[0]) <= epsilon:
                        tlistS.append(tdisc[i])
                        ptBreak += 1
                    if abs(trj[i][1] - cp[1]) <= epsilon:
                        tlistX.append(tdisc[i])
                        ptBreak += 1
                    if ptBreak == 2:
                        break
                    i += 1
            ax.plot(L, tlistS, label=f"Tps carac de S avec {str(cnd0)}")
            ax.plot(L, tlistX, label=f"Tps carac de X avec {str(cnd0)}")

        plt.xlabel('L', fontsize=12)
        plt.ylabel('Temps', fontsize=12)
        ax.legend(loc='lower right', shadow=True)
        plt.tick_params(labelsize=8)
        ax.set_title("Temps de caractéristique de S et X en fonction de L")
        plt.show()

    def plotM(self, mu, L,  k, delta, cndszr, taxis, epsilon):
        """
        Représente les temps caractéristiques de S0/X0 en fonction de M
        """
        M = np.arange(-1, 2, 0.01).tolist()
        tdisc = np.linspace(taxis.start, taxis.end, taxis.size_subdiv)
        cndszero = cndszr.cnds
        fig, ax = plt.subplots()
        for cnd in cndszero:
            tlistS = []
            tlistX = []
            cnd0 = cnd.cords
            for m in M:
                modl = Bacteries(mu, L, k, m, delta)
                trj = odeint(modl.get_rhs(), cnd0, tdisc)
                i = 1
                ptBreak = 0
                for cp in trj[:-1]:
                    if abs(trj[i][0] - cp[0]) <= epsilon:
                        tlistS.append(tdisc[i])
                        ptBreak += 1
                    if abs(trj[i][1] - cp[1]) <= epsilon:
                        tlistX.append(tdisc[i])
                        ptBreak += 1
                    if ptBreak == 2:
                        break
                    i += 1
            ax.plot(M, tlistS, label=f"Tps carac de S avec {str(cnd0)}")
            ax.plot(M, tlistX, label=f"Tps carac de X avec {str(cnd0)}")

        plt.xlabel('m', fontsize=12)
        plt.ylabel('Temps', fontsize=12)
        ax.legend(loc='lower right', shadow=True)
        plt.tick_params(labelsize=8)
        ax.set_title("Temps de caractéristique de S et X en fonction de m")
        plt.show()

    def plotDelta(self, mu, L, k, m, cndszr, taxis, epsilon):
        """
        Représente les temps caractéristiques de S0/X0 en fonction de Delta
        """
        Delta = np.arange(-2, 2, 0.01).tolist()
        tdisc = np.linspace(taxis.start, taxis.end, taxis.size_subdiv)
        cndszero = cndszr.cnds
        fig, ax = plt.subplots()
        for cnd in cndszero:
            tlist = []
            cnd0 = cnd.cords
            # som = 0
            for delta in Delta:
                modl = Bacteries(mu, L, k, m, delta)
                trj = odeint(modl.get_rhs(), cnd0, tdisc)
                cp = trj[-1]
                tlist.append(abs(cp[1]-cp[0]))
                #for cp in trj:
                 #   som += abs(cp[1]-cp[0])
                #tlist.append(som/len(trj))
            ax.plot(Delta, tlist,
                    label=f"Différence entre S et X avec {str(cnd0)}")

        plt.xlabel('delta', fontsize=12)
        plt.ylabel('|S-X|', fontsize=12)
        ax.legend(loc='upper left', shadow=True)
        plt.tick_params(labelsize=8)
        ax.set_title("Différence entre S et X en fonction de delta")
        plt.show()
