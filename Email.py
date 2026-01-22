# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 22/01/2026
# Versió: 1
#
# Descripció: Classe CompteUsuari amb atribut privat __email
# Especificacions d'Entrada: El setter valida que l’email contingui “@” i “.” El getter retorna l’email actual

class CompteUsuari:
    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        if "@" in valor and "." in valor:
            self.__email = valor
        else:
            return ValueError("L'email ha de contenir '@' i '.'")


u = CompteUsuari("usuari@example.com")
print(u.email)

u.email = "nou@mail.com"
print(u.email)

u.email = "incorrecte"