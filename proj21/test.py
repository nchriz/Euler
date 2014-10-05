def main():
    n = 10**5
    num = [1] *n
    for x in range(2,int(n/2)):
        for y in range(2*x,n,x):
            num[y] += x

    print num
        
            


if __name__ == "__main__":
    main()
