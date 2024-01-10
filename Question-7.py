# Write a python program to copy elements 4 and 5 from the following tuple into a new tuple. 
# tuple1 = (1,2,3,4,5,6)

tuple1 = (1,2,3,4,5,6)

tuple2 = tuple(e for e in tuple1[3:5])
print("Tuple2:",tuple2)