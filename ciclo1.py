from unittest import TestCase

from Arreglo import Arreglo

class ciclo1(TestCase):
    def test_numeroElementos(self):
        self.assertEqual(Arreglo().numeroElementos(""),0,"calculo de elementos vacio")

