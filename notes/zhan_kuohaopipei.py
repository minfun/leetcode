"""
括号匹配
题目

假如表达式中允许包含三中括号()、[]、{}，其嵌套顺序是任意的，例如：

正确的格式 {()[()]},[{({})}]
错误的格式 [(]),[()),(()}

编写一个函数，判断一个表达式字符串，括号匹配是否正确

思路:

创建一个空栈，用来存储尚未找到的左括号；
便利字符串，遇到左括号则压栈，遇到右括号则出栈一个左括号进行匹配；
在第二步骤过程中，如果空栈情况下遇到右括号，说明缺少左括号，不匹配；
在第二步骤遍历结束时，栈不为空，说明缺少右括号，不匹配；
"""


LEFT = ['(', '[', '{']  # 左括号
RIGHT = [')', ']', '}']  # 右括号

map_kuohao = {'{': '}', '[': ']', '(': ')'}


def match(expr):
    """
    :param expr:  传过来的字符串
    :return:  返回是否是正确的
    """
    stack = []  # 创建一个栈
    for brackets in expr:  # 迭代传过来的所有字符串
        if brackets in map_kuohao.keys():  # 如果当前字符在左括号内
            stack.append(brackets)  # 把当前左括号入栈
        elif brackets in map_kuohao.values():  # 如果是右括号
            if not stack or brackets != map_kuohao[stack[-1]]:
                # 如果当前栈为空，()]
                # 判断括号是否一致
                return False  # 返回False
            stack.pop()  # 删除左括号
    return not stack  # 如果栈内没有值则返回True，否则返回False


# result = match('[(){()}]')
# print(result)
# result = match('[({)}{()}]')
# print(result)
# print(match('({})[]'))
# print(match('({})[]'))
# print(match('({})[]'))
# print(match('({(})[]'))
# print(match('({(}))[]'))
# print(match('({})[]'))
#
# kuohao = {'(': ')', '{': '}', '[': ']'}
# def match_manually(expr):
#     stack = []
#     for brack in expr:
#         if brack in kuohao.keys():
#             stack.append(brack)
#         elif not stack or brack != kuohao[stack[-1]]:
#             return False
#         stack.pop()
#     return not stack
#
# print(match_manually('({})[]'))
# print(match_manually('({})[]'))
# print(match_manually('({})[]'))
# print(match_manually('({(})[]'))
# print(match_manually('({(}))[]'))
# print(match_manually('({})[]'))


huohao = {'(': ')', '[': ']', '{': '}'}


def match(expr):
    stack = []
    for brack in expr:
        if brack in huohao.keys():
            stack.append(brack)
        elif brack in huohao.values():
            if not stack or brack != huohao[stack[-1]]:
                return False
            stack.pop()
    return not stack


print(match('([])'))
print(match('([{}])'))
print(match('][{}])'))
print(match('()[]'))
