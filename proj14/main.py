import operator
import time

def optimal():
    r = {}
    r[1] = 0
    r[2] = 1
    for i in range(1,10**6):
        n = i
        chain = 0
        while n not in r:
            if not n%2:
                n /= 2
            else:
                n = 3*n + 1
            chain += 1
        r[i] = chain + r[n]
    print max(r.items(), key=operator.itemgetter(1))

def main():
    sum = 0
    tmp = 0
    starting = 0
    for x in range(10**6):
        n = x
        tmp = 0
        while n > 1:
            if not n%2:
                n = n/2
            else:
                n = 3*n+1
            tmp += 1
        if tmp > sum:
            sum = tmp
            starting = x
    print sum
    print starting
    

if __name__ == "__main__":
    #main()
    optimal()
