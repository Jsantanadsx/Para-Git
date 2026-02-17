# Lista de times

times = ["Corinthians", "Santos", "São Paulo", "Palmeiras","Bragantino", "Portuguesa"]


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