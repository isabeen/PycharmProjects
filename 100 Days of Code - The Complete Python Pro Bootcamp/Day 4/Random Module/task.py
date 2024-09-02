import random
# import my_module
#
# rand_num = random.randint(1, 10)
# print(rand_num)
# rand_num_0_to_1 = round(random.random(), 3)
# print(rand_num_0_to_1)
# rand_5 = random.random() * 5
# print(rand_5)
#
# print(my_module.my_favorite_number)
print("Welcome to the coin flip game!")
rand_num = random.randint(1, 10)
print(rand_num)
if rand_num > 5:
    print("Heads")
else:
    print("Tails")
