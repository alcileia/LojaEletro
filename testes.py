import unittest
import produto, cliente, venda, troca

class TesteProduto:
    def insercao(self):
        self.produto = produto.produto (1010, "HP", "Scanjet", 654321)
        assert self.produto.codprod != None
        assert self.produto.marca != None
        assert self.produto.modelo != None
        assert self.produto.numserie != None

class TesteCliente:
     def insercao(self):
        self.cliente = cliente.cliente (2020, "Maria do Socorro", "Rua das Marias")
        assert self.cliente.codcliente != None
        assert self.cliente.nome != None
        assert self.cliente.end != None

class TesteVenda:
     def insercao(self):
        self.venda = venda.venda ("20/10/2010")
        assert self.venda.datavenda != None

class TesteTroca:
     def insercao(self):
         self.troca = troca.troca ("cabeca de impressao quebrada", "25/10/2010")
         assert self.troca.defeito != None
         assert self.troca.datatroca != None
      
unittest.main()
