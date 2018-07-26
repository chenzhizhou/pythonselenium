# -*- coding:utf-8 -*-
import datetime
import os
import random
import shutil
import string
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from defAssist import randomClick, randomClick_more, \
    addButtonClick, randomString, noFirstRandomClick, isElementExist

def logPrint(logstr):
    pyfileName = str(__file__).split(".py")[0].split("/")[-1]
    filepath = ".\\log\\" + pyfileName + '-runlog.log'
    now = str(datetime.datetime.now())
    logstr = now + ' ' + logstr
    with open(filepath, 'a', encoding='utf-8') as f:
        print(logstr)
        f.write(logstr + '\t\n')

def isElementExist(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False

def waitloadmask(driver):
    loadmasklocator = (By.XPATH, "//div[@class='loadmask-msg']")
    try:
        WebDriverWait(driver, 1).until(EC.presence_of_element_located(loadmasklocator))
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

def assertErr(driver, title):
    errorLocator = (By.XPATH, "//span[text()='提示']")
    try:
        WebDriverWait(driver, 2).until(EC.presence_of_element_located(errorLocator))
        logPrint('Error：' + title + ' 错误')
        WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//span[text()='是']")).click()
        sleep(0.5)
    except:
        logPrint(title + ' 正常')

def assertSaveSuccess(driver, title):
    errorLocator = (By.XPATH, "//span[text()='提示']//..//..//div//span[contains(text(),'保存成功')]")
    try:
        WebDriverWait(driver, 2).until(EC.presence_of_element_located(errorLocator))
        logPrint(title + ' 正常')
        WebDriverWait(driver, 2).until(lambda x: x.find_element_by_xpath("//span[text()='是']")).click()
        sleep(0.5)
    except:
        logPrint('Error：' + title + ' 错误')

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

def viewIt(driver, tag):
    try:
        viewFlag = False
        if isElementExist(driver, "//a[@title='查看']"):
            viewButton = driver.find_element_by_xpath("//a[@title='查看']")
            checkboxLists = driver.find_elements_by_xpath("//td[@class='cloud-table-select-column']")
            randomClick(checkboxLists)
            viewFlag = True
            viewButton.click()
            waitloadmask(driver)
            assertErr(driver, tag + '查看')
            driver.find_element_by_xpath("//div[@class='ui-window-title-close']").click()
        if isElementExist(driver, "//a[@title='修改']"):
            editButton = driver.find_element_by_xpath("//a[@title='修改']")
            if viewFlag == False:
                checkboxLists = driver.find_elements_by_xpath("//td[@class='cloud-table-select-column']")
                randomClick(checkboxLists)
            editButton.click()
            waitloadmask(driver)
            assertErr(driver, tag + '修改')
            driver.find_element_by_xpath("//div[@class='ui-window-title-close']").click()
    except:
        logPrint('Warn：无' + tag + '可查看')


if __name__ == '__main__':
    logPrint('初始化：')
    chromedriverpath = '.\\libs\\chromedriver.exe'
    try:
        logpath = os.getcwd() + "\\log"
        # print(logpath)
        os.mkdir(logpath)
    except:
        pass
    pyfileName = str(__file__).split(".py")[0].split("/")[-1]
    logfilepath = ".\\log\\" + pyfileName + '-runlog.log'
    try:
        os.remove(logfilepath)
    except:
        pass
    try:
        shutil.rmtree('.\\download')
    except:
        pass
    os.mkdir('.\\download')
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': os.getcwd() + '\\download'}
    chrome_options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriverpath)
    driver.set_window_size(1366, 768)
    driver.get('http://182.150.21.232:10081/DeviceNetwork/www/')
    logPrint('打开页面')
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//input[@id='home-input-user']")).clear()
    WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//input[@id='home-input-user']")).send_keys(
        'chenzhiz@inhand.com.cn')
    WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//input[@id='home-input-pwd-password']")).clear()
    WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//input[@id='home-input-pwd-password']")).send_keys(
        'czz123456')
    logPrint('输入用户名与密码')
    sleep(0.5)
    WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//button[@id='home-input-submit']")).click()
    logPrint('登录')
    waitloadmask(driver)
    sleep(3)

    navigationBarClick(driver, '点位-区域管理')
    waitloadmask(driver)
    if addButtonClick(driver):
        try:
            textInput = driver.find_elements_by_xpath("//div[@id='ui-window-body']//input[@type='text']")
            for i in range(len(textInput)):
                textInput[i].send_keys(randomString(8))
            addedAreaName = randomString(8)
            addedAreaNameEle = driver.find_element_by_xpath("//div[@id='ui-window-body']//input[@id='areaname']")
            addedAreaNameEle.clear()
            addedAreaNameEle.send_keys(addedAreaName)
            driver.find_element_by_xpath("//div[@id='ui-window-body']//input[@value='保存']").click()
            assertErr(driver, '新增区域')
        except Exception as e:
            print(e)
            logPrint("ERROR：新增区域可能出现问题")

    navigationBarClick(driver, '点位-线路管理')
    waitloadmask(driver)
    if addButtonClick(driver):
        try:
            textInput = driver.find_elements_by_xpath("//div[@id='ui-window-body']//input[@type='text']")
            for i in range(len(textInput)):
                textInput[i].send_keys(randomString(8))
            addedLineName = randomString(8)
            addedLineNameEle = driver.find_element_by_xpath("//div[@id='ui-window-body']//input[@id='lineName']")
            addedLineNameEle.clear()
            addedLineNameEle.send_keys(addedLineName)
            driver.find_element_by_xpath("//div[@id='ui-window-body']//input[@value='保存']").click()
            assertErr(driver, '新增线路')
        except Exception as e:
            print(e)
            logPrint("ERROR：新增线路可能出现问题")

    navigationBarClick(driver, '点位-点位管理')
    waitloadmask(driver)
    if addButtonClick(driver):
        try:
            textInput = driver.find_elements_by_xpath("//div[@id='ui-window-body']//input[@type='text']")
            for i in range(len(textInput)):
                if textInput[i].get_attribute('id') == 'loc':
                    pass
                else:
                    textInput[i].send_keys(randomString(8))
                    driver.find_element_by_xpath("//div[@class='ui-window-title-name']").click()
            # mapEle = driver.find_element_by_xpath("//div[@class='BMap_mask']")
            # ActionChains(driver).drag_and_drop_by_offset(mapEle,150,150).perform()
            driver.find_element_by_xpath("//div[@id='ui-window-body']//textarea[@id='desc']").send_keys(randomString(16))
            addedSiteName = randomString(8)
            addedSiteNameEle = driver.find_element_by_xpath("//div[@id='ui-window-body']//input[@id='siteName']")
            addedSiteNameEle.clear()
            addedSiteNameEle.send_keys(addedSiteName)
            addSiteLineNameEle = driver.find_element_by_xpath("//select[@id='line']//..//input")
            addSiteLineNameEle.clear()
            addSiteLineNameEle.send_keys(addedLineName)
            costEle = driver.find_element_by_xpath("//div[@id='ui-window-body']//input[@id='cost']")
            costEle.clear()
            costEle.send_keys(''.join(random.sample(string.digits, 5)))
            driver.find_element_by_xpath("//div[@id='ui-window-body']//input[@value='保存']").click()
            assertSaveSuccess(driver, '新增点位')
        except Exception as e:
            print(e)
            logPrint("ERROR：新增点位可能出现问题")

    navigationBarClick(driver, '售货机-机型管理')
    waitloadmask(driver)
    if addButtonClick(driver):
        try:
            venderList = driver.find_elements_by_xpath("//select[@id='vender']//option")
            venderSelectNum = noFirstRandomClick(venderList)
            venderName = venderList[venderSelectNum].text
            machineTypeList = driver.find_elements_by_xpath("//select[@id='machineType']//option")
            machineTypeSelectNum = noFirstRandomClick(machineTypeList)
            machineTypeName = machineTypeList[machineTypeSelectNum].text
            # print(machineTypeName)
            modelName = driver.find_element_by_xpath("//input[@id='modelName']")
            modelNameText = randomString(8)
            modelName.send_keys(modelNameText)
            if machineTypeName == "饮料机" or machineTypeName == "白酒机":
                # driver.find_element_by_xpath("//input[@id='startNumber']").send_keys(random.randint(1, 20))
                driver.find_element_by_xpath("//input[@id='allNumber']").send_keys(random.randint(1, 20))
                driver.find_element_by_xpath("//input[@id='nextBase']").click()
                driver.find_element_by_xpath("//a[@id='model_submit']").click()
            elif machineTypeName == "弹簧机" or machineTypeName == "格子柜":
                driver.find_element_by_xpath("//input[@id='nextBase']").click()
                for i in range(1, random.randint(2, 6)):
                    # print(i)
                    rn = str(random.randint(1, 14))
                    # print(rn)
                    driver.find_element_by_xpath("//div[@class='selfTable'][text()='" + rn + "']").click()
                    driver.find_element_by_xpath("//div[@id='0_"+str(i)+"']").click()
                    value = str(i) + rn + '1'
                    # print(value)
                    driver.find_element_by_xpath("//div[@id='0_" + str(i) + "']//input").send_keys(value)
                driver.find_element_by_xpath("//input[@id='model_submit']").click()
            else:
                # driver.find_element_by_xpath("//input[@id='startNumber']").send_keys(random.randint(1, 20))
                driver.find_element_by_xpath("//input[@id='allNumber']").send_keys(random.randint(1, 5))
                driver.find_element_by_xpath("//input[@id='nextBase']").click()
                shelfTableList = driver.find_elements_by_xpath("//div[@class='shelfTable']")
                for i in range(len(shelfTableList)):
                    shelfTableList[i].click()
                selfTableCoffeeList = driver.find_elements_by_xpath("//div[@class='selfTableCoffee']//span[@class='modify']")
                for i in range(len(selfTableCoffeeList)):
                    selfTableCoffeeList[i].click()
                    coffeetypes = driver.find_elements_by_xpath("//select[@id='types']//option")
                    randomClick(coffeetypes)
                    tempmode = driver.find_elements_by_xpath("//input[@name='tempmode']")
                    randomClick(tempmode)
                    sugarmode = driver.find_elements_by_xpath("//input[@name='sugar']")
                    randomClick(sugarmode)
                    milkmode = driver.find_elements_by_xpath("//input[@name='milk']")
                    randomClick(milkmode)
                    icemode = driver.find_elements_by_xpath("//input[@name='ice']")
                    randomClick(icemode)
                    measurementmode = driver.find_elements_by_xpath("//input[@name='measurement']")
                    randomClick(measurementmode)
                    driver.find_element_by_xpath("//input[@id='saveConfig']")
                driver.find_element_by_xpath("//a[@id='model_submit']").click()
            waitloadmask(driver)
            assertErr(driver, "新增机型")
        except Exception as e:
            print(e)
            logPrint("ERROR：新增机型可能出现问题")

    navigationBarClick(driver, '售货机-售货机管理')
    waitloadmask(driver)
    if addButtonClick(driver):
        try:
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(
                "//select[@id='automat_vender']//option[text()='" + venderName + "']")).click()
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(
                "//select[@id='automat_machineType']//option[text()='" + machineTypeName + "']")).click()
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(
                "//select[@id='automat_model']//option[text()='" + modelNameText + "']")).click()
            addAssetid = randomString(10)
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(
                "//input[@id='assetId']")).send_keys(addAssetid)
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(
                "//input[@id='deviceName']")).send_keys(addAssetid)
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(
                "//input[@id='deviceName']")).send_keys(addAssetid)
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(
                "//select[@id='siteId']//option[contains(text(),'" + addedSiteName + "')]")).click()
            driver.find_element_by_xpath("//div[@class='ui-window-title-name']").click()
            driver.find_element_by_xpath("//input[@id='nextBase']").click()
            sleep(1)
            if not isElementExist(driver,"//input[@id='addCid'][contains(@style,'display: none')][@value='增加一个货柜']"):
                driver.find_element_by_xpath("//input[@id='addCid']").click()
                WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(
                    "//input[@id='cid1_assetId']")).send_keys(randomString(4))
                WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(
                    "//input[@id='cid1_vmcNum']")).send_keys(randomString(4))
                randomClick(driver.find_elements_by_xpath("//select[@id='cid1_plugIn']//option"))
                randomClick(driver.find_elements_by_xpath("//select[@id='cid1_serial']//option"))
                noFirstRandomClick(driver.find_elements_by_xpath("//select[@id='cid1_vender']//option"))
                noFirstRandomClick(driver.find_elements_by_xpath("//select[@id='cid1_machineType']//option"))
                noFirstRandomClick(driver.find_elements_by_xpath("//select[@id='cid1_model']//option"))
            WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//input[@id='saveBase']")).click()
            waitloadmask(driver)
            assertErr(driver, "新增售货机")
        except Exception as e:
            print(e)
            logPrint("ERROR：新增售货机可能出现问题")