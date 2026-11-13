import pytest

from frete import calcular_frete


def test_frete_produto_500g():
    assert calcular_frete(500) == 10


def test_frete_produto_2000g():
    assert calcular_frete(2000) == 20


def test_frete_produto_6000g():
    assert calcular_frete(6000) == 30


@pytest.mark.parametrize("peso, esperado", [
    (1, 10), (1000, 10), (1001, 20),
    (5000, 20), (5001, 30),
])
def test_fronteiras_das_faixas(peso, esperado):
    assert calcular_frete(peso) == esperado


@pytest.mark.parametrize("peso", [0, -1])
def test_peso_invalido(peso):
    with pytest.raises(ValueError):
        calcular_frete(peso)


def test_limite_maximo_10000g_ainda_e_aceito():
    assert calcular_frete(10000) == 30


def test_peso_acima_de_10000g_e_recusado():
    with pytest.raises(ValueError):
        calcular_frete(10001)
