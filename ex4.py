# _*_ coding:utf-8 _*_
#车的数量
cars = 100
#车的空间
space_in_a_car = 4.0
#司机的数量
drivers = 30
#乘客的数量
passengers = 90
#没有开的车的数量是车数减去司机数
cars_not_driven = cars - drivers
#开了的车的数量是司机的数量
cars_driven = drivers
#车的总容量
carpool_capacity = cars_driven * space_in_a_car
#平均每辆车几位乘客
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."



#附加练习
#错误信息是因为多写了一个下划线
#用了浮点数