# coding=utf-8
x=[7439695.07931521,13202399.4654164,-3504533.72350397,-16282945.450944,6910739.42467448]
y=[18359432.4518111,12654731.9283261,-22776742.1951248,-1270691.73493271,-15581694.9377712]
z=[-18242050.2245942,-19136436.3144384,13405348.1750206,21052945.4792735,-20210215.8550669]
# Поправка ходу годинника
t=[0.09525,0.09333,0.09058,0.08587,0.10292]
# x=[ float(input()) for _ in range(0,5)]
# y=[ float(input()) for _ in range(0,5)]
# z=[ float(input()) for _ in range(0,5)]
# t=[ float(input()) for _ in range(0,5)]
print(" K.X = {} \n K.Y = {} \n K.Z = {} \n tau = {} ".format(x,y,z,t))
# Метод "найменших квадратів"
x_new = abs(sum(x)/5)
y_new = abs(sum(y)/5)
z_new = abs(sum(z)/5)
t_new = abs(sum(t)/5)
print(" \t Our result is \n X_new = {} \n Y_new = {} \n Z_new = {} \n Tau_new = {}".format(x_new,y_new,z_new,t_new))