import math
import time

def isPrime(n):
    for x in xrange(2,int(math.sqrt(n)+1)):
        if(n%x)==0:
            return False
    return True

def prime(n):
    sieve = [True] * n
    for x in xrange(3, int(n**0.5)+1):
        if sieve[x]:
            sieve[x*x::2*x] = [False]*((n-x*x-1)/(2*x)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]
        

def main():
    start = time.time()
    sum = 0

    prime_list = prime(2*10**6)
    for p in prime_list:
        sum += p
    print time.time() - start
    print sum

    #for x in xrange(2,2*10**6):
    #    if isPrime(x):
    #        sum += x
    #print "success " + str(x)
    #print time.time() - start
    #print sum

if __name__ == "__main__":
    main()
