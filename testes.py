from should_dsl import should, should_not
import unittest
import specloud
from produto import produto
from cliente import cliente
from venda import venda
from troca import troca

class TestProduto(unittest.TestCase):
 
    def setUp(self): #test_cadastrar_produto(self):
        self.produtoA = produto(1010, "HP", "Scanjet", 654321, 0)
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
        self.produtoB = produto(3030, "Asus", "Netbook", 654333, 0)
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
        self.produtoC = produto(4040, "Kingston", "DT3", 654444, 0)
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
        p = produto.listadisponiveis() 
        p[0].codprod |should| equal_to (3030)
        p[0].marca |should| equal_to ("Asus")
        p[0].quantidade |should| equal_to (40)
        p[1].codprod |should| equal_to (4040)
        p[1].marca |should| equal_to ("Kingston")
        p[1].quantidade |should| equal_to (490)



class TestCliente(unittest.TestCase):
     def test_cadastrar_cliente(self):
        self.cliente = cliente(2020, "Maria do Socorro", "Rua das Marias")
        self.cliente.codcliente |should| equal_to (2020)
        self.cliente.nome |should| equal_to ("Maria do Socorro")
        self.cliente.end |should| equal_to ("Rua das Marias")

class TestVenda(unittest.TestCase):
     def test_inserir_venda(self):
        self.cli = cliente(2020, "Maria do Socorro", "Rua das Marias")
        self.venda = venda(1, "20/10/2010", self.cli)
        self.venda.datavenda |should| equal_to ("20/10/2010")
        self.venda.cliente.codcliente |should| equal_to (2020)
        self.venda.cliente.nome |should| equal_to ("Maria do Socorro")
        self.venda.cliente.end |should| equal_to ("Rua das Marias")
        self.produtoA = produto(1010, "HP", "Scanjet", 654321, 5)
        self.venda.adicionarProduto(self.produtoA)
        self.venda.produtos[0].codprod |should| equal_to (1010)
        self.venda.produtos[0].marca |should| equal_to ("HP")
        self.venda.produtos[0].modelo |should| equal_to ("Scanjet")
        self.venda.produtos[0].numserie |should| equal_to (654321)
        self.produtoB = produto(100, "Dell", "Notebook", 45881, 10)
        self.venda.adicionarProduto(self.produtoB)
        self.venda.produtos[1].codprod |should| equal_to (100)
        self.venda.produtos[1].marca |should| equal_to ("Dell")
        self.venda.produtos[1].modelo |should| equal_to ("Notebook")
        self.venda.produtos[1].numserie |should| equal_to (45881)	   

class TestTroca(unittest.TestCase):
    def setUp(self):
        self.cli = cliente(2020, "Maria do Socorro", "Rua das Marias")
        self.vendaA = venda(1, "20/10/2010", self.cli)
        self.vendaA.datavenda |should| equal_to ("20/10/2010")
        self.vendaA.cliente.codcliente |should| equal_to (2020)
        self.vendaA.cliente.nome |should| equal_to ("Maria do Socorro")
        self.vendaA.cliente.end |should| equal_to ("Rua das Marias")
        self.produtoA = produto(1010, "HP", "Scanjet", 654321, 5)
        self.vendaA.adicionarProduto(self.produtoA)
        self.vendaA.produtos[0].codprod |should| equal_to (1010)
        self.vendaA.produtos[0].marca |should| equal_to ("HP")
        self.vendaA.produtos[0].modelo |should| equal_to ("Scanjet")
        self.vendaA.produtos[0].numserie |should| equal_to (654321)
        self.produtoB = produto(100, "Dell", "Notebook", 45881, 10)
        self.vendaA.adicionarProduto(self.produtoB)
        self.vendaA.produtos[1].codprod |should| equal_to (100)
        self.vendaA.produtos[1].marca |should| equal_to ("Dell")
        self.vendaA.produtos[1].modelo |should| equal_to ("Notebook")
        self.vendaA.produtos[1].numserie |should| equal_to (45881)	
    
    def test_garantia(self):    
        # testar garantia
        self.vendaB = venda(1, "20/10/2009", self.cli)
        self.vendaB.datavenda |should| equal_to ("20/10/2009")
        self.vendaB.haGarantia() |should| equal_to (False)
        self.vendaB = venda(1, "01/04/2010", self.cli)
        self.vendaB.haGarantia() |should| equal_to (True)
    
    def test_inserir_troca(self):
        
         self.trocaA = troca("cabeca de impressao quebrada", "25/10/2010", self.vendaA, 1010)
         self.trocaA.defeito |should| equal_to ("cabeca de impressao quebrada")
         self.trocaA.datatroca |should| equal_to ("25/10/2010")
         self.trocaA.codprod |should| equal_to (1010)
         self.trocaA.mostrarquemtrocou() |should| equal_to ("Maria do Socorro")
         self.trocaB = troca(" nao liga", "25/01/2011", self.vendaA, 100)
         self.trocaB.defeito |should| equal_to (" nao liga")
         self.trocaB.datatroca |should| equal_to ("25/01/2011")
         self.trocaB.codprod |should| equal_to (100)
         self.trocaB.mostrarquemtrocou() |should| equal_to ("Maria do Socorro")
         pd=troca.mostrarprodutosdefeituosos()
         pd[0].codprod  |should| equal_to (1010) 
         pd[1].codprod  |should| equal_to (100) 
            
         
