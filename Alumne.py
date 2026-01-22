# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 22/01/2026
# Versió: 1
#
# Descripció: Classe Alumne amb atribut privat __edat.
# Especificacions d'Entrada: El setter no accepta valors negatius. El getter retorna l’edat

class Alumne:
    def __init__(self, edat=0):
        self.__edat = edat

    @property
    def edat(self):
        return self.__edat

    @edat.setter
    def edat(self, valor):
        if valor < 0:
            return ValueError("L'edat no pot ser negativa")
        self.__edat = valor

a = Alumne(15)
print(a.edat)

a.edat = 18
print(a.edat)

a.edat = -3