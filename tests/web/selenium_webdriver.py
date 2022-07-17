# configura
# bibliotecas / imports
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# dados de entrada
# origem = 'São Paolo'
# destino = 'New York'
primeiro_nome = 'Juca'
bandeira = 'American Express'
lembrar_de_mim = True

# resultados esperados
# titulo_voos_esperado = 'Flights from São Paolo to New York:'
mensagem_agradecimento_esperada = 'Thank you for your purchase today!'
preco_passagem_esperado = '555 USD'


# executa
class Testes:
    # inicio
    #    def setup_method(self, ):
    # instanciar a biblioteca / motor / engine
    # informar onde esta o WebDriver
    #        self.driver = webdriver.Edge()
    # espera implicita até 15 segundos por qualquer elemento
    # self.driver.implicitly_wait(15)

    # fim
    def teardown_method(self, ):
        # destruir o objeto da biblioteca utilizado
        self.driver.quit()

    # meio
    lista_de_valores = [
        ('São Paolo', 'New York', 'edge'),
        ('Philadelphia', 'Rome', 'chrome'),
        ('San Diego', 'Dublin', 'firefox'),
    ]

    @pytest.mark.parametrize('origem,destino,browser', lista_de_valores)
    def testar_comprar_passagem(self, origem, destino, browser):
        # e2e / end to end / ponta a ponta

        # trouxe o setup_method pra ca
        match browser:
            case 'edge':
                self.driver = webdriver.Edge()
            case 'chrome':
                self.driver = webdriver.Chrome()
            case 'firefox':
                self.driver = webdriver.Firefox()

        # pagina inicial (home)
        # executa / valida
        # abrir o browser no endereco
        self.driver.get("https://www.blazedemo.com")
        # clicar na lista de cidades de origem
        lista = self.driver.find_element(By.NAME, "fromPort")
        lista.click()
        # selecionar a cidade desejada
        lista.find_element(By.XPATH, f"//option[. = '{origem}']").click()
        # clicar na lista de cidades de origem
        self.driver.find_element(By.NAME, "toPort")
        lista.click()
        # selecionar a cidade de destino
        lista.find_element(By.XPATH, f"//option[. = '{destino}']").click()
        # clicar no botao de procurar voos
        self.driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()

        # pagina lista de voos
        # executa / valida
        assert self.driver.find_element(By.TAG_NAME, "h3").text == f"Flights from {origem} to {destino}:"
        # clicar no primeiro voo
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .btn").click()

        # pagina de compra
        # executa / valida
        # limpar o campo do nome para evitar problemas ao digitar
        self.driver.find_element(By.ID, "inputName").clear()
        # preenche o nome do comprador
        self.driver.find_element(By.ID, "inputName").send_keys(primeiro_nome)
        # seleciona a bandeira do cartao
        lista = self.driver.find_element(By.ID, 'cardType')
        lista.click()
        lista.find_element(By.XPATH, f"//option[. = '{bandeira}']").click()
        # marca o checkbox para ser lembrado
        self.driver.find_element(By.ID, "rememberMe").click()
        # clicar no botão de comprar voo
        self.driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()

        # pagina de obrigado
        # valida
        assert self.driver.find_element(By.TAG_NAME, 'h1').text == mensagem_agradecimento_esperada
        assert self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(3) > td:nth-child(2)'
                                        ).text == preco_passagem_esperado
