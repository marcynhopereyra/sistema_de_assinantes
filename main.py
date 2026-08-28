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
         plataforma.cadastrar_assinante()
        elif opcao == "2":
         plataforma.listar_assinantes()
        elif opcao == "3":
         plataforma.cancelar_assinatura()
        elif opcao == "0":
            print("\nEncerrando sistema...")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    menu_inicial()