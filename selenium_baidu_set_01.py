from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome(r'/Users/midou/Desktop/chromedriver')
driver.get('https://www.baidu.com')
driver.implicitly_wait(5)                              #查找时防止网速问题影响查找结果；5s（每0。5秒扫描一次，仅作用与driver.

'''设置搜索显示条数  50条,注意期间延时'''
ActionChains(driver).move_to_element(driver.find_element_by_link_text('设置')).perform()  #鼠标移动到'设置'
# time.sleep(2)
driver.find_element_by_class_name('setpref').click()
time.sleep(2)
Select(driver.find_element_by_name('NR')).select_by_value('50')  #选择每页显示50条；select无法使用driver.implicitly_wait(5)
print(len(Select(driver.find_element_by_name('NR')).options))

driver.find_element_by_css_selector('div >.prefpanelgo').click() #由于没有id使用css对class属性进行定位

driver.switch_to.alert.accept()
