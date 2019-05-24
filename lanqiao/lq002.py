for j in range(1000):
    if '3' in str(j):
        prefix = ''
        if '33' in str(j):
            prefix = '&'
        if j > 1:
            for i in range(2, j):
                if (j % i) == 0:
                    postfix = ''
                    break
            else:
                postfix = '*'
        else:
            postfix = ''
        print prefix + str(j) + postfix
