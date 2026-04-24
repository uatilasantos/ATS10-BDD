from pytest_bdd import scenarios, given, when, then, parsers
from carrinho import criar_carrinho, adicionar_produto


scenarios("carrinho.feature")


@given("que o carrinho está vazio", target_fixture="carrinho")
def carrinho_vazio():
    return criar_carrinho()


@when(
    parsers.parse(
        "eu adiciono {quantidade:d} unidades com estoque de {estoque:d} e preço unitário de {preco:d}"
    )
)
def adicionar_item(carrinho, quantidade, estoque, preco):
    try:
        adicionar_produto(carrinho, quantidade, estoque, preco)
    except ValueError as erro:
        carrinho["erro"] = str(erro)


@then(parsers.parse("o total do carrinho deve ser {total_esperado:d}"))
def validar_total(carrinho, total_esperado):
    assert carrinho["total"] == total_esperado


@then(parsers.parse("a quantidade de itens deve ser {itens_esperados:d}"))
def validar_itens(carrinho, itens_esperados):
    assert carrinho["itens"] == itens_esperados


@then(parsers.parse('deve ocorrer o erro "{mensagem_esperada}"'))
def validar_erro(carrinho, mensagem_esperada):
    assert carrinho["erro"] == mensagem_esperada