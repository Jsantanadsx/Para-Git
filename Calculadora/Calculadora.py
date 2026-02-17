resultado_atual = None

#Loop : Calculadora só é interrompida quando o usuário digitar "S".
while True:

    # Se a variável não possui valor, "Digite o número inicial."
    if resultado_atual is None:
        # Pede e converte o número inicial para float (decimal)
        resultado_atual = float(input("Digite o número inicial: "))

    # Operação desejada 
    # .upper() transforma a digitação em maiúscula (c para C, s para S) Padronizando.
    operacao = input(
        "Digite a operação (+, -, *, /), C para limpar, ou S para sair: "
    ).upper()

    # Se o usuário digitou C (clear)
    if operacao == "C":
        # Zera a memória
        resultado_atual = None
        print("Calculadora limpa.")
        # Retorna ao início do loop
        continue

    # Se o usuário digitou S (sair)
    if operacao == "S":
        print("Encerrando a calculadora...")
        # Encerra o loop
        break

    # Pede o próximo número para a operação
    num = float(input("Digite o próximo número: "))

    if operacao == "+":
        resultado_atual += num

    elif operacao == "-":
        resultado_atual -= num

    elif operacao == "*":
        resultado_atual *= num

    elif operacao == "/":
        # Verifica se não é divisão por zero
        if num != 0:
            resultado_atual /= num
        else:
            print("Erro: divisão por zero.")
            # Retorna sem atualizar o resultado
            continue
    
    # Caso digite algo inválido
    else:
        print("Operação inválida.")
        # Retorna ao loop
        continue
    
    # Resultado atualizado
    print("Resultado atual:", resultado_atual)
