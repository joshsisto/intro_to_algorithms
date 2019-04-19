import random
from insertion_sort import *


my_randoms = random.sample(range(1, 100000000), 10000)

print(my_randoms)


print(insertion_sort(my_randoms))


