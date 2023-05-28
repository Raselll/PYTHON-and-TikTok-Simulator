import unittest
from unittest import TestCase
from fonctions_a_tester import fizz_buzz,resoudre_equation

class TestFizzBuzz(TestCase):
    def test_fizz_buzz_3(self):
        # TODO Tester avec un multiple de 3
        result = fizz_buzz(9)
        self.assertEqual(result, 'fizz')



    def test_fizz_buzz_5(self):
        # TODO Tester avec un multiple de 5
        self.assertEqual(fizz_buzz(25) , 'buzz')



    def test_fizz_buzz_3_5(self):
        # TODO Tester avec un multiple de 3 et 5
        self.assertEqual(fizz_buzz(15) , 'fizzbuzz')


    def test_fizz_buzz_non_facteur(self):
        # TODO Tester avec un nombre qui nombre'a pas 3 et 5 comme facteur
        #  et assurez-vous que la valeur en sotie soit une string
        self.assertEqual(fizz_buzz(2), str(2))


class TestResoudreEquation(TestCase):
    def test_resoudre_equation_sans_racine(self):
        # TODO Tester avec un polynome sans racines réelles
        #  et assurez-vous que la valeur en sortie est None
        self.assertEqual(resoudre_equation(1,1,1) , None)


    def test_resoudre_equation_une_racine(self):
        # TODO Tester avec un polynome avec une seule solution
        self.assertEqual(resoudre_equation(1, 2, 1), -1.0)



    def test_resoudre_equation_deux_racine(self):

        # TODO Tester avec un polynome avec deux solutions
        self.assertEqual(resoudre_equation(1, 0, -1), (1.0 , -1.0))




if __name__ == '__main__':
    unittest.main()
