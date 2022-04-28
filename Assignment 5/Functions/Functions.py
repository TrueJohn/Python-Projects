def sort_algorithm(list_to_sort, condition):
    for i in range(len(list_to_sort) - 1):
        for j in range(i + 1, len(list_to_sort)):
            if condition(i, j):
                list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]
    return list_to_sort


def search_algorith(list_to_search, condition):
    temp_list = []
    for i in range(len(list_to_search)):
        if condition(i):
            temp_list.append(list_to_search[i])
    return temp_list


def combinations(lst, n):
    if n == 0:
        return [[]]

    l = []
    for i in range(0, len(lst)):

        m = lst[i]
        remLst = lst[i + 1:]

        for p in combinations(remLst, n - 1):
            l.append([m] + p)

    return l

