a = "strINg"
b = ''
for i in a:
    if(i.islower()):
        b+=i
        
for i in a:
    if (i.isupper()):
        b+=i
        
print(b)