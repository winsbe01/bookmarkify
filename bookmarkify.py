# get the input string
istr = input("What would you like to bookmarkify? ")

white = '\x1b[6;37;47m'
black = '\x1b[0;30;40m'
ender = '\x1b[0m'

# loop through, print the binary
for c in istr:
    b = bin(ord(c))
    t = b[(len(b)-5):]
    #t = b

    f = []

    for c_t in t:
        if c_t == '0':
            f.append(white)
            #f.append(black)
        else:
            f.append(black)
            #f.append(white)

        f.append('  ')
        f.append(ender)

    print("".join(f))
