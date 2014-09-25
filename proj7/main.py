import math
import time

def isPrime(x):
    for i in xrange(2,int(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True

def main():
    start = time.time()
    tmp = 6
    i = 13
    while tmp < 10001:
        i+=1
        if isPrime(i):
            tmp += 1
    end = time.time()
    print end - start
    print "the number is " + str(i) + " and its the " + str(tmp) +"th prime"

if __name__ == "__main__":
    main()
