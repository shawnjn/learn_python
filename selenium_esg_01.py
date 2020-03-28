from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

'''配置chrome浏览器'''
dr = webdriver.Chrome(r'/Users/midou/Desktop/chromedriver')
dr.maximize_window()
dr.implicitly_wait(5)

'''进入网站并输入登录账号和密码'''
dr.get('http://b.esgcc.com.cn/')
username = ''
password = ''
dr.find_element_by_id('username').send_keys(username)
dr.find_element_by_id('password').send_keys(password)

'''获取验证码并输入验证码（手动）'''
text = input('请输入验证码：')     #手动输入验证码
print('你输入的验证码为：'+text)
dr.find_element_by_id('person_reg_security').send_keys(text)
dr.find_element_by_css_selector(".login_btn[value='登录']").click()
dr.find_element_by_class_name('a-link').click()
mainwindow = dr.current_window_handle       #记录原窗口handle，便于后续切回窗口时使用
# print(mainwindow)
'''跳转至指定网页'''
for handle in dr.window_handles:
    dr.switch_to.window(handle)
    if '零星采购首页' in dr.title:
        break

'''切换搜索框至"物料编码"'''
#移动到物料编码,激活点击窗口
ac = ActionChains(dr)
ac.move_to_element(dr.find_element_by_xpath('//div[@class="header_search_bar"]')).perform
dr.find_element_by_xpath('//div[@class="header_search_bar"]').click()
#使用遍历方式，在<li>列表中找到对应位置列表然后点击；
lis = dr.find_elements_by_xpath("//li[@class='item']")
for li in lis:
    # print(li.text)
    if li.text == '物料编码':
        li.click()
        break
    else:
        continue
'''获取物料编码并进行搜索'''
num = 580012252     #搜索的物料编码，后续该物料编码从excel中获取

dr.find_element_by_id('to_seach_id').send_keys(num)  #输入框输入搜索内容
dr.find_element_by_css_selector('.searchBtn').click()

'''展示搜索结果，条件比对后获获取物资连接并点击'''
#//ul[@class="product_list"]   表示搜索后所有物品的父节点
lis_items = dr.find_elements_by_xpath('//ul[@class="product_list"]/*')  #遍历所有搜索出物品
print(f'物料编码{num}搜索结果有：' +str(len(lis_items)) + '个\n')
if len(lis_items) <= 20:        #搜索结果的数量（一页20个）
    for lis_i in lis_items:     #在第1页进行查找（价格作为条件）
        print(lis_i.text)
        #获取每个物品，然后对比条件进行选择

'''采购对应数量物资，并提示下单信息'''

'''待续'''
time.sleep(10)
dr.quit()
