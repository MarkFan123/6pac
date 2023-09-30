# You can modify this file to implement your own algorithm

from constants import *
"""
# o = normal pellet, e = empty space, O = power pellet, c = cherry position
# I = wall, n = ghost chambers
"""
#attempt to use tree to calculate route, failed.
# #
# class TreeNode:
#     def __init__(self, data=None, left=None, right=None, up=None, down=None):
#         self.data = data  # 数据域的值
#         self.left = left  # 左孩子的指针
#         self.right = right  # 右孩子的指针
#         self.up = up
#         self.down = down


# class Tree:
#     def __init__(self, root=None):
#         self.root = root  # 二叉树的根节点

# # def shortestway(root):
# #     node=root
# #     way=[]
# #     length=0
# #     while(node != None):
# #         if


# def printtree(trial, i):
#     i += 1
#     pathtree = trial
#     #print(pathtree.data, '->')
#     if pathtree.left != None:
#         printtree(pathtree.left, i)
#     if pathtree.right != None:
#         printtree(pathtree.right, i)
#     if pathtree.up != None:
#         printtree(pathtree.up, i)
#     if pathtree.down != None:
#         printtree(pathtree.down, i)
#     return pathtree.data


# def path(map,start, end):
#     pathtree = Tree()
#     pathtree.root = TreeNode()
#     pathtree.root.data = start
#     root = pathtree.root
#     node = pathtree.root
#     iterations = 0
#     i = 0
#     if(plan(map, node, root, end, iterations) ==1 ):
#         return printtree(pathtree.root, i)
        
    
    


# def plan(map, node, root, end, iteration):
#     iteration += 1
#     if iteration > 20:
#         return
#     if map[node.data[0]+1][node.data[1]]==end:
#         node.left = TreeNode()
#         node.left.data = [node.data[0]+1, node.data[1]]
#         return 1
#     if map[node.data[0]-1][node.data[1]]==end:
#         node.left = TreeNode()
#         node.left.data = [node.data[0]-1, node.data[1]]
#         return 1
#     if map[node.data[0]][node.data[1]+1]==end:
#         node.left = TreeNode()
#         node.left.data = [node.data[0]+1, node.data[1]]
#         return 1
#     if map[node.data[0]][node.data[1]-1]==end:
#         node.left = TreeNode()
#         node.left.data = [node.data[0]+1, node.data[1]]
#         return 1
#     if map[node.data[0]+1][node.data[1]] ==e :
#         node.left = TreeNode()
#         node.left.data = [node.data[0]+1, node.data[1]]
#         map[node.data[0]][node.data[1]] = 9
#         if map[node.data[0]+1][node.data[1]]==end:
#             return
#         node = node.left
#         plan(map, node, root, end, iteration)
 

#     if map[node.data[0]-1][node.data[1]] == e:
#         node.right = TreeNode()
#         node.right.data = [node.data[0]-1, node.data[1]]
#         map[node.data[0]][node.data[1]] = 9
#         if map[node.data[0]-1][node.data[1]]==end:
#             return
#         node = node.right
#         plan(map, node, root, end, iteration)

#     if map[node.data[0]][node.data[1]+1] == e:
#         node.up = TreeNode()
#         node.up.data = [node.data[0], node.data[1]+1]
#         map[node.data[0]][node.data[1]] = 9
#         if map[node.data[0]][node.data[1]+1]==end:
#             return
#         node = node.up
#         plan(map, node, root, end, iteration)

#     if map[node.data[0]][node.data[1]-1] == e:
#         node.down = TreeNode()
#         node.down.data = [node.data[0], node.data[1]-1]
#         map[node.data[0]][node.data[1]] = 9
#         if map[node.data[0]][node.data[1]-1]==end:
#             return
#         node = node.down
#         plan(map, node, root, end, iteration)
#     return

##another failed method
def distance(map, location):
    x=location[0]
    y=location[1]
    mini=3000
    mini2=300
    for i in range(len(map)):
        for j in range(len(map[0])):
            if(map[i][j] == o):
                if(abs(i-x)<mini and i!=x):
                    mini=abs(i-x)
                    deltax=i-x
                if(abs(j-y)<mini2 and j!=y):
                    mini2=abs(j-y)
                    deltay=j-y
                    
    deltax=int(deltax/abs(deltax))
    deltay=int(deltay/abs(deltay))
    return (deltax, deltay)

def close(map, location):
    go=[]
    x=location[0]
    y=location[1]
    deltax,deltay=distance(map, location)
    
    if map[x+deltax][y] == o:
        go=(x+deltax,y)
        return go
    if map[x][y+deltay] == o:
        go=(x,y+deltay)
        return go
    if map[x+deltax][y] == o:
        go=(x+deltax,y)
        return go
    if map[x][y+deltay] == o:
        go=(x,y+deltay)
        return go
    if map[x+1][y] == o:
        go=(x+1,y)
        return go
    if map[x-1][y] == o:
        go=(x-1,y)
        return go
    if map[x][y+1] == o:
        go=(x,y+1)
        return go
    if map[x][y-1] == o:
        go=(x,y-1)
        return go
    map[x][y]==100
    d1,d2=distance(map, (x+deltax,y+deltay))
    # if d1!=(-deltax) :       
    #     if map[x+deltax][y] == e:
    #         go=(x+deltax,y)
    #         return go
    # if d2!=(-deltay) :
    #     if map[x][y+deltay] == e:
    #         go=(x,y+deltay)
    #         return go
    map[x][y]==100
    if map[x+1][y] == e:
        go=(x+1,y)
        map[x+1][y]==100
        return go
    if map[x-1][y] == e:
        go=(x-1,y)
        map[x-1][y]==100
        return go
    if map[x][y+1] == e:
        go=(x,y+1)
        map[x][y+1]==100
        return go
    if map[x][y-1] == e :
        go=(x,y-1)    
        map[x][y-1] == 100
        return go
def pather(map, location):
    go=[]
    x=location[0]
    y=location[1]
    while(1):
        
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
###if I can give out a route as a array rather than just points would be good, 
##This method genrates a route between two o points, they are not the shortest route
def get_next_coordinate(grid, location):
    map=grid
    go=pather(map, location)
    
    return go[0] 

