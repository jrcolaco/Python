from colorama import Fore, Style, init

init() 

from analise import (
    classificar_temperatura,
    classificar_chuva,
    calcular_total_precipitacao,
    calcular_amplitude_termica,
    arredondar_temperatura,
    obter_temperaturas_maximas,
    calcular_temperatura_media,
    classificar_amplitude,
    converter_celsius_para_fahrenheit,
    obter_dia_mais_quente,
    sugerir_atividade,
    classificar_dia,
    calcular_sensacao_termica_simples, 
    calcular_media_geral
)

# extra
def _colorir_temperatura(classificacao):
    if classificacao == "quente":
        return Fore.RED + classificacao + Style.RESET_ALL
    elif classificacao == "frio":
        return Fore.BLUE + classificacao + Style.RESET_ALL
    else:
        return classificacao


def mostrar_previsao_diaria(previsao):
    for dia in previsao["dias"]:
        temp_max_raw = dia["temp_max"]
        temp_min_raw = dia["temp_min"]

        classificacao_temp = classificar_temperatura(temp_max_raw)
        classificacao_temp = _colorir_temperatura(classificacao_temp)
        classificacao_chuva = classificar_chuva(dia["precipitacao"])
        
        amplitude = calcular_amplitude_termica(
            temp_max_raw,
            temp_min_raw
        )
        classificacao_amplitude = classificar_amplitude(amplitude)

        temp_max = arredondar_temperatura(temp_max_raw)
        temp_min = arredondar_temperatura(temp_min_raw)

        media = calcular_temperatura_media(
            temp_max_raw,
            temp_min_raw
        )

        sensacao = calcular_sensacao_termica_simples(
            temp_max_raw,
            vento=dia.get("vento", 0)
        )

        temp_max_f = converter_celsius_para_fahrenheit(temp_max_raw)
        tipo_dia = classificar_dia(dia)
        atividade = sugerir_atividade(
            temp_max=temp_max_raw,
            precipitacao=dia["precipitacao"]
        )

        print(
            f"{dia['data']} | "
            f"Máx: {temp_max}ºC ({temp_max_f}ºF) | "
            f"Mín: {temp_min}ºC | "
            f"Média: {media}ºC\n"
            f"Chuva: {dia['precipitacao']} mm | "
            f"{classificacao_temp} | "
            f"{classificacao_chuva}\n"
            f"Amplitude: {round(amplitude, 1)}ºC ({classificacao_amplitude}) | "
            f"Sensação: {sensacao}ºC\n"
            f"Dia: {tipo_dia} | "
            f"Atividade: {atividade}"
        )
        print("-" * 80)

def mostrar_resumo(previsao):
    total_chuva = calcular_total_precipitacao(previsao["dias"])
    temperaturas = obter_temperaturas_maximas(previsao["dias"])

    print("Resumo:")
    print(f"Total de precipitação: {total_chuva} mm")
    print(f"Temperaturas máximas: {temperaturas}")

# extra
def mostrar_estatisticas(previsao):
    dias = previsao["dias"]

    dia_quente = obter_dia_mais_quente(dias)
    media_geral = calcular_media_geral(dias)

    print("Estatísticas avançadas")
    print(f"Dia mais quente: {dia_quente['data']} ({dia_quente['temp_max']}ºC)")
    print(f"Temperatura média geral: {media_geral}ºC")
