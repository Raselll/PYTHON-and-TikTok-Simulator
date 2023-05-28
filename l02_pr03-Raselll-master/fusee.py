import math

from constantes import MASSE_VOLUMIQUE_CARBURANT, CHAMP_GRAVITATIONNEL
#-----MASSE_VOLUMIQUE_CARBURANT = 50.0  # En kg/l
#-----CHAMP_GRAVITATIONNEL = 9.81  # En m/s^2

class Piece:
    def __init__(self, nom: str, hauteur: float, masse: float, prix: float) -> None:
        self.nom = nom
        self.hauteur = hauteur  # En m
        self.masse = masse  # En kg
        self.prix = prix  # En $CAN

    def __str__(self) -> str:
        return (f"{self.nom}, hauteur = {self.hauteur}m, masse = {self.masse}kg, prix = {self.prix}$")


class Capsule(Piece):
    def __init__(self, nom: str, hauteur: float, masse: float, prix: float, places: int) -> None:
        super().__init__(nom, hauteur, masse, prix)

        self.places = places  # En personnes

    def __str__(self) -> str:
        return (f"Capsule: {super().__str__()}, places = {self.places}personne(s)")


class Reservoir(Piece):
    def __init__(self, nom: str, hauteur: float, masse_vide: float, prix: float, capacite: float) -> None:
        super().__init__(nom, hauteur, masse_vide, prix)

        self.capacite = capacite  # En litres

    def __str__(self) -> str:
        return (f"Réservoir: {super().__str__()}, capacité = {self.capacite}L")

    @property
    def masse_rempli(self) -> float:
        # TODO calculez la masse du réservoir rempli.Utilisez MASSE_VOLUMIQUE_CARBURANT
        # -----MASSE_VOLUMIQUE_CARBURANT = 50.0  # En kg/l
        masse_reservoir = ((MASSE_VOLUMIQUE_CARBURANT * self.capacite) + self.masse)
        return masse_reservoir

class Moteur(Piece):
    def __init__(self, nom: str, hauteur: float, masse: float, prix: float, impulsion_specifique: int) -> None:
        super().__init__(nom, hauteur, masse, prix)

        self.impulsion_specifique = impulsion_specifique  # En secondes

    def __str__(self) -> str:
        return (f"Moteur: {super().__str__()}, impulsion spécifique = {self.impulsion_specifique}s")


class Fusee:
    """
    La classe représentant une fusée simple.

    Une fusée a comme attributs publics:
    * Un nom

    Une fusée a comme attributs privés:
    * Une capsule
    * Un réservoir
    * Un moteur
    """

    # TODO Implanter le constructeur avec les différentes pièces comme attributs privés
    # def __init__(self, couleur, taille):
    #   self.couleur = couleur # publique
    #   self.__taille = taille # privée

    def __init__(self, nom, capsule, reservoir, moteur ):
        self.nom = nom
        self.__capsule = capsule
        self.__reservoir = reservoir
        self.__moteur = moteur

    #Pour la function ci-dessous, la structure du code est celle du test. La raison pourqui elle ne passe pas est dûe à des défauts mineurs tels les indontations en trop.
    def __str__(self) -> str:
        # TODO Implantez la fonction __str__ pour permettre l'affichage de la fusée
        return (f'Fusée: \n \t  Nom: {self.nom} \n \t   Hauteur totale: {self.__reservoir.hauteur + self.__capsule.hauteur + self.__moteur.hauteur}m  \n \t   Masse totale (remplie): {self.__reservoir.masse_rempli+ self.__capsule.masse + self.__moteur.masse}kg \n \t   Prix total: {self.__reservoir.prix + self.__capsule.prix + self.__moteur.prix}$ \nPièces: \n \t {self.__capsule} \n \t {self.__reservoir} \n \t {self.__moteur}')

    @property
    def masse(self) -> float:
        # TODO Calculez la masse totale de la fusée (incluant le carburant)
        self.masse_capsule = self.__capsule.masse
        self.masse_reservoir = self.__reservoir.masse_rempli
        self.masse_moteur = self.__moteur.masse

        self.masse_finale = (self.masse_capsule + self.masse_reservoir + self.masse_moteur)
        return self.masse_finale

    @property
    def hauteur(self) -> float:
        # TODO Calculez la hauteur totale de la fusée
        self.hauteur_capsule = self.__capsule.hauteur
        self.hauteur_reservoir = self.__reservoir.hauteur
        self.hauteur_moteur = self.__moteur.hauteur

        self.hauteur_finale = (self.hauteur_capsule + self.hauteur_reservoir + self.hauteur_moteur)
        return self.hauteur_finale



    @property
    def prix(self) -> float:
        # TODO Calculez le prix total de la fusée
        self.prix_capsule = self.__capsule.prix
        self.prix_reservoir = self.__reservoir.prix
        self.prix_moteur = self.__moteur.prix

        self.prix_finale = self.prix_capsule + self.prix_reservoir + self.prix_moteur
        return self.prix_finale

    def calculer_deltav(self) -> float:
        # TODO À partir de la masse, du moteur et du réservoir,calculez le deltaV disponible de la fusée dans l'atmosphère. Utilisez la constante CHAMP_GRAVITATIONNEL
        delta_v = (self.__moteur.impulsion_specifique * CHAMP_GRAVITATIONNEL * math.log((self.masse)/(self.__reservoir.masse + self.__capsule.masse + self.__moteur.masse)))
        return delta_v


if __name__ == '__main__':
    # Reservoir.masse_rempli
    reservoir = Reservoir("Pichet", 0.4, 0.5, 20, 2)
    masse_rempli = reservoir.masse_rempli
    print(f"Une fois rempli, {reservoir.nom} a une masse de {masse_rempli} kg")
    print()

    # Fusee constructeur
    capsule = Capsule("Exigüe", 1.0, 750, 1300.0, 1)
    reservoir = Reservoir("Pichet", 0.4, 0.5, 20.0, 2)
    moteur = Moteur("Pantera Arctic Cat Triple 800", 4, 2000, 14000.0, 199)
    fusee = Fusee("Romano Fafard", capsule, reservoir, moteur)

    # Fusee.masse
    print(f"La masse de la fusée {fusee.nom} est {fusee.masse}kg")
    print()

    # Fusee.hauteur
    print(f"La hauteur de la fusée {fusee.nom} est {fusee.hauteur}m")
    print()

    # Fusee.prix
    print(f"Le prix de la fusée {fusee.nom} est {fusee.prix}$")
    print()

    # Fusee.__str__
    print(f"fusee est de type {type(fusee)}")
    print()

    print(fusee.calculer_deltav())
