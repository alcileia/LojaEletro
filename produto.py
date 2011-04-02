import io
class produto:
    produtos = []
    codprod = ""
    marca = ""
    modelo = ""
    numserie = 0
    quantidade = 0
    def __init__(self):
        self.codprod = 0
        self.marca = ""
        self.modelo = ""
        self.numserie = 0
        self.quantidade = 0

    def __init__(self, codprod, marca, modelo, numserie, quantidade):
        self.codprod = codprod
        self.marca = marca
        self.modelo = modelo
        self.numserie = numserie
        self.quantidade = quantidade
    
    @staticmethod
    def guardarprodutos(self):
         produto.produtos.append(self)

    def remover(self):
        produto.produtos.remove(self)
    
    @staticmethod    
    def alteraproduto(self):
        for i in range (0, len(produto.produtos)):
            if produto.produtos[i].codprod == self.codprod:
                produto.produtos[i] = self
               
        
    def addestoque (self, qtd):
        self.quantidade += qtd
        produto.alteraproduto(self)

    def removeestoque (self, qtd):
        self.quantidade -= qtd
        produto.alteraproduto(self)

    @staticmethod
    def listadisponiveis():
        todosDisponiveis = []
        for i in range (0, len(produto.produtos)):
            if produto.produtos[i].quantidade > 0:
                p = produto(produto.produtos[i].codprod, produto.produtos[i].marca, produto.produtos[i].modelo, produto.produtos[i].numserie, produto.produtos[i].quantidade)
                todosDisponiveis.append(p)
        return todosDisponiveis

    @staticmethod
    def buscarProduto(codprod):
        for i in range (0, len(produto.produtos)):
            if produto.produtos[i].codprod == codprod:
                p = produto(produto.produtos[i].codprod, produto.produtos[i].marca, produto.produtos[i].modelo, produto.produtos[i].numserie, produto.produtos[i].quantidade)
                return p
