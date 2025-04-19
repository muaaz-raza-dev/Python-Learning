import matplotlib.pyplot as pt 
import numpy as np 
import math as mt
# Line 

# x = [n for n in range(10) if n % 2 ==0]
# # y = mx + c 
# slope = 2
# intercept = 2
# y = list(map(lambda x: x*slope+intercept , x))


# pt.plot(x,y, marker='o', linestyle='--', color='b')
# pt.grid(True)
# pt.title("My First Graph")
# pt.xlabel("X-axis")
# pt.ylabel("Y-axis")
# pt.show()

#  Circle 

radius = 50
x=range (-50,51)
def Circle_Cordinates(X):
  cordinates = []
  for x in X :
    y_squared =  radius**2-x**2 
    if y_squared >= 0:
        y = mt.sqrt(y_squared)
        cordinates.append((x, y))
        cordinates.append((x, -y))
  return  cordinates
circle = Circle_Cordinates(x)

x, y = zip(*circle)

pt.plot(x, y, 'bo', markersize=2,linestyle="-",color="g")
pt.axis('equal')
pt.grid(True)

pt.title("Circle")
pt.xlabel("X")
pt.ylabel("Y")
pt.show()