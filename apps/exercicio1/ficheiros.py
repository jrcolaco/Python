import json
from analise import sugerir_atividade
from datetime import datetime

def guardar_resultados(previsao, nome_ficheiro="resultado.json"):
    with open(nome_ficheiro, "w", encoding="utf-8") as f:
        json.dump(previsao, f, indent=4, ensure_ascii=False)

def exportar_previsao_completa(previsao):
    dados_export = []

    for dia in previsao["dias"]:
        dados_export.append({
            "data": dia["data"],
            "temp_max": dia["temp_max"],
            "temp_min": dia["temp_min"],
            "precipitacao": dia["precipitacao"],
            "atividade": sugerir_atividade(
                dia["temp_max"],
                dia["precipitacao"]
            )
        })

    resultado_final = {  # extra
        "gerado_em": datetime.now().isoformat(),  # extra
        "cidade": previsao["cidade"],  # extra
        "pais": previsao["pais"],  # extra
        "dias": dados_export
    }

    guardar_resultados(resultado_final, "resultado_detalhado.json")