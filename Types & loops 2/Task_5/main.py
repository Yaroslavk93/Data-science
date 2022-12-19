my_list = ['a', 'b', 'c', 'd', 'e', 'f']
my_dict = dict()
my_dict[my_list[-2]] = my_list[-1]


for i in range(len(my_list) - 3, -1, -1):
    my_copy = my_dict.copy()
    my_dict.clear()
    my_dict[my_list[i]] = my_copy

print(my_dict)
