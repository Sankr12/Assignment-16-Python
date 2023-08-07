# Write a python program to swap two tuples in python

t1 = tuple([e for e in input("Enter the elements with comma between them: ").split(',')])
t2 = tuple([a for a in input("Enter the elements with comma between them: ").split(',')])

t1,t2 = t2,t1

#After swapping
print("Tuple 1:",t1)
print("Tuple 2:",t2)