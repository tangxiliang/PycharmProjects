# -*- coding: utf-8 -*-
from selenium import webdriver
from count import login

class loginTest():
    def __init__(self):
        self.driver = webdriver('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.get('http://oa.byxem.com')

    def test_admin_login(self):
        username = 'admin'
        password = '123'
        login().user_login(self.driver,username,password)
        self.driver.quit()

    def test_guest_login(self):
        username = 'guest'
        password = '321'
        login().user_login(self.driver,username,password)
        self.driver.quit()
loginTest().test_admin_login()
loginTest().test_guest_login()