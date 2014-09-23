import math
from math import *

def main():
    n = 4*pow(10,6)
    sum = 0
    i = 1

    fib = []
    fib.append(1)
    fib.append(1)

    while fib[i] < n:
        i+=1
        fib.append(fib[i-1] + fib[i-2])
        sum += fib[i] if (fib[i]%2)==0 else 0

    print(sum)

if __name__ == "__main__":
    main()
