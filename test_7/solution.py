import numpy as np 
import matplotlib.pyplot as plt
import math

def drawTriangle(a, b, c, color):
    X = np.array([a, b, c])
    Y = [color] * 3

    plt.figure()
    plt.scatter(X[:, 0], X[:, 1], s = 170, color = Y[:])

    t1 = plt.Polygon(X[:3,:], color=Y[0])
    plt.gca().add_patch(t1)

def drawLine(a, b):
    x_values = [a[0], b[0]]
    y_values = [a[1], b[1]]
    plt.plot(x_values, y_values)


def getRadianCoord(circle_center, radius, angle):
    radian_angle = math.radians(angle)
    x = circle_center[0] + radius * math.sin(radian_angle)
    y = circle_center[1] - radius * math.cos(radian_angle)  
    return [x, y]
        
def point(coords, cor, size): 
    plt.plot(coords[0], coords[1], marker="o", markersize=size, markeredgecolor=cor, markerfacecolor="green")

def isLineColiding(a, b):
    if a[0] >= b[0] and a[1] <= b[1]:
        return True
    return False

def get_intersection(a, b):
    xxx = (a[0][0] - a[1][0], b[0][0] - b[1][0])
    yyy = (a[0][1] - a[1][1], b[0][1] - b[1][1])

    det = lambda a, b: a[0] * b[1] - a[1] * b[0]
    
    div = det(xxx, yyy)
    if div == 0: return False

    d = (det(*a), det(*b))
    x = det(d, xxx) / div
    y = det(d, yyy) / div
    return x, y

def get_distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def solution(dimensions, your_position, trainer_position, distance):
    # Characters positions
    plt.plot(trainer_position[0], trainer_position[1],'ro', color='blue')     
    plt.plot(your_position[0], your_position[1],'ro', color='red')     

    # room vectors 
    bottom_left = [0, 0]
    top_left = [0, 2]
    bottom_right = [3, 0]
    top_right = [3, 2]

    # render room 
    drawLine(bottom_left, bottom_right)
    drawLine(top_left, top_right)
    drawLine(top_left, bottom_left)
    drawLine(top_right, bottom_right)
    
    def trigger_gun(start, angle):
        for r in range(0, 4):
            coords = getRadianCoord(start, r, angle)

            is_coliding_bottom = isLineColiding([start, coords], [bottom_left, bottom_right])
            is_coliding_left = isLineColiding([bottom_left, bottom_right], [start, coords])

            if is_coliding_bottom:
                intersection = get_intersection([start, coords], [bottom_left, bottom_right])
                print("aqui")
                if intersection:
                    drawLine(start, intersection)
                    return intersection
                point(coords, 'red', 1)
        return False
    
    trigger_gun(your_position, 10)
    

    plt.show()




solution([3,2], [1,1], [2,1], 4)









 