"""
Champs des gradients
"""
import numpy as np
import pylab as pl
from tools.line_style_form import Color


class Field:
    """Gestion du champ des gradients"""
    def __init__(self, col=Color()):
        self._params = {"color": col.green()}

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value

    def get_color(self):
        return self.params["color"]

    def plot(self, modl, xaxis, yaxis):
        xstr = xaxis.start
        xend = xaxis.end
        xmsh = xaxis.size_subdiv
        ystr = yaxis.start
        yend = yaxis.end
        ymsh = yaxis.size_subdiv
        xgrid, ygrid = np.mgrid[xstr:xend:xmsh, ystr:yend:ymsh]
        xfield, yfield = modl.get_field(xgrid, ygrid)
        col_field = self.get_color()
        return pl.quiver(xgrid, ygrid, xfield, yfield, color=col_field)
