# Github: https://github.com/minfun/leetcode
# Email: nowican@live.com
# Wechat: creategoodthing


def spread_list(l):
    """
    :param l: list of list of list
    :type l: list
    :return: spread list
    :rtype: list
    """
    return sum([spread_list(x) if type(x) == list else [x] for x in l], [])
