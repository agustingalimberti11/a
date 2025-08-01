from Pages.login_page import LoginPage



def test_registro2(browser):
    login_page = LoginPage(browser)
    login_page.load()
    login_page.login("maxi", "123")