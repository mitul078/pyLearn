arr = []
num = int(input("Enter num: "))
for i in range(num):
    z = int(input(f"Enter num {i+1}: "))
    arr.append(z)
    
max=0
mix2=0
idx = 0
idx2= 0

for i in range(len(arr)):
    if(arr[i] > max):
        max2 = max
        max = arr[i]
        idx2 = idx
        idx = i
    elif(arr[i] > max2):
        max2 = arr[i]
print(max2)