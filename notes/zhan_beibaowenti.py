"""
背包问题
题目

有一个背包能装10kg的物品，现在有6件物品分别为：

物品名称	重量
物品0	1kg
物品1	8kg
物品2	4kg
物品3	3kg
物品4	5kg
物品5	2kg
编写找出所有能将背包装满的解，如物品1+物品5。
"""


def knapsack(package, items):
    n = len(items)  # 可选物品的数量
    stack = []  # 创建一个栈
    index = 0  # 当前所选择的物品游标
    while stack or index < n:
        # print('current stack')
        # print(stack)
        while package > 0 and index < n:
            if package >= items[index]:
                package -= items[index]
                stack.append(index)
                # print('append {}'.format(index))
                # print(stack)
            index += 1
        if package == 0:
            # print('success')
            print(stack)
        index = stack.pop()
        package += items[index]
        index += 1


knapsack(10, [1, 8, 4, 3, 5, 2])
"""
[0, 2, 3, 5]
[0, 2, 4]
[1, 5]
[3, 4, 5]
"""
