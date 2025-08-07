arr = []
num = int(input("Enter num: "))
for i in range(num):
    z = int(input(f"Enter num {i+1}: "))
    arr.append(z)

def findGretestElem(arr):
    big = arr[0]
    idx = 0
    for i in range(len(arr)):
        if(arr[i] > big):
            big = arr[i]
            idx = i
    return(f"Gretest elem is {big} and it found at index {idx}")

print(findGretestElem(arr))