import time

def main():
    n = 101
    tmpsum = 0
    sqrsum = sum(xrange(n))**2
    for x in xrange(1,n):
        tmpsum += x**2
    print(sqrsum - tmpsum)
    print sum(xrange(n))**2 - sum([x*x for x in xrange(n)])

if __name__ == "__main__":
    main()
