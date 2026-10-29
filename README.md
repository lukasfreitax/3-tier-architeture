# 🏗️ 3-Tier Architecture

Estudo prático de **Arquitetura em 3 Camadas** com **Python**, abordando validações, regras de negócio e fundamentos de segurança.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20estudo-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📖 Sobre o projeto

Este repositório demonstra, de forma prática, como organizar uma aplicação em três camadas bem definidas, separando responsabilidades para facilitar manutenção, testes e evolução do código.

O foco é o aprendizado dos conceitos de arquitetura aplicados em Python, incluindo:

- Separação clara de responsabilidades
- Validação de dados de entrada
- Aplicação de regras de negócio isoladas
- Boas práticas básicas de segurança

---

## 🧱 Arquitetura

```
┌──────────────────────────────────────────┐
│  1. Camada de Apresentação               │
│     Interface / entrada e saída de dados │
└────────────────────┬─────────────────────┘
                     │
┌────────────────────▼─────────────────────┐
│  2. Camada de Negócio (Service)          │
│     Regras de negócio e validações       │
└────────────────────┬─────────────────────┘
                     │
┌────────────────────▼─────────────────────┐
│  3. Camada de Dados (Repository)         │
│     Persistência e acesso ao banco       │
└──────────────────────────────────────────┘
```

| Camada | Responsabilidade | O que **não** deve fazer |
|---|---|---|
| **Apresentação** | Receber dados do usuário e exibir resultados | Conter regras de negócio ou acessar o banco diretamente |
| **Negócio** | Validar dados, aplicar regras e orquestrar o fluxo | Conhecer detalhes de interface ou de SQL |
| **Dados** | Ler e gravar informações na fonte de dados | Tomar decisões de negócio |

> A comunicação acontece sempre **de cima para baixo**: apresentação → negócio → dados.

---

## 📁 Estrutura sugerida

```
3-tier-architeture/
├── presentation/      # Camada de apresentação (CLI, API ou UI)
├── business/          # Regras de negócio e validações
├── data/              # Acesso a dados / repositórios
├── tests/             # Testes automatizados
├── main.py            # Ponto de entrada
├── requirements.txt   # Dependências
└── README.md
```

> ⚠️ Ajuste os nomes das pastas conforme a estrutura real do seu projeto.

---

## 🔐 Segurança

Fundamentos aplicados ou estudados neste projeto:

- **Validação e sanitização** de todas as entradas
- **Consultas parametrizadas** para prevenir SQL Injection
- **Separação de camadas** para reduzir a superfície de ataque
- **Tratamento de erros** sem expor detalhes internos ao usuário
- **Hash de senhas** (nunca armazenar em texto puro)
- **Variáveis de ambiente** para credenciais e segredos

---

## 🚀 Como executar

### Pré-requisitos

- Python 3.10 ou superior
- `pip`

### Instalação

```bash
# Clone o repositório
git clone https://github.com/lukasfreitax/3-tier-architeture.git
cd 3-tier-architeture

# (Opcional) Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows

# Instale as dependências
pip install -r requirements.txt
```

### Execução

```bash
python main.py
```

---

## 🧪 Testes

```bash
pytest
```

---

## 🎯 Objetivos de aprendizado

- [x] Entender o conceito de arquitetura em camadas
- [x] Separar apresentação, negócio e dados
- [x] Implementar validações e regras de negócio
- [x] Aplicar fundamentos de segurança
- [ ] Adicionar testes automatizados
- [ ] Integrar com banco de dados real
- [ ] Expor uma API (FastAPI/Flask)

---

## 🛠️ Tecnologias

- [Python](https://www.python.org/)

---

## 🤝 Contribuindo

Sugestões e melhorias são bem-vindas!

1. Faça um fork do projeto
2. Crie uma branch: `git checkout -b feature/minha-feature`
3. Commit suas alterações: `git commit -m "feat: minha feature"`
4. Envie para a branch: `git push origin feature/minha-feature`
5. Abra um Pull Request

---

## 📄 Licença

Distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais informações.

---

## 👤 Autor

**Lukas Freitas**
GitHub: [@lukasfreitax](https://github.com/lukasfreitax)
