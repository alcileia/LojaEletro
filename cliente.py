class cliente:
    clientes = []
    def __init__(self, codcliente, nome, end):
        self.codcliente = codcliente
        self.nome = nome
        self.end = end

    @staticmethod
    def guardarclientes(self):
         cliente.clientes.append(self)
         
    @staticmethod
    def buscarCliente(self, codCliente):
        for i in range (0, len(cliente.clientes)):
            if cliente.clientes[i].codcliente == codCliente:
                c = cliente(cliente.clientes[i].codcliente, cliente.clientes[i].nome, cliente.clientes[i].end)
                return c            
