from should_dsl import should, should_not
import unittest
import specloud
from produto import produto
from cliente import cliente
from venda import venda
from troca import troca

class TestProduto(unittest.TestCase):
 
    def setUp(self): #test_cadastrar_produto(self):
        self.produtoA = produto(1010, "HP", "Scanjet", 654321)
        self.produtoA.codprod |should| equal_to (1010)
        self.produtoA.marca |should| equal_to ("HP")
        self.produtoA.modelo |should| equal_to ("Scanjet")
        self.produtoA.numserie |should| equal_to (654321)
        produto.guardarprodutos(self.produtoA)
        self.produtoA.quantidade |should| equal_to (0)
        self.produtoA.addestoque (30)
        self.produtoA.quantidade |should| equal_to (30)
        self.produtoA.removeestoque (30)
        self.produtoA.quantidade |should| equal_to (0)
        self.produtoB = produto(3030, "Asus", "Netbook", 654333)
        self.produtoB.codprod |should| equal_to (3030)
        self.produtoB.marca |should| equal_to ("Asus")
        self.produtoB.modelo |should| equal_to ("Netbook")
        self.produtoB.numserie |should| equal_to (654333)
        produto.guardarprodutos(self.produtoB)
        self.produtoB.quantidade |should| equal_to (0)
        self.produtoB.addestoque (50)
        self.produtoB.quantidade |should| equal_to (50)
        self.produtoB.removeestoque (10)
        self.produtoB.quantidade |should| equal_to (40)
        self.produtoC = produto(4040, "Kingston", "DT3", 654444)
        self.produtoC.codprod |should| equal_to (4040)
        self.produtoC.marca |should| equal_to ("Kingston")
        self.produtoC.modelo |should| equal_to ("DT3")
        self.produtoC.numserie |should| equal_to (654444)
        produto.guardarprodutos(self.produtoC)
        self.produtoC.quantidade |should| equal_to (0)
        self.produtoC.addestoque (500)
        self.produtoC.quantidade |should| equal_to (500)
        self.produtoC.removeestoque (10)
        self.produtoC.quantidade |should| equal_to (490)


    def teste_relatorio_prod_disponiveis(self):
        produto.listadisponiveis |should| equal_to (["Netbook", "DT3"])#rever
        produto.listadisponiveis |should| equal_to (["Scanjet"])


class TestCliente(unittest.TestCase):
     def test_cadastrar_cliente(self):
        self.cliente = cliente(2020, "Maria do Socorro", "Rua das Marias")
        self.cliente.codcliente |should| equal_to (2020)
        self.cliente.nome |should| equal_to ("Maria do Socorro")
        self.cliente.end |should| equal_to ("Rua das Marias")

class TestVenda(unittest.TestCase):
     def test_inserir_venda(self):
        self.cli = cliente(2020, "Maria do Socorro", "Rua das Marias")
        self.venda = venda("20/10/2010", self.cli)
        self.venda.datavenda |should| equal_to ("20/10/2010")
        self.venda.cliente.codcliente |should| equal_to (2020)
        self.venda.cliente.nome |should| equal_to ("Maria do Socorro")
        self.venda.cliente.end |should| equal_to ("Rua das Marias")
        self.produto = produto(1010, "HP", "Scanjet", 654321)
        self.venda.adicionarProduto(self.produto)
        self.venda.produtos[0].codprod |should| equal_to (1010)
        self.venda.produtos[0].marca |should| equal_to ("HP")
        self.venda.produtos[0].modelo |should| equal_to ("Scanjet")
        self.venda.produtos[0].numserie |should| equal_to (654321)
        self.produtoB = produto(100, "Dell", "Notebook", 45881)
        self.venda.adicionarProduto(self.produtoB)
        self.venda.produtos[1].codprod |should| equal_to (100)
        self.venda.produtos[1].marca |should| equal_to ("Dell")
        self.venda.produtos[1].modelo |should| equal_to ("Notebook")
        self.venda.produtos[1].numserie |should| equal_to (45881)	   

class TestTroca(unittest.TestCase):
     def test_inserir_troca(self):
         self.troca = troca("cabeca de impressao quebrada", "25/10/2010")
         self.troca.defeito |should| equal_to ("cabeca de impressao quebrada")
         self.troca.datatroca |should| equal_to ("25/10/2010")

