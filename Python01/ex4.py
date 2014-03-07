# coding=utf-8
#车辆数
cars=100
#车内空间数（座位数）
space_in_a_car=4.0
#使用数
drivers=30
#乘客数
passengers=90
# 没有行驶（使用）的车辆数
cars_not_driven=cars - drivers
#行驶（使用）的车辆数
cars_driven=drivers
# 可载人数
carpool_capacity=cars_driven * space_in_a_car
# 每辆车安排人数
average_passengers_per_car=passengers/cars_driven

print "There are", cars,"cars available."
print "There are only",drivers,"drivers available."
print "There will be",cars_not_driven, "empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "We need to put about", average_passengers_per_car,"in each car."


''' 加分练习题'''
# 错误信息的解释：文件ex4.py第8行，变量car_pool_capacity未定义
# 1. 用了 4.0 作为 space_in_a_car 的值没必要，表示车内座位数实际上使用整数就可以
