from should_dsl import should, should_not
import unittest
import specloud
from produto import produto
from cliente import cliente
from venda import venda
from troca import troca


class TestProduto(unittest.TestCase):
    def test_cadastrar_produto(self):
        self.produto = produto(1010, "HP", "Scanjet", 654321)
        self.produto.codprod |should| equal_to (1010)
        self.produto.marca |should| equal_to ("HP")
        self.produto.modelo |should| equal_to ("Scanjet")
        self.produto.numserie |should| equal_to (654321)

class TestCliente(unittest.TestCase):
     def test_cadastrar_cliente(self):
        self.cliente = cliente(2020, "Maria do Socorro", "Rua das Marias")
        self.cliente.codcliente |should| equal_to (2020)
        self.cliente.nome |should| equal_to ("Maria do Socorro")
        self.cliente.end |should| equal_to ("Rua das Marias")

class TestVenda(unittest.TestCase):
     def test_inserir_venda(self):
        self.venda = venda("20/10/2010")
        self.venda.datavenda |should| equal_to ("20/10/2010")

class TestTroca(unittest.TestCase):
     def test_inserir_troca(self):
         self.troca = troca("cabeca de impressao quebrada", "25/10/2010")
         self.troca.defeito |should| equal_to ("cabeca de impressao quebrada")
         self.troca.datatroca |should| equal_to ("25/10/2010")
