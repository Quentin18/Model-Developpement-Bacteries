"""
Modèle de développement des bactéries dans un substrat
"""
from tools.axis import Axis
from tools.cnds_initiales import Initials
from tools.line_style_form import LineStyle, Color, Form
from tools.phase_diag import PhaseDiag
from tools.evolution import Evolution
from mdl.model_bacteries import Bacteries


def main(mu, L, k, m, delta, phase_diag=True):
    # Le modèle
    mdl = Bacteries(mu, L, k, m, delta,
                    "Développement des bactéries dans un substrat")
    # Les axes
    xaxis = Axis(0, 5, 15j)
    yaxis = Axis(0, 5, 15j)
    yaxis1 = Axis(0, 1, 15j, "Concentration de nourriture")
    yaxis2 = Axis(0, 1, 15j, "Concentration de bactéries")
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


if __name__ == "__main__":
    main(mu=1, L=1, k=1, m=1, delta=1, phase_diag=True)
