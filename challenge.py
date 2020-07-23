import itertools as it
my_string = input()
final_set = set(list(it.permutations(my_string,len(my_string))))
my_tuple = (tuple(list(my_string[::-1])))
final_list = list(final_set)
final_list.remove(my_tuple)
print(len(final_list))

