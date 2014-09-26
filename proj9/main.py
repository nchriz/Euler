import time
import math

def isNatural(x):
    tmp = math.sqrt(x)
    if(math.floor(tmp)<tmp):
        return False
    return True

def findTri(n):
    for x in xrange(1,n):
        for y in xrange(1,x):
            tmp = x**2+y**2
            if isNatural(tmp):
                if ((x+y+math.sqrt(tmp))==1000):
                    return x, y, math.sqrt(tmp)

def main():
    start = time.time()
    n = 500
    a, b, c = findTri(n)
    print time.time() - start
    print a*b*c

if __name__ == "__main__":
    main()
