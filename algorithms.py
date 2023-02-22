from utils import *
def breadthFirstSearch(source,destination,isIllegal):
    node = source;
    if node is destination:
        return node
    frontier = Queue()
    frontier.push(node)
    reached = [node]
    greaterThan = {node : None}
    while not frontier.isEmpty():
        node = frontier.pop()
        for child in expand(node,isIllegal):
            if child not in greaterThan.keys():
                greaterThan[child] = node
            if (child == destination):
                return child
            if child not in reached:
                reached.append(child)
                frontier.push(child)
    return None





def expand(point,isIllegal):
    node = point
    node = [node.x + 1, node.y + 1]
    if node in isIllegal:
        expand(node, isIllegal)
    else:return node




