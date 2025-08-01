
def test_registro(browser):
    browser.get("https://demo.guru99.com/test/newtours/")
    browser.find_element("link text", "REGISTER").click()