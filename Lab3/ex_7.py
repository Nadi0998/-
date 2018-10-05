my_list = [x for x in range(1,6)]
print([x*x for x in my_list])
print(list(map(lambda x: x*x, my_list)))