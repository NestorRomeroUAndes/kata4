from unittest import TestCase

from Arreglo import Arreglo

class ciclo4(TestCase):
    def test_cero_elementos(self):
        self.assertEqual(Arreglo().numeroElementos(""),[0,0,0,0],"calculo de elementos vacio y todo lo demas cero")

    def test_unNumeroUnMinimoUnMaximoPromedio(self):
        self.assertEqual(Arreglo().numeroElementos("1"), [1, 1, 1, 1],
                         "calculo de elementos 1 numero minimo 1 numero maximo 1 promedio 1")

    def test_DosNumeroUnMinimoUnMaximoPromedio(self):
        self.assertEqual(Arreglo().numeroElementos("1,3"), [2, 1, 3, 2],
                         "calculo de dos elementos numero minimo 1 numero maximo 3 promedio 2")

    def test_DosNumeroUnMinimoUnMaximoPromedio(self):
        self.assertEqual(Arreglo().numeroElementos("1,3,4,5"), [4, 1, 5, 3.25],
                         "calculo de dos elementos numero minimo 1 numero maximo 1 promedio 1")
