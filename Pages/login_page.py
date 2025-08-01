# login_page.py

from selenium.webdriver.common.by import By
from base.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = 'https://demo.guru99.com/test/newtours/index.php'
        self.userName_input = (By.XPATH, "//input[@name='userName']")
        self.password_input = (By.NAME, "password")
        self.submit_button = (By.NAME, "submit")
        self.title_login = (By.XPATH, "//h3[text()='Login Successfully']")

    def load(self):
        self.ir_a(self.url)

    def login(self, username, password):
        self.escribir(self.userName_input, username)
        self.escribir(self.password_input, password)
        self.clickear(self.submit_button)

    def login_exitoso(self):
        return self.esta_visible(self.title_login)
