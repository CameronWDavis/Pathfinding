import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import time
import matplotlib.animation as animation
import matplotlib.path as mpath

mpl.use('TkAgg')
from utils import *
from grid import *
from algorithms import *

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




def isIllegal(epolygons,point):
    grid = [[0 for _ in range(50)] for _ in range(50)] #creates a 50 by 50 graph
    for i in range(len(epolygons)):
        polygon = [(point.x, point.y) for point in epolygons[i]]
        path = mpath.Path(polygon)
        inside = path.contains_points([[point.x,point.y]], radius=-0.1)
        for j in range(len(polygon)):
            if inside:
                return True
    return  False







if __name__ == "__main__":
    epolygons = gen_polygons('TestingGrid/world1_enclosures.txt')
    tpolygons = gen_polygons('TestingGrid/world1_turfs.txt')

    source = Point(8,10)
    dest = Point(43,45)


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
            draw_line(ax, [polygon[i].x, polygon[(i+1)%len(polygon)].x], [polygon[i].y, polygon[(i+1)%len(polygon)].y])
    
    # Draw turf polygons
    for polygon in tpolygons:
        for p in polygon:
            draw_green_point(ax, p.x, p.y)
    for polygon in tpolygons:
        for i in range(0, len(polygon)):
            draw_green_line(ax, [polygon[i].x, polygon[(i+1)%len(polygon)].x], [polygon[i].y, polygon[(i+1)%len(polygon)].y])


        #### Here call your search to compute and collect res_path
        badPoints = []
        for x in range(50):
            for y in range(50):
                p = Point(x,y)
                bad = isIllegal(epolygons,p)
                if bad is True:
                     badPoints.append(p)

        for p in badPoints:
         print(p)




        res_path = [source, Point(26, 17), Point(27, 17),
                    Point(28, 17), Point(28, 18), Point(28, 19), dest]

        #res_path = breadthFirstSearch(source,dest,badPoints)


        for i in range(len(res_path) - 1):
            draw_result_line(ax, [res_path[i].x, res_path[i + 1].x], [res_path[i].y, res_path[i + 1].y])
            plt.pause(0.1)

        plt.show()


