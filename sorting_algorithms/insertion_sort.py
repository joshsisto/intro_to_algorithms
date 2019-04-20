# https://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html
# https://www.laurivan.com/braindump-use-a-decorator-to-time-your-python-function/

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
def insertion_sort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue
    return alist


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# print list before sorting
# print(a_list)

# sort list using insertion_sort() function
# insertion_sort(a_list)

# print the sorted list
# print(a_list)
