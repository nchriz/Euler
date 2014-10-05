import math
import sys

def main():
    n = math.factorial(int(sys.argv[1]))
    sum = 0
    while n > 1:
        sum += n%10
        n = n/10
    print sum

if __name__ == "__main__":
    main()
