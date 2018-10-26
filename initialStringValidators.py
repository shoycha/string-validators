if __name__ == '__main__':
    s = input()
    isAlnum = False
    isAlpha = False
    isDigit = False
    isLower = False
    isUpper = False
    for i in s:
        if i.isalnum():
            isAlnum = True
        if i.isalpha():
            isAlpha = True
        if i.isdigit():
            isDigit = True
        if i.islower():
            isLower = True
        if i.isupper():
            isUpper = True
    if isAlnum:
        print("True")
    else:
        print("False")
    if isAlpha:
        print("True")
    else:
        print("False")
    if isDigit:
        print("True")
    else:
        print("False")
    if isLower:
        print("True")
    else:
        print("False")
    if isUpper:
        print("True")
    else:
        print("False")
