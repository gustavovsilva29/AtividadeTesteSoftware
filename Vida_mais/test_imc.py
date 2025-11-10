import pytest
from imc import calcular_imc, classificar_imc


# -------------------------------
# Testes do cálculo de IMC
# -------------------------------

def test_calculo_imc_valor_correto():
    """Teste se calcular_imc(70, 1.75) retorna 22.86"""
    resultado = calcular_imc(70, 1.75)
    assert resultado == 22.86


def test_calculo_imc_arredondamento():
    """Teste se o IMC é arredondado para 2 casas decimais"""
    resultado = calcular_imc(80, 1.80)  # 80 / (1.8^2) = 24.691...
    assert resultado == round(24.691358024691358, 2)
    assert isinstance(resultado, float)


def test_calculo_imc_altura_zero():
    """Teste se altura = 0 gera ValueError"""
    with pytest.raises(ValueError):
        calcular_imc(70, 0)


# -------------------------------
# Testes da classificação de IMC
# -------------------------------

def test_classificacao_abaixo_peso():
    assert classificar_imc(17.9) == "Abaixo do peso"


def test_classificacao_peso_normal():
    assert classificar_imc(22.0) == "Peso Ideal"


def test_classificacao_sobrepeso():
    assert classificar_imc(27.3) == "Sobrepeso"


def test_classificacao_obesidade_grau_1():
    assert classificar_imc(33.0) == "Obesidade Grau I"


def test_classificacao_obesidade_grau_2():
    assert classificar_imc(37.0) == "Obesidade Grau II"


def test_classificacao_obesidade_grau_3():
    assert classificar_imc(45.0) == "Obesidade Grau III"