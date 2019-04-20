import random
from insertion_sort import *
from selection_sort import *
from merge_sort import *


my_randoms = random.sample(range(1, 10000000000), 1000000)

print(my_randoms)


# print(insertion_sort(my_randoms))
# selection_sort(my_randoms)
# selection_sort_2(my_randoms)
print(merge_sort(my_randoms))


