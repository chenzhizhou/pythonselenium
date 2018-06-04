# -*- coding:utf-8 -*-
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from defAssist import waitloadmask, assertErr, navigationBarClick, logPrint

chromedriverpath = '.\\libs\\chromedriver.exe'
runlogpath = '.runlog.log'
try:
    os.remove(runlogpath)
except:
    pass
file = open(runlogpath,'wb')


chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')

driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriverpath)
driver.set_window_size(1024, 768)
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

navigationBarClick(driver, '地图模式')
waitloadmask(driver)
assertErr(driver, '地图模式')

# navigationBarClick(driver, '售货机-售货机管理')
# waitloadmask(driver)
# assertErr(driver, '售货机管理')
# WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//a[text()='已删除售货机列表']")).click()
# logPrint('进入页面 '+ '已删除售货机列表')
# waitloadmask(driver)
# assertErr(driver, '已删除售货机列表')

navigationBarClick(driver, '点位-区域管理')
waitloadmask(driver)
assertErr(driver, '区域管理')

navigationBarClick(driver, '点位-线路管理')
waitloadmask(driver)
assertErr(driver, '线路管理')

navigationBarClick(driver, '点位-点位管理')
waitloadmask(driver)
assertErr(driver, '点位管理')

navigationBarClick(driver, '售货机-售货机管理')
waitloadmask(driver)
assertErr(driver, '售货机管理')

WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//a[text()='未认证售货机列表']")).click()
logPrint('进入页面 ' + '未认证售货机列表')
waitloadmask(driver)
assertErr(driver, '未认证售货机列表')

WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//a[text()='已删除售货机列表']")).click()
logPrint('进入页面 ' + '已删除售货机列表')
waitloadmask(driver)
assertErr(driver, '已删除售货机列表')

navigationBarClick(driver, '售货机-配货管理-货道管理')
waitloadmask(driver)
assertErr(driver, '货道管理')

navigationBarClick(driver, '售货机-配货管理-货道模板')
waitloadmask(driver)
assertErr(driver, '货道模板')

navigationBarClick(driver, '售货机-配货管理-在售商品')
waitloadmask(driver)
assertErr(driver, '在售商品')

navigationBarClick(driver, '售货机-机型管理')
waitloadmask(driver)
assertErr(driver, '机型管理')

navigationBarClick(driver, '售货机-工控机-设备列表')
waitloadmask(driver)
assertErr(driver, '设备列表')

navigationBarClick(driver, '售货机-工控机-远程升级')
waitloadmask(driver)
assertErr(driver, '远程升级')

WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//a[text()='升级任务列表']")).click()
logPrint('进入页面 ' + '升级任务列表')
waitloadmask(driver)
assertErr(driver, '升级任务列表')

navigationBarClick(driver, '售货机-工控机-在线统计')
waitloadmask(driver)
assertErr(driver, '在线统计')

WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//a[text()='在线统计曲线']")).click()
logPrint('进入页面 ' + '在线统计曲线')
waitloadmask(driver)
assertErr(driver, '在线统计曲线')

navigationBarClick(driver, '售货机-工控机-流量统计')
waitloadmask(driver)
assertErr(driver, '流量统计')

WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//a[text()='流量统计曲线']")).click()
logPrint('进入页面 ' + '流量统计曲线')
waitloadmask(driver)
assertErr(driver, '流量统计曲线')

navigationBarClick(driver, '售货机-工控机-信号统计')
waitloadmask(driver)
assertErr(driver, '信号统计')

navigationBarClick(driver, '售货机-优化工具-售货机优化')
waitloadmask(driver)
assertErr(driver, '售货机优化')

navigationBarClick(driver, '售货机-优化工具-货道优化')
waitloadmask(driver)
assertErr(driver, '货道优化')

navigationBarClick(driver, '售货机-优化工具-商品优化')
waitloadmask(driver)
assertErr(driver, '商品优化')

navigationBarClick(driver, '商品-商品中心')
waitloadmask(driver)
assertErr(driver, '商品中心')

navigationBarClick(driver, '统计-数据分析-交易汇总')
waitloadmask(driver)
assertErr(driver, '交易汇总')

navigationBarClick(driver, '统计-数据分析-优惠活动汇总')
waitloadmask(driver)
assertErr(driver, '优惠活动汇总')

navigationBarClick(driver, '统计-数据分析-畅销时间图表')
waitloadmask(driver)
assertErr(driver, '畅销时间图表')

navigationBarClick(driver, '统计-数据分析-畅销商品')
waitloadmask(driver)
assertErr(driver, '畅销商品')

navigationBarClick(driver, '统计-数据分析-畅销点位')
waitloadmask(driver)
assertErr(driver, '畅销点位')

navigationBarClick(driver, '统计-数据分析-畅销线路')
waitloadmask(driver)
assertErr(driver, '畅销线路')

navigationBarClick(driver, '统计-交易流水-交易明细')
waitloadmask(driver)
assertErr(driver, '交易明细')

navigationBarClick(driver, '统计-报表中心-线路销售额汇总')
waitloadmask(driver)
assertErr(driver, '线路销售额汇总')

navigationBarClick(driver, '统计-报表中心-点位销售额汇总')
waitloadmask(driver)
assertErr(driver, '点位销售额汇总')

navigationBarClick(driver, '统计-报表中心-售货机时间段统计')
waitloadmask(driver)
assertErr(driver, '售货机时间段统计')

navigationBarClick(driver, '统计-报表中心-商品时间段统计')
waitloadmask(driver)
assertErr(driver, '商品时间段统计')

navigationBarClick(driver, '统计-报表中心-在售商品统计')
waitloadmask(driver)
assertErr(driver, '在售商品统计')

navigationBarClick(driver, '统计-报表下载')
waitloadmask(driver)
assertErr(driver, '报表下载')

navigationBarClick(driver, '补货-补货管理')
waitloadmask(driver)
assertErr(driver, '补货管理')

WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//a[text()='领货清单列表']")).click()
logPrint('进入页面 ' + '领货清单列表')
waitloadmask(driver)
assertErr(driver, '领货清单列表')

navigationBarClick(driver, '补货-出库管理')
waitloadmask(driver)
assertErr(driver, '出库管理')

navigationBarClick(driver, '补货-补货记录')
waitloadmask(driver)
assertErr(driver, '补货记录')

navigationBarClick(driver, '对账-补货对账')
waitloadmask(driver)
assertErr(driver, '补货对账')

WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//a[text()='线路虚拟补货对账列表']")).click()
logPrint('进入页面 ' + '线路虚拟补货对账列表')
waitloadmask(driver)
assertErr(driver, '线路虚拟补货对账列表')

navigationBarClick(driver, '告警-告警列表')
waitloadmask(driver)
assertErr(driver, '告警列表')

navigationBarClick(driver, '告警-事件列表')
waitloadmask(driver)
assertErr(driver, '事件列表')

navigationBarClick(driver, '增值服务-广告-媒体库')
waitloadmask(driver)
assertErr(driver, '媒体库')

navigationBarClick(driver, '增值服务-广告-售货机广告')
waitloadmask(driver)
assertErr(driver, '售货机广告')

WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//a[text()='广告任务列表']")).click()
logPrint('进入页面 ' + '广告任务列表')
waitloadmask(driver)
assertErr(driver, '广告任务列表')

navigationBarClick(driver, '增值服务-促销活动-游戏抽奖')
waitloadmask(driver)
assertErr(driver, '游戏抽奖')

navigationBarClick(driver, '增值服务-促销活动-优惠打折')
waitloadmask(driver)
assertErr(driver, '优惠打折')

navigationBarClick(driver, '增值服务-促销活动-自定义取货码')
waitloadmask(driver)
assertErr(driver, '自定义取货码')

navigationBarClick(driver, '系统-权限分配-角色管理')
waitloadmask(driver)
assertErr(driver, '角色管理')

navigationBarClick(driver, '系统-权限分配-用户管理')
waitloadmask(driver)
assertErr(driver, '用户管理')

navigationBarClick(driver, '系统-支付配置-微信')
waitloadmask(driver)
assertErr(driver, '微信')

navigationBarClick(driver, '系统-支付配置-支付宝')
waitloadmask(driver)
assertErr(driver, '支付宝')

navigationBarClick(driver, '系统-支付配置-百度钱包')
waitloadmask(driver)
assertErr(driver, '百度钱包')

navigationBarClick(driver, '系统-支付配置-翼支付')
waitloadmask(driver)
assertErr(driver, '翼支付')

navigationBarClick(driver, '系统-支付配置-京东钱包')
waitloadmask(driver)
assertErr(driver, '京东钱包')

navigationBarClick(driver, '系统-支付配置-会员支付')
waitloadmask(driver)
assertErr(driver, '会员支付')

navigationBarClick(driver, '系统-支付配置-银联支付')
waitloadmask(driver)
assertErr(driver, '银联支付')

navigationBarClick(driver, '系统-支付配置-聚合支付')
waitloadmask(driver)
assertErr(driver, '聚合支付')

navigationBarClick(driver, '系统-支付配置-融e联')
waitloadmask(driver)
assertErr(driver, '融e联')

navigationBarClick(driver, '系统-支付配置-龙支付')
waitloadmask(driver)
assertErr(driver, '龙支付')

navigationBarClick(driver, '系统-支付配置-壹钱包')
waitloadmask(driver)
assertErr(driver, '壹钱包')

navigationBarClick(driver, '系统-支付配置-盒马反扫')
waitloadmask(driver)
assertErr(driver, '盒马反扫')

navigationBarClick(driver, '系统-支付配置-沃支付')
waitloadmask(driver)
assertErr(driver, '沃支付')

navigationBarClick(driver, '系统-支付配置-自定义支付方式')
waitloadmask(driver)
assertErr(driver, '自定义支付方式')

navigationBarClick(driver, '系统-批量配置支付方式')
waitloadmask(driver)
assertErr(driver, '批量配置支付方式')

navigationBarClick(driver, '系统-开发配置')
waitloadmask(driver)
assertErr(driver, '开发配置')

navigationBarClick(driver, '系统-流量配置')
waitloadmask(driver)
assertErr(driver, '流量配置')

navigationBarClick(driver, '系统-微信绑定')
waitloadmask(driver)
assertErr(driver, '微信绑定')

WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//a[text()='公众号绑定']")).click()
logPrint('进入页面 ' + '公众号绑定')
waitloadmask(driver)
assertErr(driver, '公众号绑定')


navigationBarClick(driver, '系统-操作日志')
waitloadmask(driver)
assertErr(driver, '操作日志')

navigationBarClick(driver, '系统-账单-未付账单')
waitloadmask(driver)
assertErr(driver, '未付账单')

navigationBarClick(driver, '系统-账单-所有账单')
waitloadmask(driver)
assertErr(driver, '所有账单')

navigationBarClick(driver, '系统-账单-收费标准')
waitloadmask(driver)
assertErr(driver, '收费标准')

navigationBarClick(driver, '系统-帮助文档')
waitloadmask(driver)
assertErr(driver, '帮助文档')

navigationBarClick(driver, '系统-关于平台')
waitloadmask(driver)
assertErr(driver, '关于平台')

# driver.close()