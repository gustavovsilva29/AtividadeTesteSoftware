import pytest
from imc import calcular_imc, classificar_imc

test_calculo_imc():
    """Teste se calcular_imc(70, 1.75) retorna 22.86"""
    resultado = calcular_imc(70, 1.75)
    assert resultado == 22.86

def test_calculo_imc():
    """Teste se o IMC é arredondado para 2 casas decimais"""
    resultado = calcular_imc(80, 1.80)  # 80 / (1.8^2) = 24.691...
    assert resultado == round(24.691358024691358, 2)
    assert isinstance(resultado, float)

def test_calculo_imc():
    """Teste se altura = 0 gera ValueError"""
    with pytest.raises(ValueError):
        calcular_imc(70, 0)

def test_classificacao():
    assert classificar_imc(17.9) == "Abaixo do peso"

def test_classificacao():
    assert classificar_imc(22.0) == "Peso normal"

def test_classificacao():
    assert classificar_imc(27.3) == "Sobrepeso"

def test_classificacao():
    assert classificar_imc(33.0) == "Obesidade grau I"

def test_classificacao():
    assert classificar_imc(37.0) == "Obesidade grau II"

def test_classificacao():
    assert classificar_imc(45.0) == "Obesidade grau III"