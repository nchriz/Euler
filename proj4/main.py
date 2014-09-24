import time

def isPalindrom(x):
    if str(x) == str(x)[::-1]:
        return 1
    return 0

def main():
    start = time.time()
    tmp = 0
    for x in xrange(999,1,-1):
        for y in xrange(999,x,-1):
            if str(x*y) == str(x*y)[::-1] and tmp < x*y:
                tmp = x*y
                break
            #if isPalindrom(x*y) and tmp < x*y:
            #    tmp = x*y
    print(time.time() - start)
    print(tmp)

if __name__ == "__main__":
    main()
