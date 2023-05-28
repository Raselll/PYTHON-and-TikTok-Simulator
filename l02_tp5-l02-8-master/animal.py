from abc import abstractmethod, ABC
from typing import List, Tuple

from accessoire import Accessoire, TypeAccessoire
from elements_tiktok import ElementViral


# TODO Je suis abstraite et j'hérite de ElementViral
@abstractmethod
class Animal(ElementViral , ABC):

    # TODO Implantez mon constructeur
    def __init__(self, nom:str , nb_pattes:int) -> None:
        self.nom = nom
        self.nb_pattes = nb_pattes
        self.liste_accessoires = []

    def __add__(self, accessoire: Accessoire) -> int:
        # TODO Retournez le score viral de l'animal plus celui de l'accessoire
        return accessoire.score_viral() + self.score_viral()

    def __iadd__(self, accessoire: Accessoire) -> 'Animal':
        # TODO Ajoutez l'accessoire à la liste de l'animal. Retournez l'animal en question
        #  Attention! Un animal n'ayant aucune patte ne peut enfiler des chaussures
        if accessoire.type_accessoire == TypeAccessoire.CHAUSSURES and self.nb_pattes == 0:
             print('Vous ne pouvez pas mettre de chaussures à un animal sans pieds')
        else:
            self.liste_accessoires.append(accessoire)
        return self


    @abstractmethod
    def crier(self) -> str:
        # TODO Rendez-moi abstraite
        pass

    def score_viral(self) -> int:
        # TODO Retournez la somme du score viral des accessoires présents dans la liste d'accessoires de l'animal
        score = 0
        for i in self.liste_accessoires:
            score += i.score_viral()
        return score




def calcul_meilleur_animal(animaux: List[Animal]) -> Tuple[str, int]:
    # TODO Retournez le nom et le score viral de l'animal ayant le score le plus haut
    return max(animaux , key=lambda x : x.score_viral()).nom , max(animaux , key=lambda x : x.score_viral()).score_viral()

