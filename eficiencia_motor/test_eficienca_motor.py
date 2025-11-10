import pytest
from eficiencia_motor import calcular_eficiencia, classificar_eficiencia, analise_motor

def test_calculo_eficiencia_valor_correto():
    resultado = calcular_eficiencia(900, 1000)
    assert resultado == 90.0

def test_calculo_eficiencia_arredondamento():
    resultado = calcular_eficiencia(855, 1000)
    assert resultado == 85.5

def test_calculo_eficiencia_divisao_por_zero():
    with pytest.raises(ValueError):
        calcular_eficiencia(900, 0)

def test_classificacao_baixa_eficiencia():
    assert classificar_eficiencia(75.0) == "IE1 - Baixa Eficiência"

def test_classificacao_eficiencia_media():
    assert classificar_eficiencia(85.0) == "IE2 - Eficiência média"

def test_classificacao_alta_eficiencia():
    assert classificar_eficiencia(92.0) == "IE3 - Alta Eficiência"

def test_analise_motor_integracao():
    eficiencia, classificacao = analise_motor(880, 1000)
    assert eficiencia == 88.0,
     classificacao == "IE2 - Eficiência média",
     potencia_saida == 880,
     potencia_entrada == 1000,