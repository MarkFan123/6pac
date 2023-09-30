# You can modify this file to implement your own algorithm

from constants import *



def check(grid):
    for i in grid:
        for j in i:
            if(j == 'c'):
                return 1
    return 2
"""
# o = normal pellet, e = empty space, O = power pellet, c = cherry position
# I = wall, n = ghost chambers
"""
def turndetect(grid):
    t=0
    turns=[]
    for i in range(len(grid)-1):
        for j in range(len(grid[0])-1):
            if(grid[i][j] == o):
                if(grid[i+1][j] == o):
                    t+=1
                if(grid[i-1][j] == o):
                    t+=1
                if(grid[i][j+1] == o):
                    t+=1
                if(grid[i][j-1] == o):
                    t+=1
            if( t>=3):
                turns.append((i,j))
            t=0
    return turns

class TreeNode:
    def __init__(self, data=None, left=None, right=None, up=None, down=None):
        self.data = data  # 数据域的值
        self.left = left  # 左孩子的指针
        self.right = right  # 右孩子的指针
        self.up = up
        self.down = down

class Tree:
    def __init__(self, root=None):
        self.root = root  # 二叉树的根节点

def path(start, end):
    pathtree = Tree()
    pathtree.root = TreeNode()
    pathtree.root.data = start
    root = pathtree.root
    node = pathtree.root
    iterations = 0
    plan(node, root, end, iterations)


def plan(map, node, root, end, iteration):
    iteration += 1
    if iteration > 5:
        return
    if node.data[0] == end[0] and node.data[1] == end[1]:
        return
    if map[node.data[0]+1][node.data[1]] == 0:
        node.left = TreeNode()
        node.left.data = [node.data[0]+1, node.data[1]]
        node = node.left
        plan(map,node, root, end, iteration)

    if map[node.data[0]-1][node.data[1]] == 0:
        node.right = TreeNode()
        node.right.data = [node.data[0]-1, node.data[1]]
        node = node.right
        plan(map,node, root, end, iteration)

    if map[node.data[0]][node.data[1]+1] == 0:
        node.up = TreeNode()
        node.up.data = [node.data[0], node.data[1]+1]
        node = node.up
        plan(map,node, root, end, iteration)

    if map[node.data[0]][node.data[1]-1] == 0:
        node.down = TreeNode()
        node.down.data = [node.data[0], node.data[1]-1]
        node = node.down
        plan(map,node, root, end, iteration)
    return
    
    

def get_next_coordinate(grid, location):
    print(turndetect(grid))
    
    return location

def close(map, location):
    go=[]
    x=location[0]
    y=location[1]
    for j in range(1,1000):
        
        if(map[x+1][y] == o):
            go.append((x+1,y))
            break
        if(map[x-1][y] == o):
            go.append((x-1,y))
            break
        if(map[x][y+1] == o):
            go.append((x,y+1))
            break
        if(map[x][y-1] == o):
            go.append((x,y-1))
            break
        
        map[x][y]=100
        if(map[x+1][y] == e):
            x=x+1
            go.append((x,y))
            continue
        if(map[x][y+1] == e):
            y=y+1
            go.append((x,y))
            continue
        if(map[x-1][y] == e):
            x=x-1
            go.append((x,y))
            continue
        if(map[x][y-1] == e):
            y=y-1
            go.append((x,y))
            continue
    return go



def get_next_coordinate(grid, location):
    map=grid
    way=close(map, location)

    return way 

