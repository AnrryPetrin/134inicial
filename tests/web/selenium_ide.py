from selenium import webdriver
from selenium.webdriver.common.by import By


class TestComprarPassagem:
    def setup_method(self,):
        self.driver = webdriver.Edge('../../vendors/drivers/msedgedriver103.0.1264.49.exe')
        self.vars = {}

    def teardown_method(self,):
        self.driver.quit()

    def test_comprar_passagem(self):
        self.driver.get("https://www.blazedemo.com/")
        self.driver.set_window_size(1294, 1032)
        self.driver.find_element(By.NAME, "fromPort").click()
        dropdown = self.driver.find_element(By.NAME, "fromPort")
        dropdown.find_element(By.XPATH, "//option[. = 'São Paolo']").click()
        self.driver.find_element(By.NAME, "toPort").click()
        dropdown = self.driver.find_element(By.NAME, "toPort")
        dropdown.find_element(By.XPATH, "//option[. = 'New York']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .btn").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(4)").text == "Price: 400"
        self.driver.find_element(By.ID, "inputName").click()
        self.driver.find_element(By.ID, "inputName").send_keys("Paolo")
        self.driver.find_element(By.CSS_SELECTOR, ".control-group:nth-child(3) > .controls").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Thank you for your purchase today!"
        self.driver.find_element(By.CSS_SELECTOR, ".hero-unit").click()
