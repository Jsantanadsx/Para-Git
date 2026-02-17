def atualizar_tabela(tabela, time1, time2, gols1, gols2):
    # Atualizador dos gols
    tabela[time1]["gols_pro"] += gols1
    tabela[time1]["gols_contra"] += gols2
    tabela[time2]["gols_pro"] += gols2
    tabela[time2]["gols_contra"] += gols1

    # Resultado time 1 vencendo
    if gols1 > gols2:
        tabela[time1]["pontos"] += 3
        tabela[time1]["vitorias"] += 1
        tabela[time2]["derrotas"] += 1
        
    # Resultado time 2 vencendo
    elif gols2 > gols1:
        tabela[time2]["pontos"] += 3
        tabela[time2]["vitorias"] += 1
        tabela[time1]["derrotas"] += 1

    # Resultado empate
    else:
        tabela[time1]["pontos"] += 1
        tabela[time2]["pontos"] += 1
        tabela[time1]["empates"] += 1
        tabela[time2]["empates"] += 1
        
def classificar(tabela):
    # Ordena a tabela por pontos e saldo
    # sorted() organiza a tabela
    # lambda para como ordenar: 1º critério - pontos
    # 2º critério - saldo de gols = item[1]["gols_pro"] - item[1]["gols_contra"]
    classificacao = sorted(
        tabela.items(),
        key=lambda item: 
            (item[1]["pontos"],
            item[1]["gols_pro"] - item [1]["gols_contra"]
    ),
    reverse=True
)
    return classificacao
