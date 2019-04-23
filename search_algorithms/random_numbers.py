import random
from linear_search import *
from sequential_search import *


my_randoms = random.sample(range(1, 1000000), 999000)

print(my_randoms)


print(linear_search(my_randoms, 22))
print(sequential_search(my_randoms, 22))

