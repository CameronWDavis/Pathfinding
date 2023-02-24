import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import time
import matplotlib.animation as animation
import matplotlib.path as mpath

from utils import *
from grid import *
from algorithms import *
mpl.use('TkAgg')

def printMenu():
    print("Please enter the algorithm to display,")
    print("1) Breadth First Search")
    print("2) Depth First Search")
    print("3) Greedy Breadth First Search")
    print("4) A* Search")
    print("5) To exit")

def drawBoard(res_path):
    fig, ax = draw_board()
    draw_grids(ax)
    draw_source(ax, source.x, source.y)  # source point
    draw_dest(ax, dest.x, dest.y)  # destination point

    # Draw enclosure polygons
    for polygon in epolygons:
        for p in polygon:
            draw_point(ax, p.x, p.y)
    for polygon in epolygons:
        for i in range(0, len(polygon)):
            draw_line(ax, [polygon[i].x, polygon[(i + 1) % len(polygon)].x],
                      [polygon[i].y, polygon[(i + 1) % len(polygon)].y])

    # Draw turf polygons
    for polygon in tpolygons:
        for p in polygon:
            draw_green_point(ax, p.x, p.y)
    for polygon in tpolygons:
        for i in range(0, len(polygon)):
            draw_green_line(ax, [polygon[i].x, polygon[(i + 1) % len(polygon)].x],
                            [polygon[i].y, polygon[(i + 1) % len(polygon)].y])

    for i in range(len(res_path) - 1):
        draw_result_line(ax, [res_path[i].x, res_path[i + 1].x], [res_path[i].y, res_path[i + 1].y])
        plt.pause(0.1)
    plt.show()
    plt.close()

def fillArray(shapesArray):
    array = []
    polygons = [mpath.Path([(p.x, p.y) for p in shape]) for shape in shapesArray]
    for x in range(50):
        for y in range(50):
            point = Point(x, y)
            for polygon in polygons:
                if polygon.contains_point(point.to_tuple(), radius=-0.1):
                    array.append(point)
                    break
    return array

def gen_polygons(worldfilepath):
    polygons = []
    with open(worldfilepath, "r") as f:
        lines = f.readlines()
        lines = [line[:-1] for line in lines]
        for line in lines:
            polygon = []
            pts = line.split(';')
            for pt in pts:
                xy = pt.split(',')
                polygon.append(Point(int(xy[0]), int(xy[1])))
            polygons.append(polygon)
    return polygons


if __name__ == "__main__":
    #our starting shapes
    epolygons = gen_polygons('TestingGrid/world1_enclosures.txt')
    tpolygons = gen_polygons('TestingGrid/world1_turfs.txt')
    #our starting polygons
    source = Point(8, 10)
    dest = Point(43, 45)


    #creating lists of the points my algorithms need to make choices
    blockedPoints = fillArray(epolygons)
    costPoints = fillArray(tpolygons)

    searchToShow = 0

#while statement that takes in user input and draws the selected board
    while (searchToShow != 5):
        printMenu()
        searchToShow = input()
        searchToShow = int(searchToShow.strip()) #remove whitespaces because users can be bad
        match searchToShow:
            #cases to show path
            case 1:
                res_path = breadthFirstSearch(source, dest, blockedPoints)
                drawBoard(res_path)
            case 2:
                res_path = depthFirstSearch(source, dest, blockedPoints)
                drawBoard(res_path)
            case 3:
                res_path = gbfs(source, dest, blockedPoints)
                drawBoard(res_path)
            case 4:
                res_path = aStar(source, dest, blockedPoints, costPoints)
                drawBoard(res_path)
            case 5:
                print("Good bye!")
                exit()
            case _:
                print("Invalid search algorithm")
    
    
    



