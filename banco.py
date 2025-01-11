saldo = 0.0
limite_saque = 500.0
saques_diarios_permitidos = 3
extrato = []
saques_realizados = 0 

def menu_usuario():

    print("=== Menu do Usuário ===")
    print(f"1. Depósito")
    print(f"2. Saque")
    print(f"3. Extrato")
    print(f"4. Sair")
    print(f"Saldo atual: R$ {saldo:.2f} | Saques restantes: {saques_diarios_permitidos - saques_realizados}")

def realizar_deposito(valor):

    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido. Tente novamente!")

def realizar_saque(valor):

    global saldo, extrato, saques_diarios_permitidos, saques_realizados

    if saques_realizados >= saques_diarios_permitidos:
        print("Você atingiu o número máximo de saques permitidos.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite_saque:
        print("Você excedeu o limite de saque diário.")
    elif valor <= 0:
        print("Valor de saque inválido.") 
    else: 
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        saques_realizados += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

def exibir_extrato():
    
    print("=== Extrato ===")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for item in extrato:
            print(item)
    print(f"Saldo atual: R$ {saldo:.2f}")


while True:
    menu_usuario()
    opcao = input("Digite a sua escolha: ")
    if opcao == "1":
        try: 
            valor = float(input("Informe o valor do depósito: "))
            realizar_deposito(valor)
        except ValueError:
            print("Valor inválido. Tente novamente!")
    elif opcao == "2":
        try:
            valor = float(input("Informe o valor do saque: "))
            realizar_saque(valor)
        except ValueError:
            print("Valor inválido. Tente novamente!")
    elif opcao == "3":
        exibir_extrato()
    elif opcao == "4":
        print("Obrigado por usar o sistema bancário. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente!")
