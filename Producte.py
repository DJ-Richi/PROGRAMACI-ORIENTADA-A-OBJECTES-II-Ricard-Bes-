# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 22/01/2026
# Versió: 1
#
# Descripció: Classe Producte amb atributs
# Especificacions d'Entrada: nom (públic) __preu (privat) Mètodes per obtenir i modificar el preu (només si > 0)

class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.__preu = preu

    def obtenir_preu(self):
        return self.__preu

    def modificar_preu(self, nou_preu):
        if nou_preu > 0:
            self.__preu = nou_preu
        else:
            return ValueError("El preu ha de ser més gran que 0")

p = Producte("Ordinador", 899)

print(p.obtenir_preu())

p.modificar_preu(950)
print(p.obtenir_preu())

p.modificar_preu(-10)