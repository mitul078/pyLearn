def count(String):
    countVowel = 0
    countConsonant = 0
    for i in String:
        if i in "aeiouAEIOU" :
            countVowel+=1
        else:
            countConsonant+=1
    return f"vowels: {countVowel} , consonants: {countConsonant}"

print(count("helloWorld"))