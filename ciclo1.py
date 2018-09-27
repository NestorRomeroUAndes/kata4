from unittest import TestCase

from Arreglo import Arreglo

class ciclo1(TestCase):
    def test_numeroElementos(self):
        self.assertEqual(Arreglo().numeroElementos(""),0,"calculo de elementos vacio")

    def test_un_numero(self):
        self.assertEqual(Arreglo().numeroElementos("1"), 1, "Calculo de Un elemento")