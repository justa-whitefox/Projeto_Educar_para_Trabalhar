#UC1

clientes = []
n_clientes = 1

def menu() :
    option = int(input('''
[1] - Cadastrar cliente
[2] - Consultar Clientes
[3] - Editar Cliente
[4] - Sair do programa
'''))

    return option

def cadastra_cliente() :
    cliente_nome = input('Digite o nome do cliente: ')
    cliente_cep = input('Digite o cep do cliente: ')
    cliente_telefone = input('Digite o telefone do cliente: ')
    clientes_dados = (cliente_nome,cliente_cep,cliente_telefone)
    clientes.append(clientes_dados)
    print(clientes)
    print('Cliente adicionado')

def mostrar_cliente() :
    for cliente in clientes:
      print(f'''
      Nome: {cliente[0]}
      Cep: {cliente[1]}
      Telefone: {cliente[2]}''')


def programa() :

    while True:
        option = menu()

        if option == 1 :
            cadastra_cliente()
        if option == 2 :
            mostrar_cliente()
        if option == 4 :
          break

programa()