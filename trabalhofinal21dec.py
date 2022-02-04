class Bank:
  nome= ''
  sobrenome=''
  cpf=0
  numero_de_cartao=0
  senha=0
  Limite_de_credito=0
  compra=''
  movimento=''



lista=[]
import re
def isCpfValid(cpf):

    if not isinstance(cpf,str):
        return False

    cpf = re.sub("[^0-9]",'',cpf)

    for i in range(1, 10):
        if cpf == str(i)*11:
            return False

    if len(cpf) != 11:
        return False

    sum = 0
    weight = 10

    """ Calculating the first cpf check digit. """
    for n in range(9):
        sum = sum + int(cpf[n]) * weight

        weight = weight - 1

    verifyingDigit = 11 -  sum % 11

    if verifyingDigit > 9 :
        firstVerifyingDigit = 0
    else:
        firstVerifyingDigit = verifyingDigit

    sum = 0
    weight = 11
    for n in range(10):
        sum = sum + int(cpf[n]) * weight

        weight = weight - 1

    verifyingDigit = 11 -  sum % 11

    if verifyingDigit > 9 :
        secondVerifyingDigit = 0
    else:
        secondVerifyingDigit = verifyingDigit

    if cpf[-2:] == "%s%s" % (firstVerifyingDigit,secondVerifyingDigit):
        return True
    return False









#funcao para inserir novo cliente no sistema
def insere(lista):

  print('Insere o cliente!')
  print('________________________________')
  print()
  ban=Bank()
  ban.nome=input('Nome do cliente: ')
  ban.sobrenome=input('Sobrenome do cliente: ')
  ban.cpf=input('cpf do cliente (Com os pontos(.) ): ')
  if isCpfValid(ban.cpf) == False:
    print()
    print('Invalid cpf')
    print("Por favor recomece o cadastro")
    return
  ban.Limite_de_credito=int(input('limite de credito: '))
  if ban.Limite_de_credito>999999:
    print('error o limite de credito nao pode ser maior que 999999')
    print()
    return insere(lista)
  ban.numero_de_cartao=int(input('O numero da cartao: '))
  ban.senha=int(input('digite a senha: '))
  if ban.senha>1000000:
    print('senha incorreta ')
    print()
    return
    print()
  ban.compra
  lista.append(ban)
  print()
  print('um cliente foi adicionado com sucesso! ')
  print()




#funcao para exclui clientes
def exclui(lista):
    cpf=input('digite o cpf do cliente para excluir:')
    for i in range(len(lista)):
      if cpf==lista[i].cpf:
        lista.remove(lista[i])
        print()
        print('cliente excluido com sucesso')
        print('_____________________________')
        print()



#funcao para de credito
def movimento(movi):


    print('='*30)
    print()
    print('1- farmacia')
    print('2- supermercado')
    print('3- restaurante')
    print('4- shopping')
    print('='*30)
    print()
    categoria=int(input('digite a categoria de compra: '))
    print()
    if categoria>4:
      print('        opcao invalida')
      return
      print('__________________________')
    farmacia=['farmacia= ']
    supermercado=['supermercado= ']
    restaurante=['restaurante= ']
    shopping=['shopping= ']

    quantas=int(input('quantas compra voce quer fazer nessa categoria: '))
    compratotal=0
    print()
    for i in range(quantas):
      compra=int(input('Digite o valor da compra voce deseja fazer: '))
      compratotal+=compra
      print()
      print()
      if categoria==1:
        farmacia.append(compra)
      if categoria==2:
        supermercado.append(compra)
      if categoria==3:
        restaurante.append(compra)
      if categoria==4:
        shopping.append(compra)




    for i in range(len(lista)):
      if compratotal>lista[i].Limite_de_credito:
        print('Opa! voce nao tem limite de credito suficiente para realizar essa operacao de credito porque voce comprou por',compratotal,'e seu limite de credito e de',lista[i] .Limite_de_credito,'!')
        print()
        print('voce precisa de ',compratotal-lista[i].Limite_de_credito,'para fazer essa transacao',)
        print()
        print('digite o valor exato para fazer um pagamento ')

        entrada4=int(input(''))
        pag=entrada+lista[i].Limite_de_credito
        saldo=pag-compratotal
        print('compra realizada com sucesso')
        print('________________________')

      else:
          print('operacao de credito realiza com sucesso! e seu saldo e: ',lista[i].Limite_de_credito-compratotal)
          print('historico de compra: ')
          print()




def usuario(lis):
  CPF=input('por favaor digite seu CPF: ')
  print()
  while len(lista)==0:
    print('cpf nao encontrado por favor insere um cliente no sistema')
    return insere(lista)

  for i in range(len(lista)):

    if lista[i].cpf==CPF:
      print()
    else:
      print('cpf nao esta cadastrado! vamos tentar de novo')
      return usuario(lista)
      print('_______________________________')

    senha=int(input('digite sua senha :'))
    if senha!=lista[i].senha:
      print(' senha invalido ')
      print('______________________________')
      return usuario(lista)
    else:
      print('______________________________')
      print()
      print('seja bem vindo',lista[i].nome)




entra=1
while entra!=0:
  print('seja bem vindo no sistema de ccbank')
  print()
  print(' 1-digite 1 para usuario root')
  print(' 2-digite 2 para usuario simple')
  print(' 3-sair')
  print()
  entra=int(input(' digite a opcao desejada:  '))
  print()
  if entra==1:
    print()
    print('----------------')
    print()
    print('1- para inserir cliente ')
    print('2- exclui cliente')
    print('3- sair ')
    print()

    entrada=int(input(''))
    if entrada>3:
      print('     opcao  invalida')
      print()
      print('----------------')
    if entrada==1:
      insere(lista)
      print()

    if entrada==2:
      exclui(lista)

      print()
    if entrada==3:
      print()
      print()
  if entra==2:
    usuario(lista)
    print()
    print('digite 1 para movimento')
    entrada2=int(input(''))
    if entrada2==1:
      movimento(lista)
      print()
      print()
  if entra>3:
    print('       opcao invalida')
    print()
    print('----------------')
