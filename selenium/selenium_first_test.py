'''
1.配置好火狐的驱动（把驱动放在和firefox.exe同一目录下，然后把这个文件所在的目录配成环境变量  ，比如这个程序所在的环境一定配置的是"D:\CCApplication\Mozilla Firefox"）（Windows系统 Python3）

2.下载python的selenium模块 使用 pip install selenium 即可

3.运行下面的代码，如果可以打开火狐浏览器，则你的环境配置好了欧

注意：
firefox 47以上版本，需要下载第三方driver，即geckodriver，在http://docs.seleniumhq.org/download/的Third Party Drivers, Bindings, and Plugins下面找到Mozilla GeckoDriver
'''

import os
from selenium import webdriver

chromedriver = "D:\CCApplication\Mozilla Firefox\firefox.exe"

driver = webdriver.Firefox()

driver.get('https://www.baidu.com')

#driver.quit()