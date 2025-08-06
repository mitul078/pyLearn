a = "string"

count = len(a) #length of string
upperCase = a.upper() #upper
lowerCase = a.lower() #lower
b = a #copy

for  i in range(len(a)-1 ,-1, -1):
    print(a[i] , end=" ")
    
#also do like this
    # [::-1]