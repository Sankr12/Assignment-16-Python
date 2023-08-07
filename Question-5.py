# Write a python program to check if all items in the tuple are same

print()
t1 = tuple([int(e) for e in input("Enter the elements with comma between them: ").split(',')])

i = 0
while i<len(t1)-1:
    if (t1[i]==t1[i+1]):
        pass
    else:
        print(False)
        break
    i+=1
else:
    print(True)
print()