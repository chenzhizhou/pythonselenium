# -*- coding:utf-8 -*-
import datetime
import random
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def assertErr(driver, title):
    errorLocator = (By.XPATH, "//span[text()='提示']")
    try:
        WebDriverWait(driver, 2).until(EC.presence_of_element_located(errorLocator))
        logPrint('Error：' + title + ' 错误')
        WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//span[text()='是']")).click()
        sleep(0.5)
    except:
        logPrint(title + ' 正常')


def waitloadmask(driver):
    loadmasklocator = (By.XPATH, "//div[@class='loadmask-msg']")
    try:
        WebDriverWait(driver, 0.5).until(EC.presence_of_element_located(loadmasklocator))
    except:
        # logPrint('加载中未出现或消失太快')
        pass
    try:
        WebDriverWait(driver, 8).until_not(EC.presence_of_element_located(loadmasklocator))
    except:
        logPrint('ERROR：加载中…未消失')
        logPrint('Warn：刷新页面，跳过此条')
        driver.refresh()
        waitloadmask(driver)
        logPrint('↓↓↓↓↓↓↓↓错误↓↓↓↓↓↓↓↓')


def navigationBarClick(driver, navigationString):
    nvg = navigationString.split('-')
    # logPrint('点击 '+ navigationString)
    for i in nvg:
        xpath = "//span[text()='%s']" % i
        try:
            ActionChains(driver).move_to_element(driver.find_element_by_xpath(xpath)).click().perform()
        except:
            logPrint('Error：未能找到 ' + navigationString)
            break

def randomClick(elements):
    elements[random.randint(0, len(elements) - 1)].click()

def viewIt(driver, tag):
    try:
        checkboxLists = driver.find_elements_by_xpath("//td[@class='cloud-table-select-column']")
        randomClick(checkboxLists)
        driver.find_element_by_xpath("//a[@title='查看']").click()
        waitloadmask(driver)
        assertErr(driver, tag + '查看')
        driver.find_element_by_xpath("//div[@class='ui-window-title-close']").click()
    except:
        logPrint('Warn：无'+ tag + '可查看')

def logPrint(logstr):
    filepath = '.runlog.log'
    now = str(datetime.datetime.now())
    logstr = now + ' ' +logstr
    with open(filepath, 'a', encoding='utf-8') as f:
        print(logstr)
        f.write(logstr+'\t\n')