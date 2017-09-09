#coding=utf-8
from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.base_url="http://www.baidu.com"
    def test_baidu(self):
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
        driver.find_element_by_id("su").click()
    def tearDown(self):
        self.driver.quit()
if __name__=="_main_":
    baidu = Baidu("test_baidu_search")
    testunit = unittest.TestSuite()
    testunit.addTest(baidu)

    fp = open('./result.html', 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title = '百度搜索测试报告',
                            description = '用例执行情况：')
    runner.run(testunit)  # 运行测试用例
    fp.close()