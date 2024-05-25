numero_saldos = saldo = 0
limite_valor_por_saque = 500 # o limite de valor pra cada saque é de 500 reais
saques_realizados = 0 # o limite de saques é 3
extrato = ""
menu = '''
    ====== Banco do Claudino ======
    Escolha uma das opções:
    [1] - Depositar
    [2] - Sacar
    [3] - Extrato
    [4] - Sair

=> '''
opcao = 0 # escolha que o usuário irá fazer
while opcao != 4:

    opcao = int(input(menu))

    if opcao == 1:
        valor = int(input('Digite o valor (em R$): '))
        while valor < 0:
            print("Não é possível depositar valores negativos. Tente novamente.")
            valor = int(input('Digite o valor (em R$): '))
        saldo += valor
        extrato += f'''Foi depositado o valor de R${valor} em sua conta.
Saldo atual: R${saldo}\n'''

    elif opcao == 2:

        if saques_realizados == 3:
            print("Você já realizou o número máximo de saques. Tente outra opção.")

        else:
            valor = int(input('Digite o valor (em R$): '))

            while valor > limite_valor_por_saque or valor > saldo or valor < 0:
                print("O valor digitado não é válido. Tente novamente.")
                valor = int(input('Digite o valor (em R$): '))
            saldo -= valor
            extrato += f'''Foi sacado o valor de R${valor} em sua conta.
Saldo atual: R${saldo}'''
            saques_realizados += 1

    elif opcao == 3:
        print("EXTRATO".center(15, "="))
        print(extrato)

    elif opcao == 4:
        print("Saindo do sistema...")

    else:
        print("Opção inválida. Tente novamente.")
