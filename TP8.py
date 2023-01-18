ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = 5
b = 17

def RANG(car):
    resu = -1
    i = 0
    while (i<26) and resu == -1:
        if (car ==ALPHABET[i]):
            resu = i
        i = i+1
    return resu

def code_lettre(car):
    x = RANG(car)
    r = (a*x+b)%26
    return ALPHABET[r]

def code_message(txt):
    resu=''
    long = len(txt)
    for i in range(long):
        c = txt[i]
        resu=resu + code_lettre(c)
    return resu
