# Write a python program to reverse a tuple

print()
t1 = tuple([e for e in input("Enter a tuple: ").split(",")])

# Before slicing
print("Original Tuple:",t1)
print()

# After slicing
t2=t1[::-1]
print("Reversed Tuple:",t2)
print()