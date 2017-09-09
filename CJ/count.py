#coding=utf-8
import time
from selenium import webdriver

driver =webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('http://oa.byxem.com');

class login():
   def user_login(self,driver):
       driver.find_element_by_id("idInput").clear()
       driver.find_element_by_id("idInput").send_keys("username")
       driver.find_element_by_id("pwdInput").clear()
       driver.find_element_by_id("pwdInput").send_keys("123456")
       driver.find_element_by_id("loginBtn").click()

   def user_logout(self,driver):
       driver.find_element_by_link_text("退出").click()
       driver.quit()