import unittest

class produto(unittest.TestCase):
    def __init__(self, codprod, marca, modelo, numserie):
        self.produto = produto(1010, "HP", "Scanjet", 56789123)
        self.produto.codprod |should| equal_to (1010)
        self.produto.marca |should| equal_to ("HP")
        self.produto.modelo |should| equal_to ("Scanjet")
        self.produto.numserie |should| equal_to (56789123)

class cliente(unittest.TestCase):
    def __init__(self, codcliente, nome, end):
        self.cliente = cliente(2020, "Maria do Socorro", "Rua das Palmeiras")
        self.cliente.codcliente |should| equal_to (2020)
        self.cliente.nome |should| equal_to ("Maria do Socorro")
        self.cliente.end |should| equal_to ("Rua das Palmeiras")

unittest.main()
