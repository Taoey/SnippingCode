'''
1.���úû�������������������ں�firefox.exeͬһĿ¼�£�Ȼ�������ļ����ڵ�Ŀ¼��ɻ�������  ����������������ڵĻ���һ�����õ���"D:\CCApplication\Mozilla Firefox"����Windowsϵͳ Python3��

2.����python��seleniumģ�� ʹ�� pip install selenium ����

3.��������Ĵ��룬������Դ򿪻�������������Ļ������ú���ŷ

ע�⣺
firefox 47���ϰ汾����Ҫ���ص�����driver����geckodriver����http://docs.seleniumhq.org/download/��Third Party Drivers, Bindings, and Plugins�����ҵ�Mozilla GeckoDriver
'''

import os
from selenium import webdriver

chromedriver = "D:\CCApplication\Mozilla Firefox\firefox.exe"

driver = webdriver.Firefox()

driver.get('https://www.baidu.com')

#driver.quit()