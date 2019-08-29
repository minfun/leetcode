# 递归二分查找
def binary_search_recursion(lst, value, low, high):
    if high < low:
        return None
    mid = (low + high) / 2
    if lst[mid] > value:
        return binary_search_recursion(lst, value, low, mid - 1)
    elif lst[mid] < value:
        return binary_search_recursion(lst, value, mid + 1, high)
    else:
        return mid


# 二分查找
def binary_search(lst, key):
    low = 0
    high = len(lst) - 1
    times = 0
    while low < high:
        times += 1
        mid = int((low + high) / 2)
        if key < lst[mid]:
            high = mid - 1
        elif key > lst[mid]:
            low = mid + 1
        else:
            return mid
    return False


# 插值查找
def insert_search(lst, key):
    low = 0
    high = len(lst) - 1
    time = 0
    while low < high:
        time += 1
        mid = low + int((high - low) * (key - lst[low])/(lst[high] - lst[low]))
        if key < lst[mid]:
            high = mid - 1
        elif key > lst[mid]:
            low = mid + 1
        else:
            return mid
    return False


# 斐波那契查找
def fibonacci_search(lst, key):
    F = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
         233, 377, 610, 987, 1597, 2584, 4181, 6765,
         10946, 17711, 28657, 46368]
    low = 0
    high = len(lst) - 1
    k = 0
    while high > F[k] - 1:
        k += 1
    print(k)
    i = high
    while F[k] - 1 > 1:
        lst.append(lst[high])
        i += 1
    time = 0
    while low <= high:
        time += 1
        if k < 2:
            mid = low
        else:
            mid = low + F[k-1] - 1

        print("low=%s, mid=%s, high=%s" % (low, mid, high))

        if key < lst[mid]:
            high = mid - 1
            k -= 1
        elif key > lst[mid]:
            low = mid + 1
            k -= 2
        else:
            if mid <= high:
                print("times:%s" % time)
                return mid
            else:
                print("times:%s" % time)
                return high
    print("times:%s" % time)
    return False


LIST = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
print(binary_search(LIST, 99))
print(insert_search(LIST, 444))
print(fibonacci_search(LIST, 444))
