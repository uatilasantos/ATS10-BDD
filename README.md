
# 🛒 Carrinho de Compras com BDD (pytest-bdd)

Este projeto implementa um sistema simples de carrinho de compras utilizando BDD (Behavior Driven Development) com Python.

O objetivo é demonstrar a comunicação entre negócio, desenvolvimento e QA, garantindo que os requisitos estejam alinhados e testáveis.

Transformar um requisito de negócio em:

 - Cenários em linguagem natural (Gherkin)
 - Código de regra de negócio (Python)
 - Testes automatizados (BDD com pytest)


# 📌 Tecnologias utilizadas
 - Python 3.13
 - pytest
 - pytest-bdd


# 📂 Estrutura do projeto

```bash
.
├── carrinho.feature     # Cenários em Gherkin
├── carrinho.py          # Regras de negócio
├── test_carrinho.py     # Testes automatizados (BDD)
└── README.md
```


# 🧠 Regra de negócio

O sistema deve:

Permitir adicionar produtos ao carrinho

Atualizar o total e a quantidade de itens

Impedir adição quando o estoque for insuficiente

Retornar erro: "Estoque insuficiente"


# 🧪 Cenários de teste (BDD)

✅ Cenário 1: Adição com sucesso

 - Adiciona produto com estoque suficiente

 - Atualiza total e quantidade corretamente

❌ Cenário 2: Falha por falta de estoque

 - Tenta adicionar mais itens do que o disponível

 - Retorna erro "Estoque insuficiente"


# ⚙️ Instalação

Clone o repositório:
```bash
git clone https://github.com/uatilasantos/ATS10-BDD.git
cd ATS10-BDD
```

Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

Instale as dependências:

```bash
pip install pytest pytest-bdd
```
# ▶️ Como executar os testes
```bash
pytest test_carrinho.py -v
```

Saída esperada:
```bash
2 passed
```

# ⚠️ Observação importante

Como os cenários estão em português, o arquivo .feature precisa conter:
```bash
# language: pt
```

# 🧩 Desafio técnico aplicado

No cenário de erro, foi utilizado:

 - try...except no passo @when
 - Armazenamento do erro no estado (carrinho["erro"])
 - Validação da mensagem no @then

Isso evita que o teste falhe prematuramente e permite validar o comportamento corretamente.

# 📚 Conceitos aplicados
 - BDD (Behavior Driven Development)
 - Gherkin
 - Testes automatizados
 - Separação de responsabilidades (Negócio, Dev, QA)
 - Tratamento de exceções em testes
 
# 🚀 Resultado

Os testes comprovam que:

O comportamento esperado pelo negócio está implementado
O sistema responde corretamente tanto em sucesso quanto em erro
A comunicação entre requisitos e código está alinhada

# Autor

Uatila Dos Santos Silva