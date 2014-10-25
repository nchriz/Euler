def createPrime():
    n = 10**6
    sieve = [True] * n
    for x in range(2, int(n**0.5)+1):
        if sieve[x]:
            for y in range(2*x,n,x):
                sieve[y] = False
    return sieve

def eulerfunction(a,b,prime):
    n = 1
    while True:
        if not prime[n**2+a*n+b]:
            return a*b, n
        n += 1

def test(a,b,prime):
    n = 1
    while True:
        if not prime[n**2+a*n+b]:
            return a*b, n
        n += 1

def main():
    large = 0
    sumnum = 0
    prime = createPrime()
    for x in range(-999,999):
        for y in range(-999,999):
            tmp, tmpsum = eulerfunction(x,y,prime)
            if tmpsum > sumnum:
                large = tmp
                sumnum = tmpsum
    print large
    print sumnum

prime = createPrime()
num, b = test(-79,1601,prime)
print num
print b

main()
