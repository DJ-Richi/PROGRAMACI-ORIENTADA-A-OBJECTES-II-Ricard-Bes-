# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 22/01/2026
# Versió: 1
#
# Descripció: Classe Usuari amb atribut privat __contrasenya.
# Especificacions d'Entrada: mètode canviar_contrasenya() (amb validació: mínim 8 caràcters) mètode verificar_contrasenya(clau)

class Usuari:
    def __init__(self, contrasenya):
        self.__contrasenya = contrasenya

    def canviar_contrasenya(self, nova):
        """Canvia la contrasenya si compleix la validació."""
        if len(nova) < 8:
            return ValueError("La contrasenya ha de tenir almenys 8 caràcters")
        self.__contrasenya = nova

    def verificar_contrasenya(self, clau):
        """Retorna True si la contrasenya coincideix."""
        return clau == self.__contrasenya


u = Usuari("contrasenya123")

print(u.verificar_contrasenya("password123"))
print(u.verificar_contrasenya("hola"))

u.canviar_contrasenya("contrasenya987")
print(u.verificar_contrasenya("contrasenya987"))
