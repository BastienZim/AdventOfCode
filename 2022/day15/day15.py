'''
@author: BastienZim

'''

import os
import numpy as np
import timeit
from sympy import Interval, Union

import geopandas as gpd

from shapely.geometry import Polygon
from shapely.ops import cascaded_union, unary_union
import matplotlib.pyplot as plt

from functools import reduce

path = "/home/bastienzim/Documents/perso/adventOfCode/2022"
#path = "/home/bastien/Documents/AdventOfCode/2022"


example = False


if(example):
    global_row = 10
    search_space = 20
else:
    global_row = 2000000
    search_space = 4000000  # 4 000 000 - 4000000


def main():
    day = str(os.path.basename(__file__).split(".")[0][3:])
    if(example):
        with open(path+"/day"+day+"/example_in.txt") as f:
            input = f.readlines()
    else:
        with open(path+"/day"+day+"/input.txt") as f:
            input = f.readlines()
    input = sanitize_input(input)
    # print(input)
    sensors, beacons = [x[0] for x in input], [x[1] for x in input]

    #counter, no_beacon_pos = get_pos_no_beacon(global_row, sensors, beacons)
    # print(counter)
    # print(no_beacon_pos)

#    print(unique_beacons, uni)
    # First time = 7.187 for 10000
    # time = timeit.timeit(lambda: find_unique_pos(
    #   sensors, beacons), number=1000)
    # print(time)
    # Second time = 1.4 for 10000
    # time = timeit.timeit(lambda: find_unique_pos(
    #         sensors, beacons), number=10000)
    # print(time)
    # other func = 7.187 for 10000
    # time = timeit.timeit(lambda: get_sensor_zone(
    #    sensors, beacons), number=1000)
    # print(time)
    # other func = 0.68360 for 10000
    # time = timeit.timeit(lambda: up_down_scan(
    #   sensors, beacons), number=10000)
    # print(time)

    # print(aa)

    #(x, y), f = get_sensor_zone(sensors, beacons)
    #print(x, y, f)

    #x,y = up_down_scan(sensors, beacons)
    #print(x,y, tuning_freq(x,y))
#    print(tuning_freq(14,11))
    x,y = circles_method(sensors, beacons)
    print(x,y, tuning_freq(x,y))
    
'''
.....
..0.
. 100.
  2oooo
.  000.
..  0..
.....
0000
1111
2222
3333

0
10
210
3210
 321
  32
   3
'''


#1 circle = 2 intervals autour du centre
#ici c'est en diag

def circles_method(sensors, beacons):
    '''Not ok for immense search spaces'''
#    map = np.zeros((search_space, search_space), bool)
    #closest_b_dist = [m_dist(s, b) for s, b in zip(sensors, beacons)]
    polygons =[]
    for s, b in zip(sensors, beacons):
        d = m_dist(s, b)
        corners = [(s[0]+d, s[1]), (s[0], s[1]+d), (s[0]-d, s[1]), (s[0], s[1]-d)]
        #print(corners)
        
        polygons.append(Polygon(corners))

    all_no_beacons = gpd.GeoSeries( unary_union(polygons))
    grid = gpd.GeoSeries(Polygon([(0,0), (0,search_space), (search_space,search_space), (search_space,0)]))

    inter = grid.intersection(all_no_beacons)

    diff = grid.difference(inter)
    xx, yy = diff.geometry[0].exterior.coords.xy
    
    return((int(min(xx) + 1), int(min(yy) + 1)))
#    print(diff.geometry)
    #plt.show()

def row_col_scan(sensors, beacons):
    closest_b_dist = [m_dist(s, b) for s, b in zip(sensors, beacons)]
    unique_beacons = list(set([tuple(x) for x in beacons]))
    for i in range(search_space):
        print(i)
        
        counter_2 = get_count_no_beacon_col(
            i, sensors, closest_b_dist, unique_beacons, i+1, search_space)
        counter_1 = get_count_no_beacon(
            i, sensors, closest_b_dist, unique_beacons, i, search_space)
        #if(counter_2 < search_space+1-k-1):
        if(counter_2 < search_space-i):
            print("col->",i,i+1)
            reachs = get_each_sensor_reach_col(i, sensors, closest_b_dist)
            unio = union_intervals([x for x in reachs if x[0] < x[1]])
            if(len(unio) > 1):
                print(i, unio[0].sup)
                return(i, unio[0].sup)
        if(counter_1 < search_space+1-i):
            print("row->",i)
            reachs = get_each_sensor_reach(i, sensors, closest_b_dist)
            unio = union_intervals([x for x in reachs if x[0] < x[1]])
            if(len(unio) > 1):
                print(unio[0].sup, i)
                return(unio[0].sup, i)
            
    


def up_down_scan(sensors, beacons):
    closest_b_dist = [m_dist(s, b) for s, b in zip(sensors, beacons)]
    sensors_reach = get_each_sensor_reach(0, sensors, closest_b_dist)
    row_sensors = [elt[1] for elt in sensors]
    i_above = [i for i in range(len(sensors))]
    i_bellow = []
    for y in range(search_space):  # search_space):
        if(y % 100 == 0):
            print(y, "HERE")

        reachable = [x for x in sensors_reach if x[0] < x[1]]
        unio = union_intervals(reachable)
        if(len(unio) > 1):
            return(unio[0].sup, y)

        if(y in row_sensors):
            for i_chang in [i for i, x in enumerate(row_sensors) if x == y]:
                i_bellow.append(i_chang)
                i_above.remove(i_chang)
        for index in i_above:
            sensors_reach[index] = (
                sensors_reach[index][0]-1, sensors_reach[index][1]+1)
            # TODO: remove the ones that are too far up and that we can ignore
            # print("B",sensors_reach[index])
            # if(sensors_reach[i_above] )
        for index in i_bellow:
            sensors_reach[index] = (
                sensors_reach[index][0]+1, sensors_reach[index][1]-1)

            #print(len(bellow), len(bellow)+len(above), len(sensors))


def union_intervals(data):
    """ Union of a list of intervals e.g. [(1,2),(3,4)] """
    intervals = [Interval(begin, end) for (begin, end) in data]
    u = Union(*intervals)
    return [list(u.args[:2])] if isinstance(u, Interval) \
        else list(u.args)


def find_unique_pos(sensors, beacons):

    closest_b_dist = [m_dist(s, b) for s, b in zip(sensors, beacons)]
    unique_beacons = list(set([tuple(x) for x in beacons]))

    to_check = list(set([tuple(x) for x in sensors + beacons]))
    row_to_check = [elt[0] for elt in to_check]
    for y in range(search_space):  # row
        # if(y % 1 == 0):
        #    print(y)
        # TODO: check if this speeds up not to store the list of beacons. Speedup worse in small spaces
        counter = get_count_no_beacon(
            y, sensors, closest_b_dist, unique_beacons, 0, search_space)

#        counter, no_beacons = get_pos_no_beacon(y, sensors, closest_b_dist, unique_beacons, 0, search_space)
        if(counter < search_space+1):
            counter, no_beacons = get_pos_no_beacon(
                y, sensors, closest_b_dist, unique_beacons, 0, search_space)
            # print(y)

            if(y in row_to_check):
                to_check_row = (elt[0] for elt in to_check if elt[1] == y)
                i_to_look = (x for x in range(search_space) if (
                    x not in no_beacons and
                    x not in to_check_row))
            else:
                i_to_look = (x for x in range(search_space) if (
                    x not in no_beacons))

            for x in i_to_look:  # cols
                return(((x, y), tuning_freq(x, y)))


def tuning_freq(x, y):
    return(4000000*x + y)


def get_pos_no_beacon(row, sensors, closest_b_dist, unique_beacons, min_x, max_x):
    row_beacons_x = [b[0] for b in unique_beacons if b[1] == row]
    reachable_sensors_distance = [(s, d) for s, d in
                                  zip(sensors, closest_b_dist) if abs(s[1]-row) < d]
    counter = 0
    no_beacon_pos = []
    k_to_look = (k for k in range(min_x, max_x+1) if k not in row_beacons_x)
    for k in k_to_look:
        point = (k, row)
        for s, d_closest in reachable_sensors_distance:
            if(m_dist(point, s) <= d_closest):
                counter += 1
                no_beacon_pos.append(k)
                break
    return(counter, no_beacon_pos)


def get_count_no_beacon_col(col, sensors, closest_b_dist, unique_beacons, min_y, max_y):
    #print(f"min_y, {min_y}, max_y, {max_y}")
    col_beacons_y = [b[1] for b in unique_beacons if b[0] == col]
    reachable_sensors_distance = [(s, d) for s, d in
                                  zip(sensors, closest_b_dist) if abs(s[0]-col) < d]
    counter = 0

    if(len(col_beacons_y) > 0):
        k_to_look = (k for k in range(min_y, max_y+1)
                     if k not in col_beacons_y)
    else:
        k_to_look = (k for k in range(min_y, max_y+1))
    for k in k_to_look:
        point = (col, k)
        for s, d_closest in reachable_sensors_distance:
            if(m_dist(point, s) <= d_closest):
                counter += 1
                break
    return(counter+len(col_beacons_y))


def get_count_no_beacon(row, sensors, closest_b_dist, unique_beacons, min_x, max_x):
    row_beacons_x = [b[0] for b in unique_beacons if b[1] == row]
    reachable_sensors_distance = [(s, d) for s, d in
                                  zip(sensors, closest_b_dist) if abs(s[1]-row) < d]
    counter = 0
    if(len(row_beacons_x) > 0):
        k_to_look = (k for k in range(min_x, max_x+1)
                     if k not in row_beacons_x)
    else:
        k_to_look = (k for k in range(min_x, max_x+1))
    for k in k_to_look:
        point = (k, row)
        for s, d_closest in reachable_sensors_distance:
            if(m_dist(point, s) <= d_closest):
                counter += 1
                break
    return(counter+len(row_beacons_x))


def get_each_sensor_reach(row, sensors, closest_b_dist):
    sensors_reach = []
    for s, d in zip(sensors, closest_b_dist):
        v_dist = abs(s[1]-row)
        # if(v_dist < d):
        reach_left = s[0]-(d-v_dist)
        reach_right = s[0]+(d-v_dist)
        sensors_reach.append((reach_left, reach_right+1))
    return(sensors_reach)

def get_each_sensor_reach_col(col, sensors, closest_b_dist):
    sensors_reach = []
    for s, d in zip(sensors, closest_b_dist):
        v_dist = abs(s[0]-col)
        # if(v_dist < d):
        reach_up = s[1]-(d-v_dist)
        reach_down = s[1]+(d-v_dist)
        sensors_reach.append((reach_up, reach_down+1))
    return(sensors_reach)


def get_sensor_reach(row, sensors, closest_b_dist):

    min_x, max_x = 0, 0
    for s, d in zip(sensors, closest_b_dist):
        v_dist = abs(s[1]-row)
        if(v_dist < d):
            reach_left = s[0]-(d-v_dist)
            if(min_x > reach_left):
                min_x = reach_left

            reach_right = s[0]+(d-v_dist)
            if(max_x < reach_right):
                max_x = reach_right
    return(min_x, max_x)


def m_dist(x, y):
    return(sum([abs(a-b) for a, b in zip(x, y)]))


def get_sensor_zone(sensors, beacons):
    '''Not ok for immense search spaces'''
    map = np.zeros((search_space, search_space), bool)
    #closest_b_dist = [m_dist(s, b) for s, b in zip(sensors, beacons)]
    for s, b in zip(sensors, beacons):
        closest_dist = m_dist(s, b)
        for radius in range(0, closest_dist+1):
            vn_neighours = get_VN_neighborhood(radius, s[0], s[1])
            for n in vn_neighours:
                if(0 <= n[0] < map.shape[0] and 0 <= n[1] < map.shape[1]):
                    map[n] = 1

    # print(map.astype(int))
    x, y = np.ravel(np.where(map == False))
    return(((x, y), tuning_freq(x, y)))


def get_VN_neighborhood(radius, center_x, center_y):
    """get_Von_Neumann_neighborhood"""
    circle_pts = []
    for x in range(int(radius/2)+1):
        y = radius - x
        pts = get_circle_points(x, y, center_x, center_y)
        circle_pts = circle_pts + pts
    return(circle_pts)


def get_circle_points(x, y, center_x, center_y):
    aa = [(center_x + x, center_y + y),
          (center_x - x, center_y - y),
          (center_x + x, center_y - y),
          (center_x - x, center_y + y)]
    if x != y:
        bb = [(center_x + y, center_y + x),
              (center_x - y, center_y - x),
              (center_x + y, center_y - x),
              (center_x - y, center_y + x)]
        return(list(set(aa+bb)))
    return(list(set(aa)))


def sanitize_input(input):
    #alternative: [int(x.replace("\n","")) for x in input]
    input = list(map(lambda x: x.replace("\n", ""), input))
    clean_in = []
    for x in input:
        elts = x[10:].split(": closest beacon is at ")
        line = []
        for a in elts:
            a = a.replace("x=", "")
            a = a.replace("y=", "")
            #print([int(b) for b in a.split(", ")])
            line.append([int(b) for b in a.split(", ")])
        clean_in.append(line)
    return clean_in


if __name__ == "__main__":
    main()
