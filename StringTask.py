def isVowel(ch):
    return ch in "aeiouyAEIOUY"

def removeVowels(input_string):
    for i in input_string:
        if i.isalpha() and isVowel(i):
             input_string = input_string.replace(i,'')
    return input_string

def insertdots(novowel_str):
    final_string = ""
    for i in novowel_str:
        final_string = final_string + "." + i
    return final_string


string = input()
print(insertdots(removeVowels(string.lower())))
