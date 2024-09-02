import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1 Option
rand_num = random.randint(0, 4)
print(rand_num)
print(friends[rand_num])

# 2 Option
print(random.choice(friends))