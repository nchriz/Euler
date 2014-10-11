import time
from time import time

def is_permu(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))

def primes(max):
    to_index = lambda n: (n-3)//2
    sieve = [True] * (to_index(max)+1)
    current = 3
    while current**2 <= max:
        if sieve[to_index(current)]:
            c = current**2
            while c <= max:
                sieve[to_index(c)] = False
                c += current*2
        current += 2
    return [2] + [i*2+3 for i, is_prime in enumerate(sieve) if is_prime]

def prime(n):
    sieve = [True] * n
    for x in xrange(3, int(n**0.5)+1):
        if sieve[x]:
            sieve[x*x::2*x] = [False]*((n-x*x-1)/(2*x)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def main():
    max_n = 10**7
    max_prime = int(max_n**0.5 * (1+0.3))
    min_prime = int(max_n**0.5 * (1-0.3))
    prime_num = [p for p in primes(max_prime) if p > min_prime]
    min_r, min_n = 2, None
    for p1 in reversed(prime_num):
        for p2 in prime_num:
            n = p1*p2
            if n > max_n or p2 > p1:
                break
            phi = int(round(n*(1-1.0/p1)*(1-1.0/p2)))
            ratio = float(n)/phi
            if ratio < min_r and is_permu(n,phi):
                min_r, min_n = ratio, n
    return min_n

print main()
