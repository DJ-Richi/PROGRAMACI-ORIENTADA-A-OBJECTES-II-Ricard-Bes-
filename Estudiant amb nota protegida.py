# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 21/01/2026
# Versió: 1
#
# Descripció: Crea una classe Estudiant amb un atribut protegit _nota. Afegeix mètodes per:
# Especificacions d'Entrada: llegir la nota i modificar la nota només si és entre 0 i 10

class estudiant:
    def __init__(self, nota):
        self._nota = nota
    
    def consultar_nota(self):
        return self._nota

    def modificar_pujar(self, quantitat):
        self._nota = self._nota + quantitat

    def modificar_baixar(self, quantitat):
        self._nota = self._nota - quantitat

estudiant1 = estudiant (5)


estudiant1.modificar_pujar = (1)
estudiant1.modificar_baixar = (5)

print(estudiant1.consultar_nota())
