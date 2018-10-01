class ArregloCiclo1:
    def numeroElementos(self, cadena):
        cadena2 = cadena.split(",")
        tamano = len(cadena2)
        if len(cadena) == 0:
            return 0
        else:
            return tamano