# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 21/01/2026
# Versió: 1
#
# Descripció: Crea una calsse amb un atribut privat i amb metodes pubilcs per ingresar, retirar o veerue usuaris.
# Especificacions d'Entrada: No hi ha entrada d'usuari.

class complementari:
    def __init__(self, saldo):
        self.__saldo = saldo

    def consultar_saldo(self):
        return self.__saldo

    def ingresar(self, quantitat):
        self.__saldo = self.__saldo + quantitat

    def retirar_diners(self, quantitat):
        self.__saldo = self.__saldo - quantitat

complementari1 = complementari

complementari1.ingresar = (422)

complementari1.retirar_dinerS = (100)

print(complementari.consultar_saldo)

