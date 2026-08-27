from assinantes import Assinante
from PlataformaStreaming import PlataformaStreaming


def menu_inicial():
    plataforma = PlataformaStreaming()

    while True:
        print(
            """
==== Sistema de Gerenciamento de Assinantes ====
===========================================
1 - Cadastrar Assinante
2 - Listar Assinantes
3 - Cancelar Assinatura
0 - Sair do Sistema
===========================================
"""
        )
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- Novo Cadastro ---")
            nome = input("Informe o nome: ")
            plano = input("Informe o plano: ")
            senha = input("Informe a senha: ")

            novo_assinante = Assinante(nome, plano, senha)
            plataforma.cadastrar_assinante(novo_assinante)

            print(
                f"\nAssinante '{nome}' cadastrado com sucesso! ID Gerado: {novo_assinante.id_conta}"
            )

        elif opcao == "2":
            plataforma.listar_assinantes()

        elif opcao == "3":
            print("\n--- Cancelamento de Assinatura ---")
            try:
                id_conta = int(
                    input("Informe o ID da conta a ser cancelada: ")
                )
                removido = plataforma.cancelar_assinatura(id_conta)
                if removido:
                    print(
                        f"Assinatura ID {id_conta} foi cancelada com sucesso."
                    )
                else:
                    print(
                        f"Nenhum assinante encontrado com o ID {id_conta}."
                    )
            except ValueError:
                print("Erro: O ID deve ser um número inteiro!")

        elif opcao == "0":
            print("\nEncerrando sistema...")
            break

        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    menu_inicial()