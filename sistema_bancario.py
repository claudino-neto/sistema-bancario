numero_saldos = saldo = 0
limite_valor_por_saque = 500  # o limite de valor pra cada saque é de 500 reais
saques_realizados = 0  # o limite de saques é 3
LIMITE_SAQUES = 3
extrato = ""
menu = '''
    ====== Banco do Claudino ======
    Escolha uma das opções:
    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [u] - Criar usuário
    [c] - Criar conta corrente
    [q] - Sair

=> '''
dicionario_usuarios = dict()
dicionario_contas = dict()


def depositar(saldo, extrato, /):
    deposito = float(input('Digite o valor (em R$): '))

    while deposito < 0:
        print("Não é possível depositar valores negativos. Tente novamente.")
        deposito = float(input('Digite o valor (em R$): '))

    saldo += deposito
    extrato += f"Depósito: R${deposito:.2f} em sua conta.\n"

    return saldo, extrato


def sacar(*, saques_realizados, LIMITE_SAQUES, saldo, extrato):
    excedeu_saques = saques_realizados >= LIMITE_SAQUES

    if excedeu_saques:
        print("Você já realizou o número máximo de saques. Tente outra opção.")

    else:
        saque = float(input('Digite o valor (em R$): '))

        while saque > limite_valor_por_saque or saque > saldo or saque < 0:

            if saque > limite_valor_por_saque:
                print("Operação falhou! Você excedeu o limite por saque. Tente novamente.")

            elif saque > saldo:
                print("Operação falhou! Você não tem saldo o suficiente. Tente novamente.")
            else:
                print("Operação falhou! O valor digitado não é válido. Tente novamente.")

            saque = float(input('Digite o valor (em R$): '))

        saldo -= saque
        extrato += f"Saque: R${saque:.2f} em sua conta.\n"
        saques_realizados += 1

    return saldo, extrato, saques_realizados


def apresentar_extrato(saldo, /, *, extrato):
    print("EXTRATO".center(35, "="))
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("=" * 35)


def criar_usuario(dicio_usuarios):
    print(f'Seja bem-vindo ao Banco Claudino! Começaremos agora o seu cadastro!')

    cpf = int(input('Informe o seu CPF: '))

    if cpf in dicio_usuarios:
        print(f'O seu CPF já está cadastrado no nosso banco!')

    else:
        dicio_usuarios[cpf] = dict.fromkeys(["nome", "data de nascimento", "cpf", "endereco"])
        dicio_usuarios[cpf]["nome"] = input('Informe o seu nome: ')
        dicio_usuarios[cpf]["data de nascimento"] = input('Informe sua data de nascimento: ')
        dicio_usuarios[cpf]["cpf"] = cpf
        dicio_usuarios[cpf]["endereco"] = input('Informe o seu endereço: ')

    print(dicio_usuarios)
    return dicio_usuarios


def criar_conta_corrente(dicio_contas, dicio_usuarios):
    cpf = int(input('Informe o seu CPF: '))

    if cpf not in dicio_usuarios:
        print('Você ainda não realizou um cadastro em nosso sistema. Por favor, realize o cadastro.')

    else:

        if cpf not in dicio_contas:
            dicio_contas[cpf] = list()
            dicio_contas[cpf].append(dict.fromkeys(["usuario", "numero da conta", "agencia"]))
            dicio_contas[cpf][0]["usuario"] = dicio_usuarios[cpf]["nome"]
            dicio_contas[cpf][0]["numero da conta"] = 1
            dicio_contas[cpf][0]["agencia"] = '0001'

        else:
            dicio_contas[cpf].append(dict.fromkeys(["usuario", "numero da conta", "agencia"]))
            dicio_contas[cpf][-1]["usuario"] = dicio_usuarios[cpf]["nome"]
            dicio_contas[cpf][-1]["numero da conta"] = dicio_contas[cpf][-2]["numero da conta"] + 1
            dicio_contas[cpf][-1]["agencia"] = '0001'

    print(dicio_contas)
    return dicio_contas


opcao = ''  # escolha que o usuário irá fazer

while opcao != 'q':

    opcao = input(menu)

    if opcao == 'd':

        saldo, extrato = depositar(saldo, extrato)

    elif opcao == 's':

        saldo, extrato, saques_realizados = sacar(saques_realizados=saques_realizados, LIMITE_SAQUES=LIMITE_SAQUES,
                                                  extrato=extrato, saldo=saldo)

    elif opcao == 'e':

        apresentar_extrato(saldo, extrato=extrato)

    elif opcao == 'u':

        dicionario_usuarios = criar_usuario(dicionario_usuarios)

    elif opcao == 'c':
        dicionario_contas = criar_conta_corrente(dicionario_contas, dicionario_usuarios)

    elif opcao == 'q':
        print("Saindo do sistema...")

    else:
        print("Opção inválida. Tente novamente.")
