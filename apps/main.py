previsao = {
    "cidade": "Lisboa",
    "dias": [
        {"data": "2026-06-18", "temp_max": 32, "temp_min": 20, "precipitacao": 0},
        {"data": "2026-06-19", "temp_max": 28, "temp_min": 18, "precipitacao": 2},
        {"data": "2026-06-20", "temp_max": 22, "temp_min": 16, "precipitacao": 8},
        {"data": "2026-06-21", "temp_max": 35, "temp_min": 21, "precipitacao": 0}
    ]
}

temperaturas_maximas = [dia["temp_max"] for dia in previsao["dias"]]
dias_quentes = [dia for dia in previsao["dias"] if dia["temp_max"] >= 30]
dias_com_chuva = [dia for dia in previsao["dias"] if dia["precipitacao"] > 0]

print(f"Temperaturas máximas: {temperaturas_maximas}")
print(f"Número de dias quentes: {len(dias_quentes)}")
print(f"Número de dias com chuva: {len(dias_com_chuva)}")

datas_com_chuva = [dia["data"] for dia in previsao["dias"] if dia["precipitacao"] > 0]
print(f"Dias com chuva: {datas_com_chuva}")

datas_dias_frescos = [dia["data"] for dia in previsao["dias"] if dia["temp_max"] < 25]
print(f"Dias frescos (<25ºC): {datas_dias_frescos}")

print("\nDetalhe da previsão:")

for dia in previsao["dias"]:

    if dia["temp_max"] >= 30:
        classificacao_temp = "muito quente"
    elif dia["temp_max"] >= 20:
        classificacao_temp = "agradável"
    else:
        classificacao_temp = "fresco"

    if dia["precipitacao"] == 0:
        classificacao_chuva = "sem chuva"
    elif dia["precipitacao"] < 5:
        classificacao_chuva = "chuva fraca"
    else:
        classificacao_chuva = "chuva significativa"

    print(
        f"{dia['data']} | "
        f"Máx: {dia['temp_max']}ºC | "
        f"Mín: {dia['temp_min']}ºC | "
        f"Temp: {classificacao_temp} | "
        f"Chuva: {classificacao_chuva}"
    )