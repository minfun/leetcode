lst = [{'name': 'red', 'sub': [{'name': 'blue', 'sub': [{'name': 'white'}]}]}]


def fun(lst, name=''):
    result = []
    for dic in lst:
        if name:
            names = name + '/' + dic['name']
        else:
            names = dic['name']
        result.append(names)
        sub = dic.get('sub', None)
        if sub:
            result = result + fun(sub, names)
    return result


if __name__ == '__main__':
    print(fun(lst))
