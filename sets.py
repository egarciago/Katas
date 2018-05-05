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
print set2
print set3