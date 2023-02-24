import math

from utils import *
from search import *

def clearPath(node,reached):
    path = []
    path.append(node)
    current = reached[node.to_tuple()]
    while current:
        path.append(current)
        current = reached[current.to_tuple()]
    path.reverse()
    return path
'''
This is my algorithm for Breadth First Search 
Arguments are two points source and destination and the illegal argument for 
shapes it cannot get into
'''

def breadthFirstSearch(source,destination,isIllegal):
    current = source
    if(current == destination):
        return current
    frontier = Queue()
    frontier.push(current)
    reached = {current.to_tuple() : None}
    while frontier:
        current = frontier.pop()
        for child in expand(current, isIllegal):
            if child.to_tuple() not in reached:
                reached[child.to_tuple()] = current
                frontier.push(child)
            if child == destination:
                return clearPath(child, reached)
    return None


'''
This is my algorithm for Greedy Breadth First,
The algorithms heuristic is a straight line distance from the current point to the end point
This is put in a priority que where highest priority is popped first 
'''
def gbfs(source,destination,isIllegal):
    current = source
    if (current == destination):
        return current
    frontier = PriorityQueue()
    frontier.push(current,0)
    reached = {current.to_tuple(): None}
    while frontier:
        current = frontier.pop()
        for child in expand(current, isIllegal):
            if child.to_tuple() not in reached:
                reached[child.to_tuple()] = current
                lineDistance = sld(child,destination)
                frontier.push(child, lineDistance)
            if child == destination:
                return clearPath(child, reached)
    return None

"""
This is my depth First algorithm 
"""
def depthFirstSearch(source,destination,isIllegal):
    current = source
    if (current == destination):
        return current
    frontier = Stack()
    frontier.push(current)
    reached = {current.to_tuple(): None}
    while frontier:
        current = frontier.pop()
        for child in expand(current, isIllegal):
            if child.to_tuple() not in reached:
                reached[child.to_tuple()] = current
                frontier.push(child)
            if child == destination:
                return clearPath(child, reached)
    return None

"""
This is my A* function that is used to generate  a path using a heuristic and a cost
"""
def aStar(source,destination,isIllegal,isCost):
    current = source
    if (current == destination):
        return current
    frontier = PriorityQueue()
    frontier.push(current, 0)
    reached = {current.to_tuple(): None}
    cost = {current.to_tuple(): 1}
    while frontier:
        current = frontier.pop()
        for child in expand(current, isIllegal):
            new_cost = cost[current.to_tuple()] + costCalc(current,isCost)
            if child.to_tuple() not in reached or new_cost < cost[child.to_tuple()]:
                cost[child.to_tuple()] = new_cost
                reached[child.to_tuple()] = current
                straightlineDistance = new_cost + sld(child,destination)
                frontier.push(child, straightlineDistance)
            if child == destination:
                return clearPath(child, reached)
    return None


#this calculates move cost with turf generation
def costCalc(source,shapeArray):
    if source in shapeArray:
        cost = 1.5
    else:
        cost = 1.0
    return cost



def sld(child,destination):
   return math.sqrt((destination.x - child.x) ** 2 + (destination.y - child.y) ** 2)

#function to expand all the nodes of the given path
def expand(point,isIllegal):
    nodes =[]
    #to refactor code remove point constructor
    up = Point(point.x, point.y + 1)
    right = Point(point.x + 1, point.y)
    down = Point(point.x,point.y - 1)
    left = Point(point.x - 1, point.y)
    #making sure points are legal before we add to path
    if up not in isIllegal:
        if up.x > -1 and up.x < 50:
            if up.y > -1 and up.y < 50:
                nodes.append(up)
    if right not in isIllegal:
        if right.x > -1 and right.x < 50:
            if right.y > -1 and right.y < 50:
                nodes.append(right)
    if down not in isIllegal:
        if down.x > -1 and down.x < 50:
            if down.y > -1 and down.y < 50:
                nodes.append(down)
    if left not in isIllegal:
        if left.x > -1 and left.x < 50:
            if left.y > -1 and left.y < 50:
                nodes.append(left)
    return nodes


