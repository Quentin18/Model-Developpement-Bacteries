"""
Modèle de développement des bactéries dans un substrat
"""
import functools


class Bacteries:
    def __init__(self, mu, L, k, m, delta,
                 title="Développement des bactéries dans un substrat",
                 label1="Concentration de nourriture",
                 label2="Concentration de bactéries"):
        self._mu = mu        # Taux de croissance des bactéries
        self._L = L          # Facteur inhibiteur croissance bactéries
        self._k = k          # Taux d'affinité des bactéries
        self._m = m          # Taux de mortalité des bactéries
        self._delta = delta  # Coefficient de recyclage des cellules
        self._title = title
        self._label1 = label1
        self._label2 = label2

    @property
    def mu(self):
        return self._mu

    @mu.setter
    def mu(self, value):
        self._mu = value

    @property
    def L(self):
        return self._L

    @L.setter
    def L(self, value):
        self._L = value

    @property
    def k(self):
        return self._k

    @k.setter
    def k(self, value):
        self._k = value

    @property
    def m(self):
        return self._m

    @m.setter
    def m(self, value):
        self._m = value

    @property
    def delta(self):
        return self._delta

    @delta.setter
    def delta(self, value):
        self._delta = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def label1(self):
        return self._label1

    @label1.setter
    def label1(self, value):
        self._label1 = value

    @property
    def label2(self):
        return self._label2

    @label2.setter
    def label2(self, value):
        self._label2 = value

    def __str__(self):
        return f"""{self.title}
        mu={self.mu}, L={self.L}, k={self.k}, m={self.m}, delta={self.delta}"""

    def get_params(self):
        return [self.mu, self.L, self.k, self.m, self.delta]

    def _rhs(self, z, t):
        S, X = z[0], z[1]
        mu, L, k, m, delta = self.get_params()
        dSdt = -(mu*S*X / (k + S + (S**2/L))) + delta*m*X
        dXdt = (mu*S*X / (k + S + (S**2/L))) - m*X
        return [dSdt, dXdt]

    def get_rhs(self):
        return functools.partial(self._rhs)

    def get_field(self, S, X):
        mu, L, k, m, delta = self.get_params()
        f = -(mu*S*X / (k + S + (S**2/L))) + delta*m*X
        g = (mu*S*X / (k + S + (S**2/L))) - m*X
        return [f, g]
