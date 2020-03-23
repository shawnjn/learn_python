from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from PIL import Image, ImageEnhance
import pytesseract
import time
import pyautogui

'''配置chrome浏览器'''
dr = webdriver.Chrome(r'D:\pythonlearn\chromedriver_80.0.3987.106\chromedriver.exe')
dr.maximize_window()
dr.implicitly_wait(5)

'''进入网站并输入登录账号和密码'''
dr.get('http://b.esgcc.com.cn/')
username = 'xxxxx'
password = 'xxxxx'
dr.find_element_by_id('username').send_keys(username)
dr.find_element_by_id('password').send_keys(password)

'''获取验证码并输入验证码（手动、自动）'''
text = input('请输入验证码：')     #手动输入验证码
print(text)
dr.find_element_by_id('person_reg_security').send_keys(text)
#'''自动获取、分析验证码并输入'''
# '''获取验证码照片'''
# #方案一：（通用性）截全屏后定位验证码图片位置，再裁剪存档
# dr.save_screenshot(r'E:\code_full.png')     #整个网页截图
# ActionChains(dr).move_to_element(dr.find_element_by_id(id)).perform()
# #方案二：（适用能单独获取验证码图片）
# actions = ActionChains(dr)
# actions.context_click(dr.find_element_by_id('personSecurityCode')).perform()      #鼠标右键点击，
#                                                             # 默认存储位置C:\Users\郭晓敬\Downloads\
# pyautogui.typewrite(['down', 'down', 'enter'])
# time.sleep(3)
# pyautogui.typewrite(['enter'])
# time.sleep(5)
# #获取保存的验证码照片然后（1）将照片上传其他网站验证；（2）QCR分析模块进行识别，如 pytesseract、 tesseract、 tesseract-ocr；
#
dr.find_element_by_css_selector(".login_btn[value='登录']").click()
dr.find_element_by_class_name('a-link').click()


# time.sleep(5)
# dr.quit()
