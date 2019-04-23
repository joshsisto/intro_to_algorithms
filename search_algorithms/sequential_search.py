# https://runestone.academy/runestone/static/pythonds/SortSearch/TheSequentialSearch.html


def sequential_search(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
    return found

