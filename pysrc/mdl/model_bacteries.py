"""
Modèle de développement des bactéries dans un substrat
"""
import functools


class Bacteries:
    """Gestion du modèle de développement des bactéries"""
    def __init__(self, mu, L, k, m, delta,
                 title="Développement des bactéries dans un substrat",
                 labels=["Concentration de nourriture S",
                         "Concentration de bactéries X"],
                 symb=["S", "X"]):
        self._params = None
        self.make_params(mu, L, k, m, delta)     # dictionnaire
        self._title = title
        self._labels = labels
        self._symb = symb

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def labels(self):
        return self._labels

    @labels.setter
    def labels(self, value):
        self._labels = value

    @property
    def symb(self):
        return self._symb

    @symb.setter
    def symb(self, value):
        self.symb = value

    def make_params(self, mu, L, k, m, delta):
        self.params = {lab: p for lab, p in zip(["mu", "L", "k", "m", "delta"],
                                                [mu, L, k, m, delta])}

    def get_params(self):
        try:
            return [self.params[p] for p in ["mu", "L", "k", "m", "delta"]]
        except Exception:
            print("Erreur : manque un paramètre")
            return None

    def _rhs(self, z, t):
        S, X = z[0], z[1]
        mu, L, k, m, delta = self.get_params()
        dSdt = -(mu*S*X / (k + S + (S**2/L))) + (1 - delta)*m*X
        dXdt = (mu*S*X / (k + S + (S**2/L))) - m*X
        return [dSdt, dXdt]

    def get_rhs(self):
        return functools.partial(self._rhs)

    def get_field(self, S, X):
        mu, L, k, m, delta = self.get_params()
        f = -(mu*S*X / (k + S + (S**2/L))) + (1 - delta)*m*X
        g = (mu*S*X / (k + S + (S**2/L))) - m*X
        return [f, g]

    def str_cndzr(self):
        return f"({self.symb[0]}0, {self.symb[1]}0) = "

    def __str__(self):
        return "Modèle de développement des bactéries"
