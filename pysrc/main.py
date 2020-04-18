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

from tools.analyse import Analyse


def main(mu, L, k, m, delta, phase_diag=True):
    # Le modèle
    mdl = Bacteries(mu, L, k, m, delta)
    # Les axes
    xaxis = Axis(0, 5, 15j)
    yaxis = Axis(0, 5, 15j)
    yaxis1 = Axis(0, 1, 15j)
    yaxis2 = Axis(0, 1, 15j)
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
    evol = Evolution(str(mdl))
    evol.plot(mdl, cnds, xaxis, [yaxis1, yaxis2], taxis, exprtpng=False)
    if phase_diag:
        # Portrait des phases
        xaxis = Axis(0, 1, 15j)
        yaxis = Axis(0, 1, 15j)
        phases = PhaseDiag(str(mdl))
        phases.portrait(mdl, cnds, xaxis, yaxis, taxis, exprtpng=False)


def mainSuperpose(mu, L, k, m, delta, phase_diag=True):
    # Le modèle
    mdl = Bacteries(mu, L, k, m, delta)
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
    #Ls = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    #cnds.make_initials(Ls, [0.5], red_solid)
    # Evolution
    evol = Evolution(str(mdl))
    evol.plot(mdl, cnds, xaxis, [yaxis], taxis, exprtpng=False)
    if phase_diag:
        # Portrait des phases
        xaxis = Axis(0, 1, 15j)
        yaxis = Axis(0, 1, 15j)
        phases = PhaseDiag(str(mdl))
        phases.portrait(mdl, cnds, xaxis, yaxis, taxis, exprtpng=False)

def mainS0X0(mu, L, k, m, delta):
    # Le modèle
    mdl = Bacteries(mu, L, k, m, delta)
    # Les axes
    taxis = Axis(0, 5, 500)
    # Couleurs et formes
    col = Color()
    red_solid = LineStyle(col.red())
    Ls = [0, 0.1, 0.2, 0.3, 0.4, 0.5]
    cnds = Initials()
    cnds.make_initials(Ls, [0.5], red_solid)
    # Evolution
    evol =Analyse(str(mdl))
    evol.plotSX(mdl, cnds, taxis, Ls, 'S0')
    Lx = [0.5, 0.6, 0.7, 0.8, 0.9, 1]
    cnds = Initials()
    cnds.make_initials([0.5], Lx, red_solid)
    # Evolution
    evol = Analyse(str(mdl))
    evol.plotSX(mdl, cnds, taxis, Lx, 'X0')

def mainMu(L, k, m, delta):
    # Les axes
    taxis = Axis(0, 10, 500)
    # Couleurs et formes
    col = Color()
    red_solid = LineStyle(col.red())
    cnds = Initials()
    epsilon = 0.0001
    # Evolution
    cnds.append((0.5, 0.5), red_solid)
    cnds.append((0.25, 0.75), red_solid)
    #cnds.append((0.75, 0.25), green_dotted)
    evol =Analyse("Développement des bactéries dans un substrat")
    evol.plotMu(L, k, m, delta, cnds, taxis, epsilon)

def mainL(mu, k, m, delta):
    # Les axes
    taxis = Axis(0, 10, 500)
    # Couleurs et formes
    col = Color()
    red_solid = LineStyle(col.red())
    cnds = Initials()
    epsilon = 0.001
    # Evolution
    cnds.append((0.5, 0.5), red_solid)
    cnds.append((0.25, 0.75), red_solid)
    #cnds.append((0.75, 0.25), green_dotted)
    evol =Analyse("Développement des bactéries dans un substrat")
    evol.plotL(mu, k, m, delta, cnds, taxis, epsilon)

def mainM(mu, L, k, delta):
    # Les axes
    taxis = Axis(0, 10, 500)
    # Couleurs et formes
    col = Color()
    red_solid = LineStyle(col.red())
    cnds = Initials()
    epsilon = 0.001
    # Evolution
    cnds.append((0.5, 0.5), red_solid)
    cnds.append((0.25, 0.75), red_solid)
    #cnds.append((0.75, 0.25), green_dotted)
    evol =Analyse("Développement des bactéries dans un substrat")
    evol.plotM(mu, L, k, delta, cnds, taxis, epsilon)

def mainDelta(mu, L, k, m):
    # Les axes
    taxis = Axis(0, 10, 500)
    # Couleurs et formes
    col = Color()
    red_solid = LineStyle(col.red())
    cnds = Initials()
    epsilon = 0.001
    # Evolution
    cnds.append((0.5, 0.5), red_solid)
    cnds.append((0.25, 0.75), red_solid)
    #cnds.append((0.75, 0.25), green_dotted)
    evol =Analyse("Développement des bactéries dans un substrat")
    evol.plotDelta(mu, L, k, m, cnds, taxis, epsilon)




def mainDynamic(mu, L, k, m, delta):
    # Le modèle
    mdl = Bacteries(mu, L, k, m, delta)
    # Les axes
    xaxis = Axis(0, 5, 15j)
    yaxis = Axis(-5, 5, 15j)
    taxis = Axis(0, 5, 500)
    # Couleurs et formes
    col = Color()
    frm = Form()
    red_solid = LineStyle(col.red())
    blue_dhdot = LineStyle(col.blue(), frm.dash_dot())
    # Condition initiale
    cndzr = Initial((0.5, 0.5), red_solid)
    # Plot
    dymodel = DynamicModel(mdl)
    dymodel.plot(cndzr, blue_dhdot, xaxis, yaxis, taxis)


if __name__ == "__main__":
    #main(mu=1, L=1, k=1, m=1, delta=1, phase_diag=False)
    #mainSuperpose(mu=1, L=1, k=1, m=1, delta=1, phase_diag=True)
    #mainDynamic(mu=1, L=1, k=1, m=1, delta=1)
    mainS0X0(mu=1, L=1, k=1, m=1, delta=1)
    mainMu(L=1, k=1, m=1, delta=1)
    mainL(mu=1, k=1, m=1, delta=1)
    mainM(mu=1, L=1, k=1, delta=1)
    mainDelta(mu=1, L=1, k=1, m=1)
