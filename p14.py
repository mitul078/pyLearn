arr = [1,2,5,3,2,1]
rev = []

for i in range(len(arr)-1 , -1, -1):
    rev.append(arr[i])
    
if(arr==rev):
    print("palindrome")