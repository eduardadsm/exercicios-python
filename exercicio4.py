def cadastrar_funcionario(id):
    print(f"ID do funcionario: {id}")
    # Criando o dicionário com as informações do funcionário
    funcionario = {}
    nome = input("digite o nome do funcionário:  ")
    setor = input("digite o setor do funcionário:  ")
    salario =  input("digite o salario do funcionário:  ")

    funcionario['id'] = id
    funcionario['nome'] = nome
    funcionario['setor'] = setor
    funcionario['salario'] = salario
    #adicionando funcionario na lista
    lista_funcionarios.append(funcionario.copy())

def consultar_funcionarios():
    while True:
        print('-------------------------------------------')
        print('----------MENU CONSULTAR FUNCIONÁRIO---------')
        print('Escolha a opção desejada:')
        print('1 - Consultar todos os Funcionarios') 
        print('2 - Consultar Funcionarios por id') 
        print('3 - Consultar Funcionário(s) por setor') 
        print('4 - retonar') 
        opcaoConsulta= int(input(">>"))
        if (opcaoConsulta == 4 ):
            return
        
        elif (opcaoConsulta == 1 ):
            for funcionario in lista_funcionarios:
                print(funcionario)

        elif (opcaoConsulta == 2 ):
            id_desejado =  int(input("digite o id desejado do funcionário:  "))
            for funcionario in lista_funcionarios:
                if funcionario['id'] == id_desejado:
                    print(funcionario)
                    break

        elif (opcaoConsulta == 3 ):
            setor_desejado =  input("digite o setor desejado do funcionário:  ")
            for funcionario in lista_funcionarios:
                if funcionario['setor'] == setor_desejado:
                    print(funcionario)
        else:
            print("opcao invalida")


def remover_funcionario():
    while True:
        id_remocao =  int(input("digite o id do funcionário a ser removido:  "))
        for funcionario in lista_funcionarios:
            if funcionario['id'] == id_remocao:
                lista_funcionarios.remove(funcionario)
                return
        print("Id Invalido")
    
    
#programa principal
print('Bem vindo a Empresa da Eduarda Marcelino ^^')

id_global= 4915306
lista_funcionarios = []

while True:
    print('-------------------------------------------')
    print('--------------MENU PRINCIPAL---------------')
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Funcionarios') 
    print('2 - Consultar Funcionarios') 
    print('3 - Remover Funcionário') 
    print('4 - Sair') 
    opcaoDesejada = int(input(" >> "))
    if (opcaoDesejada == 4):
        break

    elif ( opcaoDesejada == 1):
        cadastrar_funcionario(id_global)
        id_global = id_global + 1

    elif ( opcaoDesejada == 2):
        consultar_funcionarios()

    elif (opcaoDesejada == 3):
        remover_funcionario()

    else:
        print("opção invalida")