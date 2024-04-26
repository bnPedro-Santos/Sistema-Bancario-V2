print('Bem-vindo Usuário!!!')

#Menu
def menu():

    menu= '''\n
    \/\/\/\/\/\/\/\/\/\/ MENU \/\/\/\/\/\/\/\/\/\/
    [1]\tSacar
    [2]\tDepositar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tNovo usuario
    [7]\tSair
    >> '''

#Estrutura BASE
def main():
     # Definindo os dados PADROES
    LIMITE_SAQUES= 3
    AGENCIA= '0001'

    saldo= 0
    limite= 500
    extrato= ''
    num_saques= 0
    numero_conta= 1
    usuarios= []
    contas= []
    
    while True:
        opcao= menu(1)
        # Metodo de SAQUE
        if opcao == '':
            valor= float(input("Digite o valor de SAQUE: "))

            saldo, extrato= sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                num_saques=num_saques,
                lim_saques=LIMITE_SAQUES,
            )
        
        # Metodo de DEPOSITO 
        elif opcao== '2':
            valor= float(input('Digite o valor de DEPOSITO: '))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        # Metodo de EXTRATO
        elif opcao== '3':
            exibir_extrato(saldo, extrato=extrato)
        
        # Metodo de NUMERO CONTAS
        elif opcao== '4':
            conta= criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
                numero_conta += 1

        # Metodo de USUARIOS
        elif opcao== "5":
            criar_usuario(usuarios)

        # Metodo SAIR
        elif opcao== '6':
            break
        
        #Erro de seleção
        else:
            print('Operação inválida, por favor selecione uma operação existente.')


# FUNÇÕES NESCESSARIAS PARA O PROJETO

#Deposito (positional only)
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\tR$ {valor:.2f}\n'
        print('\n\/\/\/ DEPÓSITO realizado com sucesso! \/\/\/')
    else:
        print('\n \/\/\/ OCORREU UM ERRO! O valor inserido é inválido. \/\/\/')

    return saldo, extrato    

#Saque (keyword only)
def sacar(*, saldo, valor, extrato, limite, num_saques, limite_saques):
    exedeu_saldo= valor > saldo
    exedeu_limite= valor > limite
    exedeu_saques= num_saques >= limite_saques

    if exedeu_saldo:
        print('\n\/\/\/ OCORREU UM ERRO! Não há saldo o suficiente. \/\/\/')
    
    elif exedeu_limite:
        print('\n\/\/\/ OCORREU UM ERRO! O valor para saque exede o limite. \/\/\/')
    
    elif exedeu_saques:
        print('\n\/\/\/ OCORREU UM ERRO! Número máximo de saques atingido. \/\/\/')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\tR$ {valor:.2f}\n'
        num_saques += 1
        print('\n\/\/\/ SAQUE realizado com sucesso! \/\/\/')
    else:
        print('\n \/\/\/ OCORREU UM ERRO! O valor inserido é inválido. \/\/\/')
    
    return saldo, extrato

#Extrato (positional only e keyword only)]
def exibir_extrato(saldo, /, *, extrato):
    print('\n\/\/\/\/\/\/\/\/\/\/ EXTRATO \/\/\/\/\/\/\/\/\/\/')
    print('Sem movimentações por aqui!' if not extrato else extrato)
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print('\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')

#Criar User
def criar_usuario(usuarios):
    cpf= input('Digite o CPF (apenas os números): ')
    usuario= filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\b\/\/\/ Já existe usuário com este CPF! \/\/\/')
        return
    
    nome= input('Nome completo: ')
    nascimento= input('Data de nascimento (dd-mm-aaaa: )')
    endereco= input('Endereço (Rua, nº - bairro - cidade/estado): ')

    usuarios.append({'nome':nome, 'nascimento': nascimento, 'cpf': cpf, 'endereco': endereco})
    print('\/\/\/ Usuário cadastrado com sucesso! \/\/\/')

#Filtro User
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados= [usuario for usuario in usuarios if usuario['cpf']== cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

#Criar Conta
def criar_conta(agencia, numero_conta, usuarios):
    cpf= input('CPF do usuário: ')
    usuario= filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n\/\/\/ Conta criada com sucesso" \/\/\/')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    print('\n\/\/\/ Usuário não encontrado, é nescessario um usuarios antes de criar conta! \/\/\/')

main()