max_range = int(input("Enter the maximum length of string:"))
word = input("Enter the word you want to search for :")
word_letters = list(word) 
result = 0
for i in range(max_range):
    result = result + ( ord(word_letters[i]) - ord('a') ) * (26 ** (max_range-i-1) )
 
print(result+1)



