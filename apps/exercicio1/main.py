import os
from dados_mock import previsao
from utilitarios import mostrar_previsao_diaria, mostrar_resumo, mostrar_estatisticas

def main():
    while True:
        os.system("cls")

        print("=== MeteoCLI by jrcolaco ===")
        print(f"\nPrevisão para {previsao['cidade']}, {previsao['pais']}")

        print("\nMenu")
        print("1 - Ver previsão diária")
        print("2 - Ver resumo")
        print("3 - Estatísticas avançadas")  # extra
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_previsao_diaria(previsao)

        elif opcao == "2":
            mostrar_resumo(previsao)

        elif opcao == "3":
            mostrar_estatisticas(previsao)

        elif opcao == "0":
            print("Programa terminado.")
            break

        else:
            print("Opção inválida.")

        input("\nPressiona Enter para continuar...")


if __name__ == "__main__":
    main()