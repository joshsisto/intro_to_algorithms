# https://www.programminginpython.com/selection-sort-algorithm-python/
# https://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html?highlight=selection%20sort


import time


def timeit(method: object) -> object:
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('%r %2.2f sec \n %r, %r' % (method.__name__, te - ts, args, kw))

        return result

    return timed


@timeit
def selection_sort(sort_list):
    for i in range(len(sort_list)):
        smallest_element = min(sort_list[i:])
        index_of_smallest = sort_list.index(smallest_element)
        sort_list[i], sort_list[index_of_smallest] = sort_list[index_of_smallest], sort_list[i]
        # print('\nPASS :', i + 1, sort_list)
    # print('\n\nThe sorted list: \t', sort_list)
    return sort_list


@timeit
def selection_sort_2(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
    return alist


# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# lst = []
# size = int(input("\nEnter size of the list: \t"))

# for i in range(size):
#     elements = int(input("Enter the element: \t"))
#     lst.append(elements)

# selection_sort(a_list)
