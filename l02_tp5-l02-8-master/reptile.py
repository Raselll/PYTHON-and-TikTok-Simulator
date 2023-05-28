from abc import ABC
from typing import List

from animal import Animal


# TODO Je suis abstraite et j'hérite de Animal
class Reptile(Animal, ABC):

    # TODO Implantez mon constructeur
    def __init__(self, nom: str , nb_pattes: int , est_nocturne: bool) -> None:
        super().__init__(nom , nb_pattes)
        self.est_nocturne = est_nocturne


    def __str__(self) -> str:
        # TODO Je dois retournez une chaine de caractère semblable à :
        #  Le TYPE_REPTILE NOM_REPTILE est nocturne.
        #  ou
        #  Le TYPE_REPTILE NOM_REPTILE est diurne.
        if self.est_nocturne == True:
            return f'Le {type(self).__name__} {self.nom} est nocturne.'
        elif self.est_nocturne == False:
            return f'Le {type(self).__name__} {self.nom} est diurne.'


# TODO J'hérite de Reptile
class Serpent(Reptile):

    # TODO Implantez mon constructeur
    def __init__(self, nom:str , est_nocturne:bool , est_venimeux:bool ) -> None:
        super().__init__(nom , False , est_nocturne)
        self.est_venimeux = est_venimeux
    def __str__(self) -> str:
        # TODO Ajouter les phrases suivantes à la chaine de base de Reptile:
        #  Il est venimeux.
        #  ou
        #  Il n'est pas venimeux.
        #  Utilisez la methode __str__ de Reptile avec: super(Serpent, self).__str__()
        if self.est_nocturne == False and self.est_venimeux == False:
            return f"Le {super(Serpent,self).__str__()} {self.nom} est diurne. Il n'est pas venimeux."
        elif self.est_nocturne == False and self.est_venimeux == True:
            return f"Le {super(Serpent, self).__str__()} {self.nom} est diurne. Il est venimeux."
        elif self.est_nocturne == True and self.est_venimeux == False:
            return f"{super(Serpent, self).__str__()} Il n'est pas venimeux."
        elif self.est_nocturne == True and self.est_venimeux == True:
            return f"{super(Serpent, self).__str__()} Il est venimeux."

    def crier(self) -> str:
        # TODO Retournez le cri du serpent: sssss
        return 'sssss'
