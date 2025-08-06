# a = "abc123@#$"
# charCount = 0
# digitCount = 0
# symbolCount = 0

# for i in a:
#     if(i in "abcdefghijklmnopqrstuvwxyz") :
#         charCount  = charCount +1
#     elif(i in "1234567890"):
#         digitCount = digitCount + 1
#     else:
#         symbolCount = symbolCount + 1

# print(f"Character: {charCount}")
# print(f"Digit: {digitCount}")
# print(f"Symbol: {symbolCount}")



#also use methods , ascii values

a = "abc123@#$"
charCount = 0
digitCount = 0
symbolCount = 0

for i in a:
    ascii_val = ord(i)
    if (65 <= ascii_val <= 90) or (97 <= ascii_val <= 122):
        charCount += 1
    elif 48 <= ascii_val <= 57:
        digitCount += 1
    else:
        symbolCount += 1

print(f"Character: {charCount}")
print(f"Digit: {digitCount}")
print(f"Symbol: {symbolCount}")
