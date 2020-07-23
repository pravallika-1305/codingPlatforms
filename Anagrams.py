def find_anagrams(sent):
    my_list = sent.split()

    for i in my_list :
        sort_list = sorted_word(i)


   

def sorted_word(word):
    
    my_set = set(word)
    sort_set = sorted(my_set)

    return ("".join(sort_set))

print(sorted_word("ball"))
