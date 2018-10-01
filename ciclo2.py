from unittest import TestCase

from arregloCiclo2 import ArregloCiclo2

class ciclo2(TestCase):
    def test_numeroElementos(self):
        self.assertEqual(ArregloCiclo2().numeroElementos(""),[0,0],"calculo de elementos vacio")

    def test_unNumeroUnMinimo(self):
        self.assertEqual(ArregloCiclo2().numeroElementos("1"), [1, 1], "calculo de elementos 1 y numero minimo 1")

    def test_dosNumerosUnMinimo(self):
        self.assertEqual(ArregloCiclo2().numeroElementos("1,2"), [2, 1], "calculo de elementos 2 y numero minimo 1")

    def test_tresNumerosUnMinimo(self):
        self.assertEqual(ArregloCiclo2().numeroElementos("4,2,3"), [3, 2], "calculo de elementos 2 y numero minimo 1")