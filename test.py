# -*- coding:utf-8 -*-
import os
import random
import shutil
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from defAssist import waitloadmask, assertErr, navigationBarClick, logPrint, randomClick, viewIt

chromedriverpath = '.\\libs\\chromedriver.exe'
runlogpath = '.runlog.log'
try:
    shutil.rmtree('.\\download')
    os.remove(runlogpath)
except:
    pass
os.mkdir('.\\download')
print(os.getcwd())
file = open(runlogpath, 'wb')
chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': os.getcwd()+'\\download'}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriverpath)
driver.set_window_size(1366, 768)
driver.get('http://182.150.21.232:10081/DeviceNetwork/www/')
logPrint('打开页面')
WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//input[@id='home-input-user']")).clear()
WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//input[@id='home-input-user']")).send_keys('chenzhiz@inhand.com.cn')
WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//input[@id='home-input-pwd-password']")).clear()
WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//input[@id='home-input-pwd-password']")).send_keys('czz123456')
logPrint('输入用户名与密码')
sleep(0.5)
WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//button[@id='home-input-submit']")).click()
logPrint('登录')
waitloadmask(driver)
assertErr(driver, '首页概览')
sleep(3)

navigationBarClick(driver, '增值服务-促销活动-自定义取货码')
waitloadmask(driver)
assertErr(driver, '自定义取货码')
pickcodeLists = driver.find_elements_by_xpath("//a[@class='detail']")
randomClick(pickcodeLists)
waitloadmask(driver)
assertErr(driver, '自定义取货码查看')
driver.find_element_by_xpath("//div[@class='ui-window-title-close']").click()













