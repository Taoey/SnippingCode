import os
from selenium import webdriver

chromedriver = "D:\CCApplication\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox()

driver.get("http://www.runoob.com/python/python-tutorial.html")


#��������������
 def scroll_down():
	js="var q=document.documentElement.scrollTop=10000"
	driver.execute_script(js)
	
#�����ҳԴ��
def source_code():
	return driver.page_source
	

