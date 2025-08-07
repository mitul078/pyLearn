#reverse the elem

arr = [10,20,30,40,50]
print(len(arr))
rev = []
for i in range(len(arr)-1 , -1 ,-1):
    rev.append(arr[i])
print(rev)