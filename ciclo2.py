from unittest import TestCase

from Arreglo import Arreglo

class ciclo2(TestCase):
    def test_numeroElementos(self):
        self.assertEqual(Arreglo().numeroElementos(""),[0,0],"calculo de elementos vacio")

    def test_unNumeroUnMinimo(self):
        self.assertEqual(Arreglo().numeroElementos("1"), [1, 1], "calculo de elementos 1 y numero minimo 1")

    def test_dosNumerosUnMinimo(self):
        self.assertEqual(Arreglo().numeroElementos("1,2"), [2, 1], "calculo de elementos 2 y numero minimo 1")