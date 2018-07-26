# -*- coding:utf-8 -*-
import datetime
import random
import string
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait






def randomClick(elements):
    clickCount = random.randint(0, len(elements) - 1)
    elements[clickCount].click()
    return clickCount

def noFirstRandomClick(elements):
    clickCount = random.randint(1, len(elements) - 1)
    elements[clickCount].click()
    return clickCount

def randomClick_more(elements):
    moreClickTime = random.randint(1, len(elements))
    i = 0
    count = randomClick(elements)
    while i < moreClickTime:
        try:
            randomClick(elements)
        except:
            pass
        i += 1
        sleep(0.5)

def addButtonClick(driver):
    try:
        WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//a[@title='新增']")).click()
        WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//div[@id='ui-window-body']"))
        return True
    except:
        return False


def isElementExist(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False

def randomString(length):
    salt = ''.join(random.sample(string.ascii_letters + string.digits, length))
    return salt
