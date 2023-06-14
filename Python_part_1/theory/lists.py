# Делаем списки!

my_awesome_list = [1, 2, 3, "a", "b", "c", [4, 5, 6]]

print(my_awesome_list[0])
print(my_awesome_list[-1])

print(my_awesome_list[-1][1])

print(my_awesome_list[:3])
print(my_awesome_list[::-1])

my_awesome_list[0] = "1"

print(my_awesome_list)
# Функции списков

my_awesome_list.append(7)
print(my_awesome_list)

# my_awesome_list.sort()

# Множества

list_with_duplicates = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5]
s1 = {1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5}

s2 = {4, 5, 6, 7, 8}

print(s1)

print(s1.union(s2))
print(s1.intersection(s2))
