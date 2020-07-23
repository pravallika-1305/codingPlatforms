from sys import stdin
earth, mars = 365, 687
string = stdin.readline().strip()
case = 1
while string:
    try:        
        earth_test, mars_test = map(int, string.split(' '))
        if earth_test == mars_test == 0:
            print ("Case %s: %s" % (case, 0))            
        else:
            string = earth - earth_test
            mars_test += string
            while mars_test % mars != 0:
                string += earth
                mars_test += earth
            print ("Case %s: %s" % (case, string))
        string = stdin.readline().strip()
        case+=1
    except (EOFError):
        break