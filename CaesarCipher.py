def decode(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result = result + chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            result = result + chr((ord(char) + s - 97) % 26 + 97)
        elif char == " ":
            result = result +" "
        elif char == '"':
            result = result + '"'
        elif char == "'":
            result = result + "'"
    return result
text = input("")
s = int(input(""))
k = decode(text,s)
print(k)


