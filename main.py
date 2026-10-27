"""Menu de terminal do Sistema de Chamados."""

from chamados import PRIORIDADES_VALIDAS, STATUS_VALIDOS, GerenciadorChamados


def ler_opcao(mensagem, opcoes):
    while True:
        valor = input(f"{mensagem} {opcoes}: ").strip().lower()
        if valor in opcoes:
            return valor
        print("Opção inválida, tente novamente.")


def main():
    gerenciador = GerenciadorChamados()

    while True:
        print("\n=== Sistema de Chamados - Operações ===")
        print("1 - Abrir chamado")
        print("2 - Listar chamados")
        print("3 - Alterar status")
        print("0 - Sair")
        opcao = input("Escolha: ").strip()

        try:
            if opcao == "1":
                titulo = input("Título: ")
                solicitante = input("Solicitante: ")
                prioridade = ler_opcao("Prioridade", PRIORIDADES_VALIDAS)
                chamado = gerenciador.abrir(titulo, solicitante, prioridade)
                print(f"Chamado aberto: {chamado}")
            elif opcao == "2":
                chamados = gerenciador.listar()
                if not chamados:
                    print("Nenhum chamado cadastrado.")
                for chamado in chamados:
                    print(chamado)
            elif opcao == "3":
                id_chamado = int(input("Número do chamado: "))
                status = ler_opcao("Novo status", STATUS_VALIDOS)
                print(f"Atualizado: {gerenciador.alterar_status(id_chamado, status)}")
            elif opcao == "0":
                print("Até logo!")
                break
            else:
                print("Opção inválida.")
        except (ValueError, KeyError) as erro:
            print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
