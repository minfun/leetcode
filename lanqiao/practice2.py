'''
写出python程序，一定要利用递归函数，尽量不用for循环、while循环。

输入整数B代表进制数，再输入两个B进制的数，用列表list_a和list_b表示，输出list_a+list_b的B进制数结果，也可以用列表来表示。

例如，B=16，输入list_a=[10,9,9]和list_b=[9,9]，相加后的十六进制结果是[11,3,2]；如果B=11，相加后的结果是[1,0,8,7]。

解题思路：

要注意两点，一点是列表长度可能不一致，另外一点是相加之后大于进制数时需要进位1。

每一次递归，我们都取出两个列表的最后一个元素和进位数一起进行求和。

因为列表元素数量可能不一致，当只有一个列表有元素时，只取出有元素的列表最后一位与进位数求和。

如果列表都为空，存在进位数时，直接返回进位数，否则，返回空列表。

对于每一次递归计算出的和，分别获取进位数和余数，并将余数与外层递归结果合并，将进位数作为参数传入下一次递归。
'''
list_a = [10, 9, 9]
list_b = [9, 9]
mod = 16


def fun(mod, lst_a, lst_b, carry=0):
    result = []  # 每次递归的计算结果列表
    if lst_a and lst_b:  # 如果列表均不为空
        sum = lst_a[-1] + lst_b[-1] + carry  # 取出每个列表最后一个元素与上一层传入的进位数相加求和
        print('lst_a[-1]')
        print(lst_a[-1])
        print('lst_b[-1]')
        print(lst_a[-1])
        print('sum')
        print(sum)
        print('carry')
        print(carry)
        lst_a.pop(-1)  # 从列表中去除最后一个元素
        lst_b.pop(-1)
    elif lst_a:  # 如果lst_a列表不为空
        sum = lst_a[-1] + carry  # 列表最后一位元素与上一层传入的进位数相加求和
        print('lst_a[-1]')
        print(lst_a[-1])
        print('sum')
        print(sum)
        print('carry')
        print(carry)
        lst_a.pop(-1)  # 从列表中去除最后一个元素
    elif lst_b:
        sum = lst_b[-1] + carry
        print('lst_b[-1]')
        print(lst_b[-1])
        print('sum')
        print(sum)
        print('carry')
        print(carry)
        lst_b.pop(-1)
    else:  # 如果列表均为空
        if carry:  # 如果有进位数
            return [carry]  # 返回进位数
        else:  # 否则
            return []  # 返回空列表
    carry = sum // mod  # 计算当前和按进制计算后的进位数
    print('sum in function')
    print(sum)
    print('craay in function')
    print(carry)
    remainder = sum % mod  # 计算当前和按照进制计算后的余数
    print('remainder')
    print(remainder)
    result = [remainder] + result  # 余数以列表形式与外层递归列表合并
    print('result in function')
    print(result)
    return fun(mod, lst_a, lst_b, carry=carry) + result  # 进行下一层递归


if __name__ == '__main__':
    # print(fun(11, lst_a=list_a, lst_b=list_b, carry=0))
    print(fun(11, lst_a=list_a, lst_b=list_b, carry=0))
