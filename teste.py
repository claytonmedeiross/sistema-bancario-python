
def sacar(saldo):
    valor = float(input("Digite o valor para saque: "))

    if valor <= 0:
        print("Valor inválido para saque")
        return saldo

    if valor > saldo:
        print("Saldo insuficiente")
        return saldo

    saldo = saldo - valor
    print(f"Saque realizado. Saldo atual: {saldo:.2f}")
    return saldo



def depositar(saldo):
    valor = float(input("Digite o valor de deposito"))
    if valor<= 0:
        print(f"Valor inválido para depósito")
        return saldo
    
    saldo = saldo + valor
    print(f"Saldo Atualizado:{saldo:.2f}")
    return saldo



def sistema():
    saldo = 100

    while True:
        print("\n1 - Sacar")
        print("2 - Ver saldo")
        print("3 - Sair")
        print("4 - Depositar")

        opcao = input("Escolha: ")

        if opcao == "1":
            saldo = sacar(saldo)

        elif opcao == "2":
            print(f"Saldo atual: {saldo:.2f}")

        elif opcao == "4":
            saldo = depositar(saldo)

        elif opcao == "3":
            print("Saindo...")
            break

        else:
            print("Opção inválida")


sistema()