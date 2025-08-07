arr = [1,2,3,2,1,2,3,4,3,2,5,6,7,8,6,10,5,6,7]
d = {}

for i in arr:
    if(i in d.keys()):
        d[i] += 1;
    else:
        d[i] = 1

print(d)