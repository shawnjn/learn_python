#2020年2月29日
#再次学习Class类

class Car():
    def __init__(self, make, modle, year):
        self.make = make
        self.modle = modle
        self.year = year
        self.odometer_reading = 30       #方法1：设置初始值（第1次初始化）

    def get_discriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.modle
        return long_name.title()

    def red_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):   #方法3-1
        '''增加防止调小obometer_reading'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back the odometer!")

my_new_car = Car('audi', 'a4', 2016)    #实例

my_new_car.odometer_reading = 33      #方法2：在实例中找到obmeter_reding的数字;这里可以相当于再次初始化里程（第2次）
my_new_car.update_odometer(25)        #方法3-2：类中设置专用函数进行调节；
my_new_car.red_odometer()
print(my_new_car.get_discriptive_name())
