# Write a python program to reverse a tuple

print()

num = int(input("Enter a range of element you want to enter: "))
t1 = tuple(input(f"Enter tuple element {e+1}: ") for e in range(num))

# Before slicing
print("Original Tuple:",t1)
print()

# After slicing
t2=t1[::-1]
print("Reversed Tuple:",t2)
print()