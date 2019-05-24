"""
迷宫问题
题目

用一个二维数组表示一个简单的迷宫，用0表示通路，用1表示阻断，老鼠在每个点上可以移动相邻的东南西北四个点，设计一个算法，模拟老鼠走迷宫，找到从入口到出口的一条路径。

思路

用一个栈来记录老鼠从入口到出口的路径
走到某点后，将该点左边压栈，并把该点值置为1，表示走过了；
从临近的四个点中可到达的点中任意选取一个，走到该点；
如果在到达某点后临近的4个点都不走，说明已经走入死胡同，此时退栈，退回一步尝试其他点；
反复执行第二、三、四步骤直到找到出口；
"""


def initMaze():
    maze_list = [[0 for i in range(7)] for j in range(7)]
    for i in range(7):
        maze_list[i][0] = 1
        maze_list[i][-1] = 1
        maze_list[0][i] = 1
        maze_list[-1][i] = 1
    walls = [(1, 3), (2, 1), (2, 5), (3, 3), (3, 4), (4, 2), (5, 4)]
    for i, j in walls:
        maze_list[i][j] = 1
    return maze_list


def path(maze, start, end):
    i, j = start
    ei, ej = end
    stack = [(i, j)]
    maze[i][j] = 1
    while stack:
        i, j = stack[-1]
        if (i, j) == (ei, ej):
            break
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if maze[di + i][dj + j] == 0:
                maze[di + i][dj + j] = 1
                stack.append((di + i, dj + j))
                break
        else:
            stack.pop()
    return stack


Maze = initMaze()  # 初始化迷宫
for i in Maze:
    print(i)
# result = path(maze=Maze, start=(1, 1), end=(5, 5))  # 老鼠开始走迷宫
# print(result)
