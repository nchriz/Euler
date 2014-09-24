def main():
    n = 20
    i = 1
    while True:
        tmp = 0
        if n%11 != 0:
            tmp = 1
        for x in xrange(13,20):
            if (n%x)!= 0:
                tmp = 1
                break
        if tmp < 1:
            print(n)
            return 0
        i += 1
        n = 20 * i
        #print(n)
            
    print("Hello")

if __name__ == "__main__":
    main()
