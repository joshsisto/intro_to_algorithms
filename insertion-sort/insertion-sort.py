# https://interactivepython.org/runestone/static/pythonds/SortSearch/TheInsertionSort.html


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

insertion_sort(a_list)
print(a_list)
