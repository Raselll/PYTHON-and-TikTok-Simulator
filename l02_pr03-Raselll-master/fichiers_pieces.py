import pandas as pd
import json

from constantes import CHEMIN_CAPSULES, CHEMIN_MOTEURS, CHEMIN_RESERVOIRS, FICHIER_CAPSULE, FICHIERS_RESERVOIRS, \
    FICHIERS_MOTEURS


def charger_capsules_df(chemin_capsules: str) -> pd.DataFrame:
    # TODO Retournez un dataframe des capsules décrites dans le fichier FICHIER_CAPSULE.
    #  Il faut aussi renommer les colonnes pour que celles-ci soient plus lisibles

    # --- FICHIER_CAPSULE = "capsules.csv"
    # --- CHEMIN_CAPSULES = CHEMIN_PIECES + "/capsules"
    # --- n,h,m,p,pl
    df = (pd.read_csv(f'{chemin_capsules}/capsules.csv'))
    columns = ['n', 'h', 'm', 'p', 'pl']
    for elements in columns:
        df = df.rename(columns = {'n': 'nom', 'h': 'hauteur', 'm': 'masse', 'p': 'prix', 'pl': 'places'})

    return df

def charger_reservoirs_df(chemin_reservoirs: str) -> pd.DataFrame:
    # TODO Retournez un dataframe combiné des réservoirs décrits dans les fichiers FICHIERS_RESERVOIRS

    # --- Charge les réservoirs contenus dans les fichiers reservoir*.json dans un dataframe
    # --- chemin_reservoirs (str) : Une chaine de caractères du chemin vers le dossier reservoirs
    # --- CHEMIN_RESERVOIRS = CHEMIN_PIECES + "/reservoirs"
    # --- FICHIERS_RESERVOIRS = ["reservoir1.json", "reservoir2.json", "reservoir3.json"]
    with open(f'{chemin_reservoirs}/reservoir1.json') as f1:
        reservoir_df1 = json.load(f1)
    with open(f'{chemin_reservoirs}/reservoir2.json') as f2:
        reservoir_df2 = json.load(f2)
    with open(f'{chemin_reservoirs}/reservoir3.json') as f3:
        reservoir_df3 = json.load(f3)

    reservoir_df = pd.DataFrame(reservoir_df1 + reservoir_df2 + reservoir_df3)
    return reservoir_df

# Le code ci-dessous affiche la réponse attendue, mais les tests ne passent pas.
def charger_moteurs_df(chemin_moteurs: str) -> pd.DataFrame:
    # TODO Retournez un dataframe combiné des moteurs décrits dans les fichiers FICHIERS_MOTEURS
    # --- CHEMIN_MOTEURS = CHEMIN_PIECES + "/moteurs"
    # --- FICHIERS_MOTEURS = ["moteur1.ppl", "moteur2.ppl", "moteur3.ppl", "moteur4.ppl"]
    # --- chemin_moteurs (str) : Une chaine de caractères du chemin vers le dossier moteurs

    dict1 = {}
    dict2 = {}
    dict3 = {}
    dict4 = {}

    with open (f'{chemin_moteurs}/moteur1.ppl') as f4:
        cm1 = f4.readlines()
    with open (f'{chemin_moteurs}/moteur2.ppl') as f5:
        cm2 = f5.readlines()
    with open (f'{chemin_moteurs}/moteur3.ppl') as f6:
        cm3 = f6.readlines()
    with open (f'{chemin_moteurs}/moteur4.ppl') as f7:
        cm4 = f7.readlines()

    for element in cm1:
        if '=' in element:
            key, result = element.rstrip("\n").split("=")
            if key not in dict1.keys():
                dict1[key] = result

    for element in cm2:
        if '=' in element:
            key, result = element.rstrip("\n").split("=")
            if key not in dict2.keys():
                dict2[key] = result

    for element in cm3:
        if '=' in element:
            key, result = element.rstrip("\n").split("=")
            if key not in dict3.keys():
                dict3[key] = result

    for element in cm4:
        if '=' in element:
            key, result = element.rstrip("\n").split("=")
            if key not in dict4.keys():
                dict4[key] = result

    dict_cm_df = ([dict1] + [dict2] + [dict3] + [dict4])
    return (pd.DataFrame(dict_cm_df))

def filtrer_moteurs(moteurs_df: pd.DataFrame, impulsion_minimum: int) -> pd.DataFrame:
    # TODO Retourner un sous-ensemble filtré d'un df de moteurs où l'impulsion spécifique est au dessus d'un certain seuil

    moteurs = moteurs_df.astype({'impulsion specifique': int})
    return (moteurs_df.loc[((moteurs['impulsion specifique']) > impulsion_minimum)])



if __name__ == '__main__':
    # charger_capsules_df
    capsules = charger_capsules_df(CHEMIN_CAPSULES)
    print(capsules)
    print()

    # charger_reservoirs_df
    reservoirs = charger_reservoirs_df(CHEMIN_RESERVOIRS)
    print(reservoirs)
    print()

    # charger_moteurs_df
    moteurs = charger_moteurs_df(CHEMIN_MOTEURS)
    print(moteurs)
    print()

    # filtrer_moteurs
    moteurs_filtres = filtrer_moteurs(moteurs, 220)
    print(moteurs_filtres)
