"""
Conditions initiales
"""


class Initial:
    """Gestion d'une condition générale"""
    def __init__(self, cords, param):
        self._cords = cords
        self._param = param

    @property
    def cords(self):
        return self._cords

    @cords.setter
    def cords(self, value):
        self._cords = value

    @property
    def param(self):
        return self._param

    @param.setter
    def param(self, value):
        self._param = value

    def get_style(self):
        return self.param.get_lineStyle()


class Initials:
    """Gestion des conditions initiales"""
    def __init__(self):
        self._cnds = []

    @property
    def cnds(self):
        return self._cnds

    @cnds.setter
    def cnds(self, value):
        self._cnds = value

    def append(self, cords, param):
        self.cnds.append(Initial(cords, param))

    def make_initials(self, lx, ly, param):
        for x in lx:
            for y in ly:
                self.append((x, y), param)
