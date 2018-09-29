from unittest import TestCase

from Arreglo import Arreglo

class ciclo2(TestCase):
    def test_cero_elementos(self):
        self.assertEqual(Arreglo().numeroElementos(""),[0,0,0],"calculo de elementos vacio")

    def test_unNumeroUnMinimoUnMaximo(self):
        self.assertEqual(Arreglo().numeroElementos("1"), [1, 1, 1], "calculo de elementos 1 numero minimo 1 numero maximo 1")

    def test_DosNumeroUnMinimoUnMaximo(self):
        self.assertEqual(Arreglo().numeroElementos("1,3"), [2, 1, 3], "calculo de dos elementos numero minimo 1 numero maximo 3")

    def test_cualquierNumeroUnMinimoUnMaximo(self):
        self.assertEqual(Arreglo().numeroElementos("1,3,5,8"), [4, 1, 8], "calculo de dos elementos numero minimo 1 numero maximo 3")