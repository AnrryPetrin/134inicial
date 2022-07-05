# Done: 1 - criar um teste que adiocone um usuário
# Done: 2 - realizar o login e extrair o token da resposta

import json

import requests

# variaveis publicas
url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}
token = ''


def teste_incluir_usuario():
    # configura
    # dados de entrada
    # os dados de entrada provem do arquivo usuario.json

    # resultados esperados
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '9529518'

    # executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('../../vendors/json/usuario1.json')
    )

    # valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == codigo_esperado
    assert corpo_do_resultado_obtido['type'] == tipo_esperado
    assert corpo_do_resultado_obtido['message'] == mensagem_esperada


def teste_login():
    # configura
    # dados de entrda
    username = 'batman'
    password = 'BatSenha'

    # resultados esperados
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = 'logged in user session'

    # executa
    resultado_obtido = requests.get(
        url=f'{url}/login?username={username}&password={password}',
        headers=headers
    )

    # valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == codigo_esperado
    assert corpo_do_resultado_obtido['type'] == tipo_esperado
    assert mensagem_esperada.find(corpo_do_resultado_obtido['message'])

    # extrai
    mensagem_extraida = corpo_do_resultado_obtido.get('message')
    print(f'mensagem = {mensagem_extraida}')
    token = mensagem_extraida[23:]
    print(f'tokem = {token}')
