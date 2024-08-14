# a = [1, 2, 3, 4, 5]
# b = [5, 6, 7, 8, 9]

# common_elements = [value for value in a if value in b]
# print(common_elements)

list1 = ['a', 'b', 'c']
list2 = ['a', 'z', 'c']


common_elements = list(set(list1).intersection(list2))
print(common_elements)
