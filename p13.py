arr= [1,2,5,4,5,6]

for i in range(len(arr)-1):
    if(arr[i] <=   arr[i+1]):
        continue
    else:
        print("Not a sorted array")
        break
else:
    print("Array is sorted")
