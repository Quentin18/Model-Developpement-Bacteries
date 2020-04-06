"""
Style des lignes
"""


class Color:
    """Gestion de la couleur d'une ligne"""
    def __init__(self):
        self._colors = {"blue": "b",
                        "red": "r",
                        "black": "k",
                        "cyan": "c",
                        "green": "g",
                        "magenta": "m",
                        "yellow": "y"}

    def blue(self):
        return self._colors["blue"]

    def red(self):
        return self._colors["red"]

    def black(self):
        return self._colors["black"]

    def cyan(self):
        return self._colors["cyan"]

    def green(self):
        return self._colors["green"]

    def magenta(self):
        return self._colors["magenta"]

    def yellow(self):
        return self._colors["yellow"]


class Form:
    """Gestion de la forme d'une ligne"""
    def __init__(self):
        self._forms = {"solid": "-",
                       "dashed": "--",
                       "dash-dot": "-.",
                       "dotted": ":"}

    def solid(self):
        return self._forms["solid"]

    def dashed(self):
        return self._forms["dashed"]

    def dash_dot(self):
        return self._forms["dash-dot"]

    def dotted(self):
        return self._forms["dotted"]


class LineStyle:
    """Gestion du style graphique d’une trajectoire"""
    def __init__(self, color, form="-"):
        self._color = color
        self._form = form

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def form(self):
        return self._form

    @form.setter
    def form(self, value):
        self._form = value

    def get_lineStyle(self):
        return self.color + self.form
