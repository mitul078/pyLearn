arr = []

elem = int(input("Enter total elem: "))
for i in range(elem):
    z = int(input(f"Enter num {i+1}: "))
    arr.append(z)

positive =[]
negative=[]

for i in arr:
    if (i >= 0):
        positive.append(i)
    else:
        negative.append(i)

print(f"positive: {positive}")
print(f"negative: {negative}")