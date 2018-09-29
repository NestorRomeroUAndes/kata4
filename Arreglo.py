__author__ = 'johanna gutierres - nestor romero'

class Arreglo:
    def numeroElementos(self, cadena):
        cadena2 = cadena.split(",")
        tamano = len(cadena2)
        if len(cadena) == 0:
            return [0,0,0,0]
        else:
            minimo = int(min(cadena2))
            maximo = int(max(cadena2))
            suma = 0
            for elemento in cadena2:
                suma = suma + int(elemento)
            promedio = suma / tamano
            return [tamano,minimo,maximo,promedio]
