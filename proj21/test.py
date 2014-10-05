import time
from time import *

def main():
    start = time()
    n = 10**6
    sum = 0
    num = [1] *n
    for x in range(2,int(n/2)):
        for y in range(2*x,n,x):
            num[y] += x

    for x in range(2,10001):
        if x == num[num[x]] and num[x] != x:
            sum += x

    print time() - start
    print sum
        
            


if __name__ == "__main__":
    main()
