# configura
# bibliotecas / imports
from selenium import webdriver
from selenium.webdriver.common.by import By

# dados de entrada
origem = 'São Paolo'
destino = 'New York'
primeiro_nome = 'Juca'
bandeira = 'American Express'
lembrar_de_mim = True

# resultados esperados
titulo_passagens_esperado = 'Flights from São Paolo to Buenos Aires:'
mensagem_agradecimentp_esperada = 'Thank you for your purchase today!'
preco_passagem_esperado = '555 USD'


# executa
class Testes:
    # inicio
    def setup_method(self):
        # instanciar a biblioteca / motor / engine
        # informar onde esta o WebDriver
        self.driver = webdriver.Edge('../../vendors/drivers/msedgedriver103.0.1264.49.exe')

    # fim
    def teardown_method(self):
        # destruir o objeto da biblioteca utilizado
        self.driver.quit()

    # meio
    def testar_comprar_passagem(self):
        # e2e / end to end / ponta a ponta
        # pagina inicial (home)
        # executa / valida
        # abrir o browser no endereco
        self.driver.get("https://www.blazedemo.com")
        # clicar na lista de cidades de origem
        lista = self.driver.find_element(By.NAME, "fromPort")
        lista.click()
        # selecionar a cidade desejada
        lista.find_element(By.XPATH, "//option[. = 'São Paolo']").click()
        # clicar na lista de cidades de origem
        lista = self.driver.find_element(By.NAME, "toPort")
        lista.click()
        # selecionar a cidade de destino
        lista.find_element(By.XPATH, "//option[. = 'New York']")
        # clicar no botao de procurar voos
        self.driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary")


        # pagina lista de passagens
        # executa / valida

        # pagina de compra
        # executa / valida

        # pagina de obrigado
        # executa / valida

    # valida
