def checkPalindrome(String):
    rev = ""
    for i in range(len(String)):
        rev = String[::-1]
    if(rev == String):
        return f"{String} is a palindrome"
    else:
        return f"{String} is not a palindrome"
    

print(checkPalindrome("madam"))
print(checkPalindrome("hello"))
print(checkPalindrome("naman"))