# Github: https://github.com/minfun/leetcode
# Email: nowican@live.com
# Wechat: creategoodthing
# multiple sort https://www.cnblogs.com/wuxinyan/p/8615127.html


def quick_sort(unsort_list):
    """
    unsort_list = [1,3,5,8,2,6,7,9]
    :param unsort_list:
    :return:
    """
    if len(unsort_list) < 2:
        return unsort_list
    pivot = unsort_list[0]

    left = filter(lambda x: x < pivot, unsort_list[1:])
    right = filter(lambda x: x >= pivot, unsort_list[1:])

    return quick_sort(left) + [pivot] + quick_sort(right)


def bubblesort(unsort_list):
    for i in range(1, len(unsort_list)):
        for j in range(0, len(unsort_list) - i):
            if unsort_list[j] > unsort_list[j+1]:
                unsort_list[j], unsort_list[j+1] = unsort_list[j+1], unsort_list[j]
    return unsort_list


def selectionsort(unsort_list):
    for i in range(len(unsort_list) - 1):
        minIndex = i
        for j in range(i + 1, len(unsort_list)):
            if unsort_list[j] < unsort_list[minIndex]:
                minIndex = j
        if i != minIndex:
            unsort_list[i], unsort_list[minIndex] = unsort_list[minIndex], unsort_list[i]
    return unsort_list
