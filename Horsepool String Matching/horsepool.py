text = "Hey! You think you know me? yes ..... what ? yeah! you heard me i know you."
pattern = "You"

def shiftTable(p):
    lp = len(p)
    table = [lp] * 256
    for i in range(0, lp):
        table[ord(p[i])] -= 1+i
    return table

def horsepool(t, p):
    table = shiftTable(p)
    n = len(t)
    m = len(p)
    i = m-1
    while i < n :
        k = 0
        while k < m and p[m-1-k] == t[i-k] :
            k += 1
        if k == m :
            return i - m + 1
        else :
            i += table[ord(t[i])]
    return -1

print("Text :", text)
print("Pattern :", pattern)
print("Pattern found at :",horsepool(text, pattern))
