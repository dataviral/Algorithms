def polynomial(P, x):
    p = P[-1]
    for i in reversed(range(0, len(P)-1)) :
        p = p*x + P[i]
    return p

def binLRExponentiation(a, b):
    p = a
    for i in (range(1 ,len(b))) :
        p = p * p
        if b[i] == 1:
            p = p*a
    return p

def binRLExponentiation(a, b):
    term = a
    if b[-1] == 1:
        p = a
    else :
        p = 1
    for i in reversed(range(0, len(b)-1)):
        term = term * term
        if b[i] == 1:
            p = p *term
    return p

P = [ -10, 0, 5, -7, 3  ]   # 3x^4 - 7x^3 + 5x^2 - 10
b = [1, 1, 0, 1]

print("p(x) = 3x^4 - 7x^3 + 5x^2 - 10 evaluated at x = 2 :  ",polynomial(P, 2))
print("2^ 13 (LR Exponentiation):  ", binLRExponentiation(2, b))
print("3^ 13 (RL Exponentiation):  ", binRLExponentiation(3, b))
