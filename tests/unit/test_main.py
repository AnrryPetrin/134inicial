import csv

import pytest

from main import somar, dividir, subtrair, multiplicar


def ler_csv(arquivo_csv):
    dados_csv = []
    try:
        with open(arquivo_csv, newline='') as massa:
            campos = csv.reader(massa, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {arquivo_csv}')
    except Exception as fail:
        print(f'Falha imprevista: {fail}')


def teste_subtrair():

    numero_a = 15
    numero_b = 10
    resultado_esperado = 5

    resultado_obtido = subtrair(numero_a, numero_b)

    assert resultado_obtido == resultado_esperado


@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', ler_csv(
    '../../vendors/csv/massa_teste_subtrair_positivo.csv'))
def teste_subtrair_leitura_de_csv(numero_a, numero_b, resultado_esperado):

    resultado_obtido = subtrair(int(numero_a), int(numero_b))

    assert resultado_obtido == int(resultado_esperado)


def teste_somar():
    # 1 - Configura
    numero_a = 8
    numero_b = 7
    resultado_esperado = 15

    # 2 - Executa
    resultado_obtido = somar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado


def teste_multiplicar():

    numero_a = 2
    numero_b = 3
    resutado_esperado = 6

    resultado_obtido = multiplicar(numero_a, numero_b)

    assert resultado_obtido == resutado_esperado


def teste_dividir_positivo():
    # 1 - Configura
    # 1.1 - Dados de Entrada
    numero_a = 27
    numero_b = 3

    # 1.2 - Resuldados Esperados
    resultado_esperado = 9

    # 2 - Executa
    resultado_obtido = dividir(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado


def teste_dividir_negativo():
    # 1 - Configura
    # 1.1 - Dados de Entrada
    numero_a = 27
    numero_b = 0

    # 1.2 - Resuldados Esperados
    resultado_esperado = 'Não dividiras por zero'

    # 2 - Executa
    resultado_obtido = dividir(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado


# lista para o uso como massa de teste
lista_de_valores = [
    (8, 7, 15),
    (20, 30, 50),
    (25, 0, 25),
    (-5, 12, 7),
    (6, -3, 3)
]
# essa lista é uma tupla, ume espécie de uma matriz ou vetor


@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', lista_de_valores)
def teste_somar_leitura_de_lista(numero_a, numero_b, resultado_esperado):
    # 1 - Configura
    # utilizamos a lista como massa de teste

    # 2 - Executa
    resultado_obtido = somar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado


@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', ler_csv(
    '../../vendors/csv/massa_teste_somar_positivo.csv'))
def teste_somar_leitura_de_csv(numero_a, numero_b, resultado_esperado):
    # 1 - Configura
    # utilizamos a lista como massa de teste

    # 2 - Executa
    resultado_obtido = somar(int(numero_a), int(numero_b))

    # 3 - Valida
    assert resultado_obtido == int(resultado_esperado)


# TDD = Test Driven Development
#       Desenvilvimento Direcionado por Teste

# - Criar todos os testes de unidade no começo
# - Executar todos os testes pelo menos 1 vez pr dia

# Imagine que você no 1º dia (nada pronto)
# Você executa todos os testes - o que acontece?
# Dia 01 - Falhou 100 - Passou 000
# Dia 02 - Falhou 095 - Passou 005
# Dia 03 - Falhou 090 - Passou 010
# Dia 04 - Falhou 088 - Passou 012
# Dia 05 - Falhou 081 - Passou 019
# Dia 06 - Falhou 075 - Passou 025
# Informação sobre o progresso
# Insistir mais um dia      1 + 1 = 2?
# Pedir ajuda               1 + 2 = 3
# Devolver e pegar outro    1 + 1 = 2!
# "Tudo certo!"             1 + 2 = 4
# TDD: Teste é uma medida de progresso

# CI: Continuous Integration
# (build) --> Suite de Testes --------> (Build)
#              Automatizada    passou
# Ambiente                               Então, move >> Ambiente
# de Desenvolvimento                                    de Teste

# CD: Continuous Delivery
# EC: Entrega Continua

# (Build) --> Suite --> (Build) -----> (Build)
#   Dev      de Teste    Teste  Muitos Produção
#                               Testes
# Escrevi isso no github
# Eu vi
