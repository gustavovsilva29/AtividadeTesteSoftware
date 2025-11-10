import pytest
from eficiencia_motor import calcular_eficiencia, classificar_eficiencia, analise_motor


# -------------------------------
# Testes de cálculo de eficiência
# -------------------------------

def test_calculo_eficiencia_valor_correto():
    """Teste se calcular_eficiencia(900, 1000) retorna 90.0"""
    resultado = calcular_eficiencia(900, 1000)
    assert resultado == 90.0


def test_calculo_eficiencia_arredondamento():
    """Teste se calcular_eficiencia(855, 1000) retorna 85.5"""
    resultado = calcular_eficiencia(855, 1000)
    assert resultado == 85.5


def test_calculo_eficiencia_divisao_por_zero():
    """Teste se potencia_entrada = 0 gera ValueError"""
    with pytest.raises(ValueError):
        calcular_eficiencia(900, 0)


# -------------------------------
# Testes da classificação de eficiência
# -------------------------------

def test_classificacao_baixa_eficiencia():
    assert classificar_eficiencia(75.0) == "IE1 - Baixa eficiência"


def test_classificacao_eficiencia_media():
    assert classificar_eficiencia(85.0) == "IE2 - Eficiência média"


def test_classificacao_alta_eficiencia():
    assert classificar_eficiencia(92.0) == "IE3 - Alta eficiência"


# -------------------------------
# Teste de integração
# -------------------------------

def test_analise_motor_integracao():
    """Teste de integração da função analise_motor"""
    eficiencia, classificacao = analise_motor(880, 1000)
    assert eficiencia == 88.0
    assert classificacao == "IE2 - Eficiência média"