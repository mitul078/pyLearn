a = "hello world how are you"
#result = "hello dlrow how era you"
b = a.split()

for i in range(len(b)):
    if i%2!=0 :
        b[i] = b[i][::-1]

print(' '.join(b))
