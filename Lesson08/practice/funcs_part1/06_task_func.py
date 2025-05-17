# Напишите функцию, которая проверит, что точка (x, y)
# находится строго внутри окружности с центром в точке (xc, yc)
# и радиусом r:

def point_in_circle(x, y, xc, yc, r):
    return((x-xc)**2+(y-yc)**2)**0.5 < r

x = int(input("enter value x "))
y = int(input("enter value y "))
xc  = int(input("enter value xc "))
yc  = int(input("enter value yc "))
r  = int(input("enter value r "))
print(point_in_circle(x,y,xc,yc,r))
# Не забудьте протестировать вашу функцию
