from typing import List

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from constantes import DELTA_V_MINIMUM_PAR_CORPS_CELESTE, CHEMIN_CAPSULES, CHEMIN_MOTEURS, CHEMIN_RESERVOIRS
from fichiers_pieces import charger_capsules_df, charger_moteurs_df, charger_reservoirs_df
from fusee import Fusee, Capsule, Reservoir, Moteur


def creer_capsules(capsules_df: pd.DataFrame) -> List[Capsule]:
    # TODO Transformez le dataframe des capsules en liste d'objets de type Capsule
    liste_capsules = capsules_df.values.tolist()
    ccapsules = [Capsule(i[0], i[1], i[2], i[3], i[4]) for i in liste_capsules]
    return ccapsules



def creer_moteurs(moteurs_df: pd.DataFrame) -> List[Moteur]:
    # TODO Transformez le dataframe des moteurs en liste d'objets de type Moteur
    liste_moteurs = moteurs_df.values.tolist()
    cmoteurs = [Moteur(i[0], i[1], i[2], i[3], i[4]) for i in liste_moteurs]
    return cmoteurs


def creer_reservoirs(reservoirs_df: pd.DataFrame) -> List[Reservoir]:
    # TODO Transformez le dataframe des reservoir en liste d'objets de type Reservoir
    liste_reservoirs = reservoirs_df.values.tolist()
    creservoir = [Reservoir(i[0], i[1], i[2], i[3], i[4]) for i in liste_reservoirs]
    return creservoir


def corps_celestes_accessibles(fusee: Fusee) -> List[str]:
    # TODO Retournez la liste des corps célestes accessibles par la fusée. Utiliser DELTA_V_MINIMUM_PAR_CORPS_CELESTE

    x = [ ]
    for elements in DELTA_V_MINIMUM_PAR_CORPS_CELESTE:
        if fusee.calculer_deltav() >= DELTA_V_MINIMUM_PAR_CORPS_CELESTE[elements]:
            x.append(elements)
        else:
            pass
    return x

def comparer_fusee(fusee_1: Fusee, fusee_2: Fusee) -> None:
    # TODO créer un grouped barplot comparant les fusées passées en paramètre en fonction des trois métriques suivantes:
    #  * Masse / Coût
    #  * DeltaV / Coût
    #  * DeltaV / Masse
    # TODO Générez un dataframe avec trois colonnes; fusée, résultats des différents ratios et type_ratio

    # https://www.geeksforgeeks.org/create-a-grouped-bar-plot-in-matplotlib/
    Diagramme = plt.figure()
    group_barplot1 = [fusee_1.calculer_deltav()/fusee_1.masse,fusee_2.calculer_deltav()/fusee_2.masse]
    group_barplot2 = [fusee_1.calculer_deltav()/fusee_1.prix,fusee_2.calculer_deltav()/fusee_2.prix]
    group_barplot3 = [fusee_1.hauteur/fusee_1.masse,fusee_2.hauteur/fusee_2.masse]

    x = np.arange(2)
    width = 0.2
    plt.bar(x - 0.2, group_barplot1, width, color = 'cyan')
    plt.bar(x, group_barplot2, width, color = 'orange')
    plt.bar(x + 0.2, group_barplot3, width, color = 'green')
    plt.xticks(x, [(fusee_1.nom), (fusee_2.nom)])
    plt.ylabel('Ratios')
    plt.ylim(0, 0.20)
    plt.xlabel = ()
    plt.title = ("Comparaison de ratios pour les fusees" + (fusee_1.nom))
    plt.legend(['DeltaV / masse', 'DeltaV / Cout', 'hauteur / Masse'])
    plt.show()

    return Diagramme

if __name__ == '__main__':
    # creer_capsules
    capsules_df = charger_capsules_df(CHEMIN_CAPSULES)
    capsules = creer_capsules(capsules_df)
    for capsule in capsules:
        print(capsule)
    print()

    # creer_moteurs
    moteurs_df = charger_moteurs_df(CHEMIN_MOTEURS)
    moteurs = creer_moteurs(moteurs_df)
    for moteur in moteurs:
        print(moteur)
    print()

    # creer_reservoirs
    reservoirs_df = charger_reservoirs_df(CHEMIN_RESERVOIRS)
    reservoirs = creer_reservoirs(reservoirs_df)
    for reservoir in reservoirs:
        print(reservoir)
    print()

    # corps_celestes_accessibles
    capsule = Capsule("PasDBonSens", 1.5, 840.0, 600.0, 1)
    reservoir_1 = Reservoir("Piscine", 25.0, 9000.0, 13000.00, 6480.0)
    moteur = Moteur("La Puissance", 12.0, 15000.0, 39000.00, 295)
    fusee_1 = Fusee("Romano Fafard", capsule, reservoir_1, moteur)

    deltaV = fusee_1.calculer_deltav()
    corps_celestes = corps_celestes_accessibles(fusee_1)
    print(f"La fusée {fusee_1.nom} peut aller, avec {deltaV:.2f} de deltaV, jusqu'à: {corps_celestes}")

    # comparer_fusee
    reservoir_2 = Reservoir("Pichet", 0.4, 0.5, 20, 2)
    fusee_2 = Fusee("Romano Fafard Lite", capsule, reservoir_2, moteur)
    comparer_fusee(fusee_1, fusee_2)
