# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 22/01/2026
# Versió: 1
#
# Descripció: Classe Rellotge amb atribut __hores. El setter només accepta valors entre 0 i 23.
# Especificacions d'Entrada: Afegeix mètode per mostrar les hores en format “HH:00”

class Rellotge:
    def __init__(self, hores=0):
        self.__hores = hores

    @property
    def hores(self):
        return self.__hores

    @hores.setter
    def hores(self, valor):
        if 0 <= valor <= 23:
            self.__hores = valor
        else:
            return ValueError("Les hores han d'estar entre 0 i 23")

    def mostrar(self):
        return f"{self.__hores:02d}:00"

r = Rellotge(7)
print(r.mostrar())

r.hores = 15
print(r.mostrar())

r.hores = 30