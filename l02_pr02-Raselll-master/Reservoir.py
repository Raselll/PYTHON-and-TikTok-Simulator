# -*- coding: utf-8 -*-
# Nom_du_fichier: Reservoir.py
# Creer le      :
# Creer par     :
# Version num   :
# Modifier le   :

import matplotlib.pyplot as plt
from IPython.display import clear_output
from Molecule import moleculesSeTouche, deplacerMolecule, creerListMolecules, creerMolecule
from Molecule import ajusteDirApresCollision, inverseDirMolecule


def creerReservoir(hauteur, largeur, posParoi, nbMoleculesG, nbMoleculesD):
    # TODO 3.2.1 Créer le structure de données d'un réservoir
    # Utiliser creerListMolecules (voir 3.1.5)

    reservoir = {'h': hauteur, 'l': largeur, 'posPar': posParoi, 'mG': nbMoleculesG, 'mD': nbMoleculesD}

    reservoir['mG'] = creerListMolecules(reservoir['h'], 0, reservoir['posPar'], reservoir['mG'])
    reservoir['mD'] = creerListMolecules(reservoir['h'], reservoir['posPar'], reservoir['l'], reservoir['mD'])
    reservoir['lCD'] = [0] * int((nbMoleculesD * (nbMoleculesD - 1) / 2))
    reservoir['lCG'] = [0] * int((nbMoleculesG * (nbMoleculesG - 1) / 2))

    return reservoir


def colision(reservoir):
    # TODO 3.2.2 Vérifier si il y a des collisions entre des molécules dans un réservoir
    # Pour chaque molécule vérifier si elles est en collision avec une autre molécule du réservoir
    if 'mG' not in reservoir:
        return

    c = 0
    for i in range(len(reservoir['mG'])):
        for j in range((i + 1), len(reservoir['mG'])):
            if moleculesSeTouche(reservoir['mG'][i], reservoir['mG'][j]) is True:
                reservoir['lCG'][c] = 1
                reservoir['mG'][i], reservoir['mG'][j] = ajusteDirApresCollision(reservoir['mG'][i], reservoir['mG'][j])
            c += 1
    c = 0
    for i in range(len(reservoir['mD'])):
        for j in range((i + 1), len(reservoir['mD'])):
            if moleculesSeTouche(reservoir['mD'][i], reservoir['mD'][j]) is True:
                reservoir['lCD'][c] = 1
                reservoir['mD'][i], reservoir['mD'][j] = ajusteDirApresCollision(reservoir['mD'][i], reservoir['mD'][j])
            c += 1

    return reservoir


def inverseDirMolecules(reservoir):
    # TODO 3.2.3 Ajuster la direction des molécules qui touchent aux parois dans chaque réservoir
    # Faire appel à inverseDirMolecule(mol, paroiG, paroiD, hauteur) (3.2.3)
    for i in range(len(reservoir['mG'])):
        inverseDirMolecule(reservoir['mG'][i], 0, reservoir['posPar'], reservoir['h'])
    for i in range(len(reservoir['mD'])):
        inverseDirMolecule(reservoir['mD'][i], reservoir['posPar'], reservoir['l'], reservoir['h'])

    return reservoir


def getTemperature(reservoir, cote):
    # TODO 3.2.4 Calcule la température de chaque côté du réservoir.
    # Utiliser la formule dans le Readme
    if cote == 'Gauche':
        Energie = 0
        masse = 1
        Temperature = 0
        N = len(reservoir['mG'])
        for i in range(0, N):
            Energie += ((1 / 2) * masse * (
                        (((reservoir['mG'][i]['dx']) ** 2 + (reservoir['mG'][i]['dy']) ** 2) ** (1 / 2)) ** 2))
        Temperature = Energie / N

    if cote == 'Droite':
        Energie = 0
        masse = 1
        Temperature = 0
        N = len(reservoir['mD'])
        for i in range(0, N):
            Energie += ((1 / 2) * masse * (
                        (((reservoir['mD'][i]['dx']) ** 2 + (reservoir['mD'][i]['dy']) ** 2) ** (1 / 2)) ** 2))
        Temperature = Energie / N

    return Temperature


#####################################################
# Donner
#####################################################
def affichage(reservoir):
    txt = "Température côté Gauche: {:.2f}C \t\t\t\t\t Température côté Droit: {:.2f}C".expandtabs()
    plt.figure(figsize=(20, 10))
    plt.plot([reservoir['posPar'], reservoir['posPar']], [0, reservoir['h']], 'k-', linewidth=10)
    plt.axis([-20, reservoir['l'] + 20, -20, reservoir['h'] + 20])
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.title(txt.format(getTemperature(reservoir, "Gauche"), getTemperature(reservoir, "Droite")), fontsize=23)

    for k in [['mG', 'ro'], ['mD', 'go']]:
        for i in range(len(reservoir[k[0]])):
            inte = min(max((abs(reservoir[k[0]][i]['dx']) + abs(reservoir[k[0]][i]['dy'])) / 60, 0.2), 1)
            plt.plot(reservoir[k[0]][i]['x'], reservoir[k[0]][i]['y'], k[1], alpha=inte, ms=reservoir[k[0]][i]['rayon'])
            reservoir[k[0]][i] = deplacerMolecule(reservoir[k[0]][i])

    plt.pause(0.01)
    clear_output()


def deplacerMolecules(reservoir):
    # TODO 3.2.6
    # deplacer_molecule deplace les molecules du reservoir
    # Cette funcytion recoit comme parametre un objet de type reservoire est execute les etapes suivantes:
    # 1) Inverser la direction des molecules du reservoir
    inverseDirMolecules(reservoir)

    # 2) Afficher les molecules
    affichage(reservoir)

    # 3) Determination des colision des molecules
    colision(reservoir)

    return reservoir


if __name__ == '__main__':
    hauteur, largeur, posParoi, nbMoleculesG, nbMoleculesD = 2000, 2000, 1300, 100, 50
    reservoir = creerReservoir(hauteur, largeur, posParoi, nbMoleculesG, nbMoleculesD)
    for i in range(1000):
        reservoir = deplacerMolecules(reservoir)
