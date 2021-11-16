import pytest

from main import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros, \
    elevar_um_numero_pelo_outro, calcular_area_de_um_quadrado, calcular_area_de_um_tringulo, \
    calcular_area_de_um_retangulo, calcular_area_do_circulo


def test_somar_dois_numeros():
    # - 1 Etapa: Configura / Prepara
    # dados / Valores
    # Entrada / Input
    num1 = 5
    num2 = 7
    # Saida / Output

    resultado_esperado = 12

    # - 2 Etapa: Executar
    resultado_atual = somar_dois_numeros(num1, num2)

    # 3 Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

def test_subtrair_dois_numeros():
    num1 = 7
    num2 = 5
    resultado_atual = subtrair_dois_numeros(num1, num2)
    resultado_esperado = 2
    assert resultado_atual == resultado_esperado

def test_multiplicar_dois_numeros():
    num1 = 7
    num2 = 5
    resultado_atual = multiplicar_dois_numeros(num1, num2)
    resultado_esperado = 35
    assert resultado_atual == resultado_esperado

def test_dividir_dois_numeros():
    num1 = 10
    num2 = 2
    resultado_atual = dividir_dois_numeros(num1, num2)
    resultado_esperado = 5.0
    assert resultado_atual == resultado_esperado

def test_elevar_um_numero_pelo_outro():
    num1 = 2
    num2 = 3
    resultado_atual = elevar_um_numero_pelo_outro(num1, num2)
    resultado_esperado = 8
    assert resultado_atual == resultado_esperado

def test_calcular_area_de_um_quadrado():
    num1 = 3
    num2 = 4
    resultado_atual = calcular_area_de_um_quadrado(num1, num2)
    resultado_esperado = 12
    assert resultado_atual == resultado_esperado

def test_calcular_area_de_um_tringulo():
    num1 = 3
    num2 = 4
    resultado_atual = calcular_area_de_um_tringulo(num1, num2)
    resultado_esperado = 6.0
    assert resultado_atual == resultado_esperado

def test_calcular_area_de_um_retangulo():
    num1 = 5
    num2 = 2
    resultado_atual = calcular_area_de_um_retangulo(num1, num2)
    resultado_esperado = 10
    assert resultado_atual == resultado_esperado

def testar_calcular_area_do_circulo():
    # 1 configura
    raio = 2 #entrada
    resultado_esperado = 12.56
    # 2 executa
    resultadoatual = calcular_area_do_circulo(raio)

    # 3 valida
    assert resultadoatual == resultado_esperado

    #oi