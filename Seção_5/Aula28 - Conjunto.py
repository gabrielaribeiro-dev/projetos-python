a ={1, 2, 3}
print(type(a))
a = set('cod3r')
print(a)
print('3' in a, 4 not in a)
a = {1, 2, 3} == {3, 2, 1, 3}
print(a)
c1 = {1, 2}
c2 = {2, 3}
print(c1.union(c2))
print(c1.intersection(c2))
c1.update(c2)
print(c1)
a= c2 <= c1
print(a)
a= c1 =c2
print(a)
a = {1, 2, 3} - {2, 3}
print(a)