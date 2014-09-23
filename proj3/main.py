import time

def isPrime(x):
    for i in xrange(2,x):
        if (x%i)==0:
            return False
    return True

def main():
    n = 13195
    i = 600851475143
    prime = 2

    start = time.time()
    while prime <= i:
        if i%prime:
            prime +=1
        else:
            i //= prime
    print(time.time() - start)
    print(prime)
    return 0

    #for j in range(2,n):
    #    if isPrime(j):
    #        if(i%j)==0:
    #            i = i/j
    #            tmp = j

    #for j in range(n,i):
    #    if isPrime(j):
    #        if (i%j)==0:
    #            i = i/j
    #            tmp = j
    #print(tmp)


if __name__ == "__main__":
    main()
