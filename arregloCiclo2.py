class ArregloCiclo2:
    def numeroElementos(self, cadena):
        cadena2 = cadena.split(",")
        tamano = len(cadena2)
        if len(cadena) == 0:
            return [0, 0]
        else:
            minimo = int(min(cadena2))
            return [tamano, minimo]