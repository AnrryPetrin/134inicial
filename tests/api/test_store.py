# Done: 1 - criar uma venda de um pet para um usuário
# Done: 2 - consultar os dados do pet que foi vendido
import json

import requests

url = 'https://petstore.swagger.io/v2/'
headers = {'Content-Type': 'application/json'}


def teste_vender_pet():
    # configura
    # dados de entrada
    # provem do arquivo pedido1.json

    # resultados esperados
    status_code_esperado = 200
    id_pedido_esperado = 985189529
    pet_id_esperado = 5189529
    status_pedido_esperado = 'placed'

    # executa
    resultado_obtido = requests.post(
        url=url + 'store/order',
        headers=headers,
        data=open('../../vendors/json/pedido1.json')
    )

    # valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == id_pedido_esperado
    assert corpo_do_resultado_obtido['petId'] == pet_id_esperado
    assert corpo_do_resultado_obtido['status'] == status_pedido_esperado

    # extrai
    pet_id_extraido = corpo_do_resultado_obtido.get('petId')

    # realizar a consulta da primeira transação

    # configura
    # dados de entrada
    # provem da transação acima

    # resultado esperado
    pet_name_esperado = 'Hex'
    status_code_esperado = 200

    # executa
    resultado_obtido = requests.get(
        url=url + 'pet/' + str(pet_id_extraido),
        headers=headers
    )

    # valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    corpo_do_resultado_obtido = resultado_obtido.json()
    assert corpo_do_resultado_obtido['name'] == pet_name_esperado
    assert resultado_obtido.status_code == status_code_esperado
