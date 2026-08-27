import hashlib
import random


class Assinante:

    def __init__(self, nome: str, plano: str, senha_plana: str):
     
        self.id_conta = random.randint(1000, 9999)
        self.nome = nome
        self.plano = plano
       
        self.senha_hash = self._gerar_hash(senha_plana)

    def _gerar_hash(self, senha_plana: str):
       
        return hashlib.sha256(senha_plana.encode("utf-8")).hexdigest()

    def exibir_dados(self):
        
        return f"ID: {self.id_conta} | Nome: {self.nome} | Plano: {self.plano} | Hash Senha: {self.senha_hash[:10]}..."