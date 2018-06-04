# -*- coding:utf-8 -*-
import datetime
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def assertErr(driver, title):
    errorLocator = (By.XPATH, "//span[text()='提示']")
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(errorLocator))
        # print('-'*6, title, '-'*6, '错误')
        logPrint('Error：' + title + ' 错误')
        WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//span[text()='是']")).click()
        sleep(0.5)
    except:
        # print(title, '正常')
        logPrint(title + ' 正常')


def waitloadmask(driver):
    loadmasklocator = (By.XPATH, "//div[@class='loadmask-msg']")
    try:
        WebDriverWait(driver, 0.5).until(EC.presence_of_element_located(loadmasklocator))
    except:
        logPrint('加载中未出现或消失太快')
    try:
        WebDriverWait(driver, 8).until_not(EC.presence_of_element_located(loadmasklocator))
    except:
        logPrint('ERROR：加载中…未消失')
        logPrint('Warn：刷新页面，跳过此条')
        driver.refresh()
        waitloadmask(driver)


def navigationBarClick(driver, navigationString):
    nvg = navigationString.split('-')
    logPrint('点击 '+ navigationString)
    for i in nvg:
        xpath = "//span[text()='%s']" % i
        try:
            ActionChains(driver).move_to_element(driver.find_element_by_xpath(xpath)).click().perform()
        except:
            logPrint('Error：未能找到 ' + navigationString)
            break


def logPrint(logstr):
    filepath = '.runlog.log'
    now = str(datetime.datetime.now())
    logstr = now + ' ' +logstr
    with open(filepath, 'a', encoding='utf-8') as f:
        print(logstr)
        f.write(logstr+'\t\n')