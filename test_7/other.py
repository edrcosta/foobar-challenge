#!/usr/bin/python
# -*- coding: utf-8 -*-
# import numpy as np
# import matplotlib.pyplot as plt

import math


# def drawTriangle(a, b, c, color):
#     X = np.array([a, b, c])
#     Y = [color] * 3

#     plt.figure()
#     plt.scatter(X[:, 0], X[:, 1], s = 170, color = Y[:])

#     t1 = plt.Polygon(X[:3,:], color=Y[0])
#     plt.gca().add_patch(t1)

# def drawLine(a, b):
#     x_values = [a[0], b[0]]
#     y_values = [a[1], b[1]]
#     plt.plot(x_values, y_values)

# def point(coords, cor, size):
#     plt.plot(coords[0], coords[1], marker="o", markersize=size, markeredgecolor=cor, markerfacecolor="green")

def get_mirror_coordinates(
    size,
    pos,
    rel_cg,
    distance_count,
    ):
    [w, h] = size
    [px, py] = pos
    xr = (w - px) * 2
    xl = px * 2

    x = [px - rel_cg[0]] * (distance_count * 2 + 1)

    for i in range(distance_count + 1, distance_count * 2 + 1):
        x[i] = (x[i - 1] + xr if (i - distance_count - 1) % 2 == 0 else x[i - 1] + xl)

    for i in range(distance_count - 1, -1, -1):
        x[i] = (x[i + 1] - xl if (distance_count - 1 - i) % 2 == 0 else x[i + 1] - xr)

    dyU = (h - py) * 2
    dyD = py * 2
    y = [py - rel_cg[1]] * (distance_count * 2 + 1)

    for i in range(distance_count + 1, distance_count * 2 + 1):
        y[i] = (y[i - 1] + dyU if (i - distance_count - 1) % 2 == 0 else y[i - 1] + dyD)

        for i in range(distance_count - 1, -1, -1):
            y[i] = (y[i + 1] - dyD if (distance_count - 1 - i) % 2 == 0 else y[i + 1] - dyU)

    return (x, y)


def solution(
    dimensions,
    your_position,
    trainer_position,
    distance,
    ):
    min_d = min(dimensions)
    distance_count = distance // min_d + 1

    (px, py) = get_mirror_coordinates(dimensions, your_position,
            your_position, distance_count)
    (tx, ty) = get_mirror_coordinates(dimensions, trainer_position,
            your_position, distance_count)

    angle_dist = {}
    for _x in px:
        for _y in py:
            if _x == 0 and _y == 0:
                continue

            d = math.hypot(_y, _x)

            if d <= distance:
                beam = math.atan2(_y, _x)
                if beam in angle_dist:
                    if d < angle_dist[beam]:
                        angle_dist[beam] = d
                else:
                    angle_dist[beam] = d

    res = set()
    for _x in tx:
        for _y in ty:
            d = math.hypot(_y, _x)
            if d <= distance:
                beam = math.atan2(_y, _x)
                if beam in angle_dist:
                    if d < angle_dist[beam]:
                        angle_dist[beam] = d
                        res.add(beam)
                else:
                    angle_dist[beam] = d
                    res.add(beam)
    return len(res)


# print solution([3, 2], [1, 1], [2, 1], 4)

# print(solution([300,275], [150,150], [185,100], 500))
# print(solution([2,5], [1,2], [1,4], 11))
# print(solution([10,10], [4,4], [3,3], 5000))
