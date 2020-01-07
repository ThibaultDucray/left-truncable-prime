from sympy import isprime
import time

def ltoi(l):
    n = 0
    u = 1
    for i in l:
        n += i * u
        u *= 10
    return n

def record(recN, n):
    print(str(n) + "          ", end='\r')
    if n > recN:
        print(n)
        return n
    else:
        return recN

def longestPrime(startnum):
    u = 1
    l = [startnum]
    m = 0
    n = 0
    recN = 0
    while u > 0:
        m = ltoi(l)
        if isprime(m):
            recN = record(recN, m)
            u += 1
            l.append(1)
        else:
            n = l[u-1]
            while (n == 9) and (u > 0):
                l.pop()
                u -= 1
                if u > 0:
                    n = l[u-1]
            if u > 0:
                l[u - 1] = n + 1
    return recN

t1 = time.time()
print("result: " + str(longestPrime(1)))
t2 = time.time()
print("elapsed time: " + str(t2 - t1) + "s")
