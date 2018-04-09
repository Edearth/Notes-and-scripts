list_a = [1, 2, 3, 4, 5]
list_b = [1, 3, 4, 6, 8]

print("assuming list_b is a new version of list_a")
print("added elements: ")
for elem in set(list_b) - set(list_a):
    print(" - "+str(elem))

print("deleted elements: ")
for elem in set(list_a) - set(list_b):
    print(" - "+str(elem))

print("difference: ")
for elem in set(list_a).symmetric_difference(set(list_b)):
    print(" - "+str(elem))

print("intersection/common elements: ")
for elem in [x for x in list_a if x in list_b]:
    print(" - "+str(elem))
