#2020年3月2日
#学习通过json创建数据（记录1个数据）及建立json文件
#python 3.72

import json
filename = 'UsNames.json'
flag = 1
try:
    with open(filename) as file_object:
        usernames = json.load(file_object)
except FileNotFoundError:
    print("Can't find the UsNames.json file!")
    '''如果没有该数据文件是否需要创建空数据'''
    creat_data = input('抱歉，初次运行无数据库，是否需要创建, y / n').lower()
    if creat_data == 'y':
        numbers =''
        filename = 'UsNames.json'
        with open(filename, 'w') as file_object:
            json.dump(numbers, file_object)
            flag = 0
            print('UsName.json 文件创建完成！')
    else: pass

'''第一次运行程序，由于无UsName.json文件回导致username未定义情况，因此增加了flag，让程序无json文件，第一次运行创建'''
if flag == 0:
    print('请重新运行程序，谢谢！')
    pass
else:
    username = input("What's your name?")
    if username in usernames:
        print(f'Welcome back {username} !')
    else:
        with open(filename, 'w') as file_object:
            json.dump(username, file_object)
            print(f"We'll remenber you when you come back,{username}!")
