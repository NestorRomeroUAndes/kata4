from unittest import TestCase

from arregloCiclo1 import ArregloCiclo1

class ciclo1(TestCase):
    def test_numeroElementos(self):
        self.assertEqual(ArregloCiclo1().numeroElementos(""),0,"calculo de elementos vacio")

    def test_un_numero(self):
        self.assertEqual(ArregloCiclo1().numeroElementos("1"), 1, "Calculo de Un elemento")

    def test_dos_numeros(self):
        self.assertEqual(ArregloCiclo1().numeroElementos("1,2"), 2, "Calculo de Dos elementos")

    def test_cualquier_numero(self):
        self.assertEqual(ArregloCiclo1().numeroElementos("1,2,5,7,4"), 5, "Calculo de varios elementos")