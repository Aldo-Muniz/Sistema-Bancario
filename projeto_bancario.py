menu = '''
    Seja Bem-vindo ao Banco Aldo
Selecione abaixo a opção que deseja:
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> '''

saldo = 0
limite = 500
extrato = ''
quantidade_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == '1':
        valor = float(input('Informe qual o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor: .2f}\n'
            print('Valor Depositado!')

        else:
            print('Operação falhou! Tente novamente inserindo um valor válido.')

    elif opcao == '2':
        valor = float(input('Informe o valor que deseja sacar: '))

        ultrapassou_saldo = valor > saldo #Se o valor foi maior do que se tem no saldo
        ultrapassou_limite = valor > limite #Se o valor foi maior que 500
        ultrapassou_saque = quantidade_saques >= limite_saques #Se passou do limite permitido de saques (3)

        if ultrapassou_saldo:
            print('Operação falhou! Não possui saldo o suficiente!')

        elif ultrapassou_limite:
            print('Operação falhou! Valor do saque maior que limite permitido!')

        elif ultrapassou_saque:
            print('Operação Falhou! Você já realizou a quantidade de saques permitida!')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R${valor: .2f}\n'
            quantidade_saques += 1
            print('Saque Realizado!')
        else:
            print('Operação falhou! Tente novamente inserindo um valor válido.')

    elif opcao == '3':
        print('\n========== EXTRATO ==========')
        print('Não foi realizada nenhuma movimentação' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        final = '=' * 29
        print(final)

    elif opcao == '0':
        break

    else:
        print('Operação inválida, tente novamente selecionando a opção desejada!')

    