def convert(s): 
    new = ""  
    for x in s: 
        new += x   
    return new 


def replaceIOUnderscore(string):
    count = 0
    string = list(string)
    for i in range(len(string)):
        if string[i] == "I":
            for j in range(i + 1,len(string)):
                if string[j] == "O":
                    count = count + 1
                    string[i],string[j]= "_","_"
                    break
    return string

def replaceothers(char_list):
    for i in range(len(char_list)):
        if char_list[i] in "iI":
            char_list[i] = "*"
        if char_list[i] in "oO":
            char_list[i] = "#"
    return char_list

def remove_(new_list):
    for i in new_list:
        if i == '_':
            new_list.remove('_')
    return new_list

def count_(modified_string):
    count = 0
    for i in modified_string: 
        if i == '_': 
            count = count + 1
    return count

def checking(coded_string):
    for i in coded_string:
        if i == "#":
            return False
        else:
            return True
        
my_string = input()
if "I" and "O" not in my_string:
    print(0)
else:
    new_list = replaceothers(replaceIOUnderscore(my_string))
    check_string = convert(remove_(new_list))
    if (checking(check_string)):
        totalIOs = int(count_(replaceIOUnderscore(my_string)) / 2)
        print(totalIOs)
    else:
        print(0)



