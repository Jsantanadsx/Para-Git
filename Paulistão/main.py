from dados import times, criar_tabela
from simulador import simular_gols
from tabela import atualizar_tabela, classificar


# Criação da tabela
tabela = criar_tabela(times)

# Simulando os jogos
for i in range(len(times)):
    for j in range(i + 1, len(times)):

        time1 = times[i]
        time2 = times[j]

        gols1, gols2 = simular_gols()

        print(f"{time1} {gols1} x {gols2} {time2}")

        atualizar_tabela(tabela, time1, time2, gols1, gols2)

# Classificação final
classificacao = classificar(tabela)

print("\n🏆 Classificação final\n")

for pos, (time, dados) in enumerate(classificacao, start=1):
    saldo = dados["gols_pro"] - dados["gols_contra"]
    print(f"{pos}º) {time} - {dados['pontos']} pts | SG: {saldo}")