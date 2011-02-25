while opcao != 5:
    print "Escolha a opcao desejada:"
    print "1 - Cadastrar produto"
    print "2 - Cadastrar Cliente"
    print "3 - Efetuar compra"
    print "4 - Efetuar troca"
    print "5 - Sair"
    opcao = input ()

    if opcao == 1:
       codprod = raw_input ("Informe codigo do produto: ")
       marca = raw_input ("Informe a marca do produto: ")
       modelo = raw_input ("Informe o modelo do produto: ")
       numserie = raw_input ("Informe o numero de serie do produto: ")
       produto(codprod, marca, modelo, numserie)

