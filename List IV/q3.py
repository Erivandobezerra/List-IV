class Item:
    def __init__(self, valor):
        self.valor = valor 
        self.proximo = None

class Fila:
    def __init__(self):
        self.inicio = None 
        self.fim = None
         self.tamanho = 0 
    
    def vazia(self):
        return self.inicio is None
    
    def tam(self):
        return self.tamanho 
    
    def enfileirar(self, valor):
        novo_item = Item(valor)
        if self.vazia():
            self.inicio = novo_item
            self.fim = novo_item
        else:
            self.fim.proximo = novo_item
            self.fim = novo_item 
        self.tamanho += 1 
        
    def desenfileirar(self):
        if self.vazia():
            raise IndexError('A fila está vazia!')
        valor = self.inicio.valor
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self.tamanho -=1
        return valor
        
def sequencia():
    f = Fila()

    while True:
        num = int(input('Informe o número para adicionar a fila: '))
        if num < 0:
            break
        f.enfileirar(num)
    print('Os números foram adicionados a fila!\n')
        
    print('Ordem que os elementos foram inseridos: ')
    while not f.vazia():
        removidos = f.desenfileirar()
        print(removidos)

sequencia()    