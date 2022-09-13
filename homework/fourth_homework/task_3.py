import random
rand = random.Random()
num_list = []
for i in range(50):
    num_list.append(rand.randint(1,101))
set_num = set(num_list)
lang = len(set_num)
print(num_list, set_num, sep='\n')

