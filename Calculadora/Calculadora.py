resultado_atual = None

while True:
    if resultado_atual is None:
        resultado_atual = float(input("Digite o número inicial: "))

    operacao = input(
        "Digite a operação (+, -, *, /), C para limpar, ou S para sair: "
    ).upper()

    if operacao == "C":
        resultado_atual = None
        print("Calculadora limpa.")
        continue

    if operacao == "S":
        print("Encerrando a calculadora...")
        break

    num = float(input("Digite o próximo número: "))

    if operacao == "+":
        resultado_atual += num

    elif operacao == "-":
        resultado_atual -= num

    elif operacao == "*":
        resultado_atual *= num

    elif operacao == "/":
        if num != 0:
            resultado_atual /= num
        else:
            print("Erro: divisão por zero.")
            continue

    else:
        print("Operação inválida.")
        continue

    print("Resultado atual:", resultado_atual)
