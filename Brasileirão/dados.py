# Lista de times

times = ["Corinthians", "Santos", "São Paulo", "Palmeiras","Bragantino", "Fluninense",
          "Bahia", "Athletico-PR", "Chapecoense", "Mirassol", "Coritiba", "Flamengo", "Botafogo", "Grêmio",
          "EC Vitória", "Atlético-MG", "Remo", " Vasco da Gama", "Internacional", "Cruzeiro",]


def criar_tabela(times):
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
    return tabela