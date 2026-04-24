# language: pt

Funcionalidade: Carrinho de compras

  Cenário: Adicionar um produto com sucesso
    Dado que o carrinho está vazio
    Quando eu adiciono 2 unidades com estoque de 5 e preço unitário de 10
    Então o total do carrinho deve ser 20
    E a quantidade de itens deve ser 2

  Cenário: Tentar adicionar um produto sem estoque suficiente
    Dado que o carrinho está vazio
    Quando eu adiciono 10 unidades com estoque de 3 e preço unitário de 15
    Então deve ocorrer o erro "Estoque insuficiente"