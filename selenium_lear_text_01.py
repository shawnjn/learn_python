from selenium import webdriver
import time

drivrt_test = webdriver.Chrome(r'/Users/midou/Desktop/chromedriver')
drivrt_test.implicitly_wait(5)                              #查找时防止网速问题影响查找结果；5s（每0。5秒扫描一次）

drivrt_test.get('http://f.python3.vip/webauto/test1.html')

'''xpath绝对路径，/html/body/div，逐个直接子节点'''
elements = drivrt_test.find_elements_by_xpath('/html/body/div')#绝对路径 从头开始/html/body/div一层层往下
'''xpath相对路径 //div 表示：html内所有的div；//div//p,p为div的子节点；//div/p，p是div的直接子节点;//div/*：div内所有子节点
    对应css方法，div p；和  div > p'''
'''
xpath根据属性值选择，【@属性名='属性值'】，可以没有值【@属性名】
xpath示例：//*[@id = 'west'任何元素的属性id为west的；//div[@class='single_choice']
            所有div元素中属性class为single_choice的元素
            class属性有多个；xpath搜索，属性值必须全部相等
    xpath查找包含关系：//*[contains(@style,'color')] 表示任何元素属性为style包含color属性值；
                    //*[starts-with(@style,'color')] 表示任何元素属性为style以color属性值开始；
                    //*[ends-with(@style,'color')] 表示任何元素属性为style以color属性值结尾；xpath2.0才支持
                    //p[2] 表示p类型（html内所有）第2个的子元素,可以增加//div/p[2]作个父类型限制
                    //div/*[2] 表示div内（上层元素）的第2个元素
                    //div/p[last()]表示父元素为div中p类型倒数1个，last()-1表示倒数第2个p元素
                    //option[position()<=2] 选取option类型第1到2个子元素，等效//option[position()<3]
                    //*[@class='multi_choice']/*[position()<3] 选择class属性为multi_choice的前3个子元素
                    //*[@class='multi_choice']/*[position()>last()-2] 选择class属性为multi_choice的后3个子元素
                组选择，多个表达式
                    //option | //h4 表示选择所有的option元素和所有的h4元素
                        示例 //*[@class='single_chioce']|//*[@class='multi_choice']
                【xpath特殊用法】选择某个节点的父节点 /.. 可继续往上找父节点
                    //*[@id='china']/.. 表示玄子id为china的父节点
                【兄弟节点的选择】
                        following-sibling::选择后续兄弟节点
                        preceding-sibling::选择前面的兄弟节点
                    //*[@class='sigle']/following-sibling::* 所有节点class属性为single的后续所有兄弟节点，
                                                            *改为h4所有节点class属性为single的后续所有的h4兄弟节点
            【特别注意】china = wb.find_element_by_id('china')
                      elements = china.find_elements_by_xpath('//p')与elements = china.find_elements_by_xpath('.//p')
                      的区别是，前面还是在整个html内查找所有p节点元素，后程序表示在china内查找所有p节点元素
                        
                    
css对应[id = west],id特殊属性 # ，class属性 . 
    css查找包含关系：a[style*='color'] 表示a节点里面的style属性包含color字符串
                    a[style^='color'] 表示a节点里面的style属性以color字符串开始
                    a[style$='color'] 表示a节点里面的style属性以color字符串结尾
                    p:nth-of-type(2) 表示p类型（html内所有）第2个的子元素
                    option，h4 表示选择所有的option元素和所有的h4元素
                【兄弟节点选择】
                    h3+span 相邻兄弟关系
                    h3～span 选择h3后面所有的兄弟节点span
                    
'''
for element in elements:
    print('/n')
    print(element.get_attribute('outerHTML'))
time.sleep(3)
drivrt_test.quit()
