from unittest import TestCase

from Arreglo import Arreglo

class ciclo2(TestCase):
    def test_cero_elementos(self):
        self.assertEqual(Arreglo().numeroElementos(""),[0,0,0],"calculo de elementos vacio")