class produto:
    todosProdutos = []
    def __init__(self):
        self.codprod = 0
        self.marca = ""
        self.modelo = ""
        self.numserie = 0
        self.quantidade = 0

    def __init__(self, codprod, marca, modelo, numserie):
        self.codprod = codprod
        self.marca = marca
        self.modelo = modelo
        self.numserie = numserie
        self.quantidade = 0
    
    @staticmethod
    def guardarprodutos(self):
        produto.todosProdutos.append(produto)
        
    def addestoque (self, qtd):
        self.quantidade += qtd

    def removeestoque (self, qtd):
        self.quantidade -= qtd

    @staticmethod
    def listadisponiveis(self):
        self.todosDisponiveis = []
        for i in range (0, len(todosProdutos)):
            if produto.todosProdutos[i].quantidade > 0:
                self.todosDisponiveis.append(todosProdutos [i].modelo)
        print self.todosDisponiveis
        return self.todosDisponiveis
