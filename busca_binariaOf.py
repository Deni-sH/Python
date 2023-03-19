class Buscador:
    def busca_sequencial(self, lista, x):
        for i in range(len(lista)):
            if lista[i] == x:
                return i
        return -1
    def busca_binaria(self, lista, x):
        primeiro = 0 #indice zero
        ultimo = len(lista) -1 #ultimo
        
        while primeiro <= ultimo:
            meio = (primeiro + ultimo) //2
            if lista[meio] == x:
                return meio
            else:
                if x < lista[meio]: #se nao esta no meio, agora estamos fazendo a busca em meio -1, ou seja na primeira parte.
                    ultimo = meio -1
                else:
                    primeiro = meio +1 #não esta no meio nem no começo, agora estamos buscando acima do meio
        return False
    
lista = [-100, 0, 20, 30, 50, 100, 3000, 5000]
b = Buscador()
b.busca_binaria(lista, 0)
numerobinario = b.busca_binaria(lista, 100)
print(numerobinario)