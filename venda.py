class venda:
    def __init__(self, datavenda, cliente):
        self.datavenda = datavenda
        self.cliente = cliente
        self.produtos = []

    def adicionarProduto(self, produto):
        self.produtos.append(produto)
        

