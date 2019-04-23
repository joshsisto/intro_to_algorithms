# https://www.simplifiedpython.net/linear-search-python/

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
def linear_search(myList, item):
    for i in range(len(myList)):
        if myList[i] == item:
            return f'{item} found at index {i}'
    return f'{item} not found'


# myList = [1, 7, 6, 5, 8]
# print("Element in List :", myList)
# x = int(input("enter searching element :"))

# result = linear_search(myList, x)
# if result == -1:
#     print("Element not found in the list")
# else:
#     print("Element " + str(x) + " is found at position %d" % result)

