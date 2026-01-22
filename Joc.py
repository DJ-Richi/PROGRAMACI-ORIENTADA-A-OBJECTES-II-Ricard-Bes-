# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 22/01/2026
# Versió: 1
#
# Descripció: Classe Joc amb atribut privat __puntuacio.
# Especificacions d'Entrada: Inicialitza a 0 Afegeix mètodes per sumar punts i reiniciar la puntuació El getter retorna la puntuació

class Joc:
    def __init__(self):
        self.__puntuacio = 0

    @property
    def puntuacio(self):
        return self.__puntuacio

    def sumar_punts(self, punts):
        if punts > 0:
            self.__puntuacio += punts
        else:
            return ValueError("Els punts han de ser positius")

    def reiniciar(self):
        self.__puntuacio = 0

j = Joc()

print(j.puntuacio)

j.sumar_punts(10)
print(j.puntuacio)

j.reiniciar()
print(j.puntuacio)