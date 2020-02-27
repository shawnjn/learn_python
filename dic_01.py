#2020年2月27日再次学习字典使用；

def build_names(first_name, last_name, age = ''):
    person = {'name'+ first_name:first_name, last_name:last_name}
    if age:
        person['age'+age] = age     
    return person

names = {}
name01 = build_names('abs', 'gfd', age='27')
name02 = build_names("tyu", 'GFD', age='000')
names.update(name01)
# print(names)
names.update(name02)            #关键字相同时，使用会替换
print(names)
