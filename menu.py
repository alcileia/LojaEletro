from datetime import date
import io
from produto import produto
from cliente import cliente
from venda import venda
from troca import troca

opcao = ""
opc =  ""

while opcao != "7" :
    print ("Escolha a opcao desejada")
    print ("1 - Cadastrar produto")
    print ("2 - Incluir produto no estoque")
    print ("3 - Cadastrar Cliente")
    print ("4 - Efetuar compra")
    print ("5 - Efetuar troca")
    print ("6 - Listar produtos disponiveis ")
    print ('7 - Sair')
    opcao = raw_input()
    #print(opcao)
    if opcao == "1":
        print("Cadastro de Produto")
        codprod = input("Informe codigo do produto: ")
        marca = raw_input("Informe a marca do produto: ")
        modelo = raw_input("Informe o modelo do produto: ")
        numserie = raw_input("Informe o numero de serie do produto: ")
        produto.guardarprodutos(produto(codprod, marca, modelo, numserie, 0))

    elif opcao == "2":
        print("Incluir produto no estoque")
        codprod = input("Informe codigo do produto: ")
        p = produto.buscarProduto(codprod)
        if p!= None:
            qtd = input("Informe a quantidade do produto: ")
            p.addestoque(qtd)
        else:
            print("produto nao encontrado")

    elif opcao == "3":   
        codCli = input ("Informe codigo do cliente: ")
        nome = raw_input ("Informe o nome: ")   
        end = raw_input ("Informe o endereco: ")
        cliente.guardarclientes(cliente(codCli, nome, end))
        
    elif opcao == "4":
        codVenda = input ("Informe codigo da venda: ")
        codCli = input ("Informe codigo do cliente: ")
        clienteA = cliente.buscarCliente
        data = date.today()
        v= venda(codVenda, data, clienteA)
        while opc != "n":
            print("Incluir produto na venda")
            codprod = input("Digite o codigo do produto")
            p = produto.buscarProduto(codprod)
            if p!= None:
                qtd = input("Informe a quantidade do produto: ")
                p.removeestoque(int(qtd))
                v.adicionarProduto(p)
            else:
                print("produto nao encontrado")
            opc = raw_input("Incluir mais produtos: s para sim ou n para nao")

        venda.guardarvenda(v)
        
    elif opcao == '5':
        codVenda = input ("Informe codigo do venda: ")
        venda = venda.buscarVenda(codVenda)
        if venda.haGarantia:
            codProd = input ("Informe codigo do produto: ")
            defeito = raw_input ("Informe o defeito: ")  
            troca(defeito, data, venda, codProd)
            troca.adicionarTroca(troca)
            
    elif opcao == '6':
        lista = produto.listadisponiveis()
        for i in range (0, len(lista)):
            print (lista[i].marca+"-"+str(lista[i].quantidade))
