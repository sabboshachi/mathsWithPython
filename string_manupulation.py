def string_bits(str):
    newStr = ''
    for i in range(len(str)):
        if (i % 2) == 0:
            newStr=newStr+(str[i])
    return newStr

string_bits('Heeololeo')
