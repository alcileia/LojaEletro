from datetime import date
class venda:
  todasVendas = []
  def __init__(self, codvenda, datavenda, cliente):
    self.codVenda = codvenda
    self.datavenda = datavenda
    self.cliente = cliente
    self.produtos = []

  def adicionarProduto(self, produto):
    self.produtos.append(produto)

  @staticmethod
  def guardarvenda(self):
    venda.todasVendas.append(self)

  @staticmethod
  def buscarVenda(self, codVenda):
    for i in range (0, len(venda.todasVendas)):
      if venda.todasVendas[i].codVenda == codVenda:
        return venda.todasVendas[i]
  
  def haGarantia(self):
    data = date.today()
    datav = date(int(self.datavenda[6:10]), int(self.datavenda[3:5]), int(self.datavenda[0:2]))
    ano = datav.year+1
    dataGarantia= date(ano, datav.month, datav.day)       
    if data <= dataGarantia:
      return True
    else: 
      return False
