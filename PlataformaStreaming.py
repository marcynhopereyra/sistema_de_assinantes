from assinantes import Assinante


class PlataformaStreaming:

    def __init__(self):
        
        self.assinantes: list[Assinante] = []

    def cadastrar_assinante(self, assinante: Assinante):
        
        self.assinantes.append(assinante)

    def listar_assinantes(self):
    
        if not self.assinantes:
            print("\nNenhum assinante cadastrado.")
            return

        print("\n--- Assinantes Ativos ---")
        for assinante in self.assinantes:
            print(assinante.exibir_dados())

    def buscar_por_id(self, id_conta: int):
        
        for assinante in self.assinantes:
            if assinante.id_conta == id_conta:
                return assinante
        return None

    def cancelar_assinatura(self, id_conta: int):
        
        assinante = self.buscar_por_id(id_conta)
        if assinante:
            self.assinantes.remove(assinante)
            return True
        return False