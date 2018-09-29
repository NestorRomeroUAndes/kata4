__author__ = 'johanna gutierres - nestor romero'

class Arreglo:
    def numeroElementos(self, cadena):
        cadena2 = cadena.split(",")
        tamano = len(cadena2)
        if len(cadena) == 0:
            return [0,0]
        else:
            return [tamano,1]