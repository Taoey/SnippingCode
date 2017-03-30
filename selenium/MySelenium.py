#conding=utf-8
import os
from selenium import webdriver

class OperateSelenium:
    def __init__(self,webdriver):
        chromedriver = "D:\CCApplication\Mozilla Firefox\firefox.exe"
        self.driver=webdriver

    #打开网页
    def open(self,url):
        self.driver.get(url)
    #下拉滚动条到底
    def down_scroll(self):
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)

    #获得网页源码
    def get_code(self):
        return self.driver.page_source


#TestDemo
# url='http://www.runoob.com/python/python-tutorial.html'
# s=OperateSelenium(webdriver.Firefox())
# s.open(url)
# s.down_scroll()
# print(s.get_code())