import random
import time
class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)]
        return lista
        
    def compara (self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]
        
        o= ordenador.Ordenador()
        
        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print("Bolha demorou ", depois - antes)