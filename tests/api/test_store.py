# ToDo: 1 - criar uma venda de um pet para um usuário
# ToDo: 2 - consultar os dados do pet que foi vendido
import json

import requests

url = 'https://petstore.swagger.io/v2/store/order'
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
        url=url,
        headers=headers,
        data=open('C:\\Users\\anrry\\PycharmProjects\\134inicial\\vendors\\json\\pedido1.json')
    )

    # retorno
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == id_pedido_esperado
    assert corpo_do_resultado_obtido['petId'] == pet_id_esperado
    assert corpo_do_resultado_obtido['status'] == status_pedido_esperado
