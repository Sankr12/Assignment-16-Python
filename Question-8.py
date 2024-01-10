# Write a python program to sort a tuple of tuples by the second item.
# tuple1 = (('a',21),('b',37),('c',11),('d',29))

print()

tuple1 = [('a',21),('b',37),('c',11),('d',29)]
print("Original list:",tuple1)
Len=len(tuple1)

for i in range(0,Len):
    for j in range(0,(Len-i-1)):
        if(tuple1[j][1]>tuple1[j+1][1]):
            tuple1[j], tuple1[j+1] = tuple1[j+1], tuple1[j]


print("Sorted list:",tuple1)
print()