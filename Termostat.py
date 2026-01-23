# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 22/01/2026
# Versió: 1
#
# Descripció: Crea una classe Estudiant amb un atribut protegit _nota. Afegeix mètodes per:
# Especificacions d'Entrada: llegir la nota i modificar la nota només si és entre 0 i 10

class Termostat:
    def __init__(self, temperatura):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura

    def temperatura(self, valor):
        if 10 <= valor <= 30:
            self.__temperatura = valor
        else:
            print("La temperatura ha d'estar entre 10 i 30 °C")


temp = Termostat(20)
print(temp)

temp = 28
print(temp)
