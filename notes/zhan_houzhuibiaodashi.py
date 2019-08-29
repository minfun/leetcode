"""
题目

计算一个表达式时，编译器通常使用后缀表达式，这种表达式不需要括号：

中缀表达式	后缀表达式
2 + 3 * 4	2 3 4 * +
( 1 + 2 ) * ( 6 / 3 ) + 2	1 2 + 6 3 / * 2 +
18 / ( 3 * ( 1 + 2 ) )	18 3 1 2 + * /
编写程序实现后缀表达式求值函数。

思路

建立一个栈来存储待计算的操作数；
遍历字符串，遇到操作数则压入栈中，遇到操作符号则出栈操作数(n次)，进行相应的计算，计算结果是新的操作数压回栈中，等待计算
按上述过程，遍历完整个表达式，栈中只剩下最终结果；
"""

operator = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}


def eval_postfix(expr):
    tokens = expr.split()
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token in operator.keys():
            x = stack.pop()
            y = stack.pop()
            stack.append(operator[token](x, y))
    return stack.pop()

print(eval_postfix('2 3 4 * +'))
