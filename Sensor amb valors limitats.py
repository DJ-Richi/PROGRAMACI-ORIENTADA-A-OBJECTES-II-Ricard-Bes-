# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 22/01/2026
# Versió: 1
#
# Descripció: Classe Sensor amb atribut privat __valor.
# Especificacions d'Entrada: només permet valors entre 0 i 100 el getter retorna el valor actual

class Sensor:
    def __init__(self, valor=0):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, nou_valor):
        if 0 <= nou_valor <= 100:
            self.__valor = nou_valor
        else:
            return ValueError("El valor ha d'estar entre 0 i 100")

s = Sensor()

s.valor = 75
print(s.valor)

s.valor = 101
print(s.valor)
