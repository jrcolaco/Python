import os
from dados_mock import previsao
from utilitarios import mostrar_previsao_diaria, mostrar_resumo, mostrar_estatisticas
from ficheiros import guardar_resultados, exportar_previsao_completa

def main():
    while True:
        os.system("cls")

        print("=== MeteoCLI by jrcolaco ===")
        print(f"\nPrevisão para {previsao['cidade']}, {previsao['pais']}")

        print("\nMenu")
        print("1 - Ver previsão diária")
        print("2 - Ver resumo")
        print("3 - Estatísticas avançadas")  # extra
        print("4 - Guardar resultado em JSON")  # extra
        print("5 - Exportar previsão detalhada")  # extra
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_previsao_diaria(previsao)

        elif opcao == "2":
            mostrar_resumo(previsao)

        elif opcao == "3":
            mostrar_estatisticas(previsao)

        elif opcao == "4":
            guardar_resultados(previsao)
            print("Dados guardados em resultado.json")

        elif opcao == "5":
            exportar_previsao_completa(previsao)
            print("Dados exportados para resultado_detalhado.json")

        elif opcao == "0":
            print("Programa terminado.")
            break

        else:
            print("Opção inválida.")

        input("\nPressiona Enter para continuar...")


if __name__ == "__main__":
    main()