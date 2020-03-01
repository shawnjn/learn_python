#2020年3月1日
#再次学习Class类；子类继承等

class Car():
    def __init__(self, make, modle, year):
        self.make = make
        self.modle = modle
        self.year = year
        self.odometer_reading = 0      #方法1：设置初始值（第1次初始化）;设置初始值的属性可以不再__init__()内提供形参

    def get_discriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.modle
        return long_name.title()

    def red_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):   #方法3-1【通过方法修改属性值】
        '''增加防止调小obometer_reading'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back the odometer!")
    def increment_odometer(self, miles):
        '''将里程表读书增加指定的量'''
        self.odometer_reading += miles
    def fill_gas_tank(self):
        print("this car need a 120L gas tank!")

'''编写Car 的ElectricCar子类'''
class ElectricCar(Car):         #父类必须在子类前，指定必须父类Car
    def __init__(self, make, modle, year):      #必须初始化父类形参
        '''初始化父类属性'''
        super().__init__(make, modle, year)     #super（）函数，将父类与子类连接起来，并初始化父类属性
        self.battery = Battery()                #Battery()是新增的Battery类
    '''在子类中可以对父类中的方法进行修改'''
    def fill_gas_tank(self):
        print("this car does'n need a gas tank!")

'''新增battery类'''
class Battery():
    '''初始化'''
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size
    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-KWh battery.')
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = 'This car can go approximately ' + str(range)     #输出文字的一种方法
        message += ' miles on a full charge.'
        print(message)
    def upgrade_battery(self):      #该方法相当于升级电池
        if self.battery_size != 85:
            self.battery_size = 85

# my_new_car = Car('audi', 'a4', 2016)    #实例
# # my_new_car.odometer_reading = 30      #方法2【直接修改属性值】：在实例中找到obmeter_reding的数字;
#                                         # 这里设置数值，相当相当于再次初始化里程（第2次）
# my_new_car.update_odometer(25)        #方法3-2【通过方法修改属性值】：类中设置专用函数进行调节；
# my_new_car.red_odometer()
# print(my_new_car.get_discriptive_name())
#
# my_used_car = Car('subaru', 'outback', 2013)
# print(my_used_car.get_discriptive_name())
#
# my_used_car.update_odometer(2300)
# my_used_car.red_odometer()
#
# my_used_car.increment_odometer(100)
# my_used_car.red_odometer()

my_tesla = ElectricCar('tesla', 'modle s', 2016)
print(my_tesla.get_discriptive_name())
my_tesla.battery.battery_size = 70     #也可进行初始化
'''查询当前电池情况'''
my_tesla.battery.describe_battery()
'''对电池进行升级'''
my_tesla.battery.upgrade_battery()
'''了解升级后信息'''
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
