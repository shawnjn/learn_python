#2020年3月2日
#在圆周率中找自己生日，并且告诉所在位置
# filename = 'pi_digits.txt'


filename = 'pi_00000000001到00100000000.txt'     #pi是1亿位
with open(filename) as file_object:
    lines = file_object.readlines()             #将从文件中读出的每行存储到列表中，将列表内容赋值给lines
    # print(len(lines))                   #检查列表内容数量
    # # contents = file_object.read()
    # for line in file_object:
    #     print(line.rstrip())
    # print(contents)
    # print(contents.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.strip()
    # print(line.rstrip())         #rstrip（）函数删除末尾空格；
# print(pi_string)
# print(pi_string[:10] + '...')
# print(len(pi_string))

brithday = input('请输入生日（格式：yymmdd）:')
if brithday in pi_string:                                    #成员运算符 - 如果字符串中包含给定的字符返回 True
    str_where = pi_string.find(brithday)                     #如果包含子字符串返回开始的索引值，否则返回-1
    print(f'你的生日{brithday}在pi中,在pi中的{str_where}位')
else:
    print('你的生日不再pi中')
