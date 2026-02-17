import random # Bibilioteca para gerar números aleatórios de gols

# Versão inicial.
# Conceitos: Dicionário, Lista, Loop duplo, random, sorted(), lambda

# Lista de times.
times = ["Corinthians", "Santos", "São Paulo", "Palmeiras"]

# Criação da tabela

tabela = {}

for time in times:
    tabela[time] = {
        "pontos": 0,
        "vitorias": 0,
        "empates": 0,
        "derrotas": 0,
        "gols_pro": 0,
        "gols_contra": 0
    }

# Simulando os jogos.
# Dois loops, 1 para o primeiro time(for i in range(len(times))).
# Para o segundo time (for j in range(i + 1, len(times))).
for i in range(len(times)):
    for j in range(i + 1, len(times)):

        time1 = times[i]
        time2 = times[j]

        # Quantidade aleatória de gols, de 0 a 7.
        gols1 = random.randint(0, 7)
        gols2 = random.randint(0, 7)

        print(f"{time1} {gols1} x {gols2} {time2}")

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

# Ordena a tabela por pontos e saldo
# sorted() organiza a tabela
# lambda para como ordenar: 1º critério - pontos
# 2º critério - saldo de gols = item[1]["gols_pro"] - item[1]["gols_contra"]
classificacao = sorted(
    tabela.items(),
    key=lambda item: (item[1]["pontos"],
                      item[1]["gols_pro"] - item [1]["gols_contra"]),
    reverse=True
)

print("\n🏆 Classificação final\n")

for pos, (time, dados) in enumerate(classificacao, start=1):
    saldo = dados["gols_pro"] - dados["gols_contra"]
    print(f"{pos}º) {time} - {dados['pontos']} pts | SG: {saldo}")