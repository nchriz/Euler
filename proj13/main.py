import time

def main():
    start = time.time()
    n = []
    for f in open('digits.txt'):
        n.append(float(f.strip())/10**25)
    print sum(n)
    print time.time() - start

if __name__ == "__main__":
    main()
