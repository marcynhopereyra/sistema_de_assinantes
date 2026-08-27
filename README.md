# 🎬 Sistema de Gerenciamento de Assinantes

Um sistema orientado a objetos desenvolvido em Python para gerenciamento de assinantes de uma plataforma de streaming. O projeto demonstra conceitos fundamentais de **Programação Orientada a Objetos (POO)**, **encapsulamento de dados**, **hashing criptográfico de senhas** e interface via linha de comando (**CLI**).

---

## 📌 Funcionalidades

- **🔒 Criptografia de Senhas:** Senhas nunca são armazenadas em texto simples. Elas são convertidas para hash **SHA-256** no momento em que o objeto é instanciado.
- **🆔 Gerenciamento de ID:** Geração automática de identificador único numérico de 4 dígitos (entre 1000 e 9999).
- **👤 Cadastro de Assinantes:** Registro completo contendo Nome, Plano (*Básico*, *Padrão* ou *Premium*) e Senha com hash criptográfico.
- **📋 Listagem de Assinantes:** Exibição interativa e formatada de todas as contas ativas na plataforma.
- **❌ Cancelamento de Assinatura:** Remoção de assinantes do sistema a partir do seu ID numérico.
- **📊 Relatório de Encerramento:** Apresentação automática do estado final das contas cadastradas ao encerrar a aplicação.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Módulos Nativos:**
  - `hashlib`: Para geração do hash SHA-256 das senhas.
  - `random`: Para geração dos IDs únicos das contas.

---

## 📁 Estrutura do Projeto

```bash
.
├── assinantes.py           # Classe Entidade Assinante (Atributos e Criptografia)
├── PlataformaStreaming.py  # Classe Controladora (Regras de negócio e lista de contas)
├── main.py                 # Ponto de entrada e Interface CLI (Menu interativo)
└── README.md               # Documentação do projeto
