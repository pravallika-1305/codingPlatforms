def shift(character,shifts):
    if character == 'z':
        return shift('a', shifts-1)
    return chr(ord(character) + shifts)

inp='abc'
shifts=[3,5,9]
shifts_for_char = []
for i in range(len(shifts)):
    shifts_for_char.append(sum(shifts[i:]))
string= ''
for char,shift_times in zip(list(inp),shifts_for_char):
    string = string + shift(char,shift_times)
print(string)