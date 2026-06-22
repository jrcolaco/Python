import math

def sugerir_atividade(temp_max: float, precipitacao: float) -> str:
    """
    Sugere uma atividade com base nas condições meteorológicas.

    Args:
        temp_max (float): Temperatura máxima do dia.
        precipitacao (float): Precipitação prevista em mm.

    Returns:
        str: Sugestão de atividade.
    """

    if temp_max > 25 and precipitacao == 0:
        return "Ir à praia ou fazer caminhada"
    elif precipitacao > 5:
        return "Ficar em casa ou ver um filme"
    else:
        return "Passeio leve ao ar livre"

def classificar_temperatura(temp_max: float) -> str:
    """
    Classifica a temperatura com base no valor máximo.

    Args:
        temp_max (float): Temperatura máxima em graus Celsius.

    Returns:
        str: Categoria da temperatura ("frio", "ameno", "quente").
    """

    if temp_max < 20:
        return "frio"
    elif temp_max < 30:
        return "ameno"
    else:
        return "quente"

def classificar_chuva(precipitacao):
    if precipitacao == 0:
        return "sem chuva"
    elif precipitacao < 5:
        return "chuva fraca"
    else:
        return "chuva intensa"


def calcular_total_precipitacao(dias):
    return sum(dia["precipitacao"] for dia in dias)


def calcular_amplitude_termica(temp_max, temp_min):
    return temp_max - temp_min


def arredondar_temperatura(temperatura, casas_decimais=1):
    return round(temperatura, casas_decimais)


def calcular_sensacao_termica_simples(temperatura, vento=0):
    sensacao = temperatura - (vento * 0.2)
    return math.ceil(sensacao)


def obter_temperaturas_maximas(dias):
    return [dia["temp_max"] for dia in dias]


def calcular_temperatura_media(temp_max, temp_min, casas_decimais=1):
    media = (temp_max + temp_min) / 2
    return round(media, casas_decimais)


def classificar_amplitude(amplitude):
    if amplitude < 5:
        return "baixa"
    elif 5 <= amplitude <= 10:
        return "moderada"
    else:
        return "elevada"


def converter_celsius_para_fahrenheit(temperatura, casas_decimais=1):
    fahrenheit = (temperatura * 9 / 5) + 32
    return round(fahrenheit, casas_decimais)

# extra
def classificar_dia(dia):
    if dia["temp_max"] > 25 and dia["precipitacao"] == 0:
        return "bom"
    elif dia["precipitacao"] > 5:
        return "mau"
    else:
        return "normal"

# extra
def obter_dia_mais_quente(dias):
    return max(dias, key=lambda d: d["temp_max"])

# extra
def calcular_media_geral(dias):
    medias = [(d["temp_max"] + d["temp_min"]) / 2 for d in dias]
    return round(sum(medias) / len(medias), 1)