import pytest

from Pages.login_page import LoginPage
from utils.leer_excel import leer_datos_excel

datos = leer_datos_excel("tests/datos_login.xlsx")

@pytest.mark.parametrize("username, password", datos)
def test_login_excel(browser, username, password):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login(username, password)