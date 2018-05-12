set1 = {2,4,6}

print set1

set1.update([2,6,9])

print set1
set1.add(3)
print set1

set1.discard(3)
print set1

set2 = set('Hola')

print set2
print type(set2)
print set2.pop()

set3 = set2.copy()

set2.clear()
print set2.symmetric_difference(set3)
print set3.symmetric_defference(set2)
print set1.difference(set2)

print set1.intersection(set2)

print set1.union(set2)

print set3.union(set2).union(set1)

set3.clear()
set2.remove()
