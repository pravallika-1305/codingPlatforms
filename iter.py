my_string = "abcbx"
def longestPalindrome(my_string):
    final_string = ""
    for i in range(len(my_string)):
        my_str = my_string
        for j in my_str[i:]:
            new_string = ""
            new_string = new_string + j
            if(isPalindrome(new_string)):
                final_string = final_string + new_string
            else:
                print("no")
    return final_string

def isPalindrome(astr):
    astr == astr[::-1]

print(longestPalindrome(my_string))