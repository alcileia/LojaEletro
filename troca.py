class troca:
    trocas = []
    def __init__(self, defeito, datatroca, venda, codprod):
        self.defeito = defeito
        self.datatroca = datatroca
        self.venda = venda
        self.codprod = codprod
    
    def adicionarTroca(self):
        if self.venda.haGarantia:
            self.trocas.append(self)

    def mostrarquemtrocou(self):
        return self.venda.cliente.nome

    @staticmethod    
    def mostrarprodutosdefeituosos():
        return troca.trocas

