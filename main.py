import pytest

# Cozinheiro - Definições
def somar_dois_numeros(num1, num2):
    return num1 + num2

def subtrair_dois_numeros(num1, num2):
    return num1 - num2

def multiplicar_dois_numeros(num1, num2):
    return num1 * num2

def dividir_dois_numeros(num1, num2):
    return num1 / num2

def elevar_um_numero_pelo_outro(num1, num2):
    return num1 ** num2

def calcular_area_de_um_quadrado(area, lado):
    return area * lado

def calcular_area_de_um_tringulo( lado1, lado2):
    return lado1 * lado2 /2

def calcular_area_de_um_retangulo(largura, comprimento):
    return largura * comprimento

def calcular_area_do_circulo(raio):
    return 3.14 * raio ** 2


if __name__ == '__main__':
    # Garçon - Requisições / Chamadas
    soma = somar_dois_numeros(5, 7)
    print(f'A soma é {soma}')  # <-- Prato

    subtracao = subtrair_dois_numeros(7, 5)
    print(f'A subtração é {subtracao}')

    multiplicar = multiplicar_dois_numeros(7, 5)
    print(f'A multiplicar é {multiplicar}')

    dividir = dividir_dois_numeros(10, 2)
    print(f'A dividir é {dividir}')

    elevar = elevar_um_numero_pelo_outro(2, 3)
    print(f'A exponenciação é {elevar}')

    area = calcular_area_de_um_quadrado(3, 4)
    print(f'O perimetro do quadrado é {area}')

    area = calcular_area_de_um_tringulo(3, 4)
    print(f'A área do triãngulo é {area}')

    area = calcular_area_de_um_retangulo(5, 2)
    print(f'A Área de retangulo é {area}')



    # Degustador / teste

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

