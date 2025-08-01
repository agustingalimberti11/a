def test_login(browser):
    browser.get("https://demo.guru99.com/test/newtours/")
    browser.find_element("name", "userName").send_keys("agustin")
    browser.find_element("name", "password").send_keys("1234")
    browser.find_element("name", "submit").click()