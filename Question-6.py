# Write a python program to divide the tuple into four variable (tuple1 = (100, 200, 300, 400))

print()

tuple1 = (100, 200, 300, 400)

for i in range(len(tuple1)):
    if i==0:
        t1=tuple1[i]
        print(t1)
    elif i==1:
        t2=tuple1[i]
        print(t2)
    elif i==2:
        t3=tuple1[i]
        print(t3)
    else:
        t4=tuple1[i]
        print(t4)

print()