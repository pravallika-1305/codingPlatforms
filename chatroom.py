def solve(string):
    word = "hello"
    index = 0
    for i in range(0,len(string)):
        if(index == 5):
            return "YES"
        if(string[i] == word[index]):
            index +=  1
    if(index < 5):
        return "NO"
    else:
        return "YES"
string = input()
print(solve(string))