"""
Modèle de développement des bactéries dans un substrat
"""
from mdl.model_bacteries import Bacteries
from tools.axis import Axis
from tools.cnds_initiales import Initials, Initial
from tools.line_style_form import LineStyle, Color, Form
from tools.phase_diag import PhaseDiag
from tools.evolution import Evolution
from tools.dynamic_model import DynamicModel
from tools.analysis import Analysis
import numpy as np


def mainModeleBasique(mdl, phase_diag=True, exprtpng=False):
    """Affiche le modèle de base"""
    # Les axes
    xaxis = Axis(0, 5, 15j)
    yaxis = Axis(0, 1, 15j)
    taxis = Axis(0, 5, 500)
    # Couleurs et formes
    col = Color()
    frm = Form()
    red_solid = LineStyle(col.red())
    blue_dhdot = LineStyle(col.blue(), frm.dash_dot())
    green_dotted = LineStyle(col.green(), frm.dotted())
    # Conditions initiales
    cnds = Initials()
    cnds.append((0.5, 0.5), red_solid)
    cnds.append((0.25, 0.75), blue_dhdot)
    cnds.append((0.75, 0.25), green_dotted)
    # Evolution
    evol = Evolution()
    # Graphes séparés
    evol.plot(mdl, cnds, xaxis, [yaxis, yaxis], taxis, exprtpng)
    # Graphes superposés
    evol.plot(mdl, cnds, xaxis, [yaxis], taxis, exprtpng)
    if phase_diag:
        # Portrait des phases
        xaxis = Axis(0, 1, 15j)
        yaxis = Axis(0, 1, 15j)
        phases = PhaseDiag()
        phases.portrait(mdl, cnds, xaxis, yaxis, taxis, exprtpng)


def mainEvolParams(mdl, exprtpng=False):
    """Affiche l'impact des différents paramètres du modèle"""
    # Les axes
    xaxis = Axis(0, 1, 15j)
    yaxis = Axis(0, 1, 15j)
    taxis = Axis(0, 1, 500)
    # Couleurs et formes
    col = Color()
    frm = Form()
    red_solid = LineStyle(col.red())
    blue_dhdot = LineStyle(col.blue(), frm.dash_dot())
    green_dotted = LineStyle(col.green(), frm.dotted())
    # Conditions initiales
    cnds = Initials()
    cnds.append((0.5, 0.5), red_solid)
    cnds.append((0.25, 0.75), blue_dhdot)
    cnds.append((0.75, 0.25), green_dotted)
    # Analyse
    ana = Analysis(mdl.title, figsize=(15, 9))
    for p in ["mu", "L", "k", "m", "delta"]:
        ana.plot_evol_param(mdl, p, [0, 0.25, 0.75, 1],
                            cnds, xaxis, yaxis, taxis, exprtpng)


def mainDynamic(inf=0, sup=2):
    """Affiche la fenêtre du modèle dynamique"""
    # Les axes
    xaxis = Axis(0, 5, 15j)
    yaxis = Axis(0, 3, 15j)
    taxis = Axis(0, 5, 500)
    # Couleurs et formes
    col = Color()
    frm = Form()
    red_solid = LineStyle(col.red())
    blue_dhdot = LineStyle(col.blue(), frm.dash_dot())
    # Condition initiale
    cndzr = Initial((0.5, 0.5), red_solid)
    # Plot
    mdl = Bacteries(mu=0.5, L=0.5, k=0.5, m=0.5, delta=0.5)
    dymodel = DynamicModel(mdl)
    dymodel.plot(cndzr, blue_dhdot, xaxis, yaxis, taxis, inf, sup)


def mainS0X0(mdl):
    # Les axes
    taxis = Axis(0, 5, 500)
    # Couleurs et formes
    col = Color()
    red_solid = LineStyle(col.red())
    Ls = [0, 0.1, 0.2, 0.3, 0.4, 0.5]
    cnds = Initials()
    cnds.make_initials(Ls, [0.5], red_solid)
    # Analyse
    evol = Analysis(mdl.title)
    evol.plot_cross(mdl, cnds, taxis, Ls, 'S0')
    Lx = [0.5, 0.6, 0.7, 0.8, 0.9, 1]
    cnds = Initials()
    cnds.make_initials([0.5], Lx, red_solid)
    evol.plot_cross(mdl, cnds, taxis, Lx, 'X0')


def mainParams(mdl):
    # Les axes
    taxis = Axis(0, 5, 500)
    # Couleurs et formes
    col = Color()
    red_solid = LineStyle(col.red())
    # Conditions initiales
    cnds = Initials()
    # Evolution
    cnds.append((0.5, 0.5), red_solid)
    cnds.append((0.25, 0.75), red_solid)
    # Analyse
    evol = Analysis(mdl.title)
    epsilon = 0.001
    evol.plot_param(mdl, "mu", np.arange(0, 1, 0.001), cnds, taxis, epsilon)
    evol.plot_param(mdl, "L", np.arange(-1, 2, 0.001), cnds, taxis, epsilon)
    evol.plot_param(mdl, "m", np.arange(-1, 2, 0.01), cnds, taxis, epsilon)
    evol.plot_diff(mdl, "delta", np.arange(-2, 2, 0.01), cnds, taxis, epsilon)


if __name__ == "__main__":
    mdl = Bacteries(mu=0.5, L=0.5, k=0.5, m=0.5, delta=0.5)
    mainDynamic()
    mainModeleBasique(mdl)
    mainEvolParams(mdl)
    # mainS0X0(mdl)
    # mainParams(mdl)
