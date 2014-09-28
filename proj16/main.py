import time

def main():
    start = time.time()
    n = 2**1000
    sum = 0
    while n > 0:
        sum += (n%10)
        n = n/10
    print sum
    print time.time() - start

if __name__ == "__main__":
    main()
