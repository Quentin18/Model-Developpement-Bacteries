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

    def plot_cross(self, modl, cndszr, taxis, ls, leg):
        """
        Représente la variation de temps de croisement entre deux composantes
        en fonction des conditions initiales
        """

        # Calcul des trajectoires
        tdisc = np.linspace(taxis.start, taxis.end, taxis.size_subdiv)
        cndszero = cndszr.cnds
        tlist = []
        # Cherche les points d'intersections entre les deux composantes
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
        ax.set_title(
            f"""Temps de croisement entre {modl.symb[0]} et {modl.symb[1]}
            en fonction de {leg}""")
        plt.show()

    def plot_param(self, modl, param, values, cndszr, taxis, epsilon):
        """
        Représente les temps caractéristiques du quotient des deux composantes
        en fonction du paramètre param (type : str)
        """
        val_init_param = modl.params[param]
        label1, label2 = modl.symb
        tdisc = np.linspace(taxis.start, taxis.end, taxis.size_subdiv)
        cndszero = cndszr.cnds
        fig, ax = plt.subplots()
        for cnd in cndszero:
            tlist1 = []
            tlist2 = []
            cnd0 = cnd.cords
            for v in values:
                modl.params[param] = v
                trj = odeint(modl.get_rhs(), cnd0, tdisc)
                i = 1
                ptBreak = 0
                for cp in trj[:-1]:
                    if abs(trj[i][0] - cp[0]) <= epsilon:
                        tlist1.append(tdisc[i])
                        ptBreak += 1
                    if abs(trj[i][1] - cp[1]) <= epsilon:
                        tlist2.append(tdisc[i])
                        ptBreak += 1
                    if ptBreak == 2:
                        break
                    i += 1
            ax.plot(
                values, tlist1,
                label=f"Temps caractéristique de {label1} avec {str(cnd0)}")
            ax.plot(
                values, tlist2,
                label=f"Temps caractéristique de {label2} avec {str(cnd0)}")

        modl.params[param] = val_init_param
        plt.xlabel(param, fontsize=12)
        plt.ylabel('Temps', fontsize=12)
        ax.legend(loc='upper left', shadow=True)
        plt.tick_params(labelsize=10)
        ax.set_title(
            f"""Temps caractéristique de {label1} et {label2}
            en fonction de {param}""")
        plt.show()

    def plot_diff(self, modl, param, values, cndszr, taxis, epsilon):
        """
        Représente la différence des deux composantes en fonction de param
        """
        val_init_param = modl.params[param]
        label1, label2 = modl.symb
        tdisc = np.linspace(taxis.start, taxis.end, taxis.size_subdiv)
        cndszero = cndszr.cnds
        fig, ax = plt.subplots()
        for cnd in cndszero:
            tlist = []
            cnd0 = cnd.cords
            # som = 0
            for v in values:
                modl.params[param] = v
                trj = odeint(modl.get_rhs(), cnd0, tdisc)
                cp = trj[-1]
                tlist.append(abs(cp[1]-cp[0]))
                # for cp in trj:
                #    som += abs(cp[1]-cp[0])
                # tlist.append(som/len(trj))
            ax.plot(
                values, tlist,
                label=f"""Différence entre {label1} et {label2}
                avec {str(cnd0)}""")

        modl.params[param] = val_init_param
        plt.xlabel(param, fontsize=12)
        plt.ylabel(f"|{label1}-{label2}|", fontsize=12)
        ax.legend(loc='upper left', shadow=True)
        plt.tick_params(labelsize=8)
        ax.set_title(f"""Différence entre {label1} et {label2}
        en fonction de delta""")
        plt.show()
