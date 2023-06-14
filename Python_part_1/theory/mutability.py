# Списки, словари и множества - изменяемые!

from copy import deepcopy


l = [1, 2, 3, [4, 5, 6]]
# ll = l.copy()
ll = deepcopy(l)

ll.append(7)
l[-1].append(7)

print(l)
print(ll)


l.sort()
l_with_sort = sorted(l)


# Кортежи, frozenset - нет


t = (1, 2, 3)

ss = frozenset([1, 2, 3])
