def amicable(n, x):
    sum = 0
    for i in range(1,n):
        if not n%i:
            sum += i
    if x and sum != n:
        return n == amicable(sum,0)
    return sum


def ami(n):
    sum = 0
    for i in range(1,int(n/2)):
        if not n%i:
            sum += i
    return sum

def main():
    tmp = {1:1}
    real = {}
    sum = 0
    n = 10000
    for x in range(2,100000):
        n = ami(x)
        if x != n:
            tmp[x] = n
        
    i = {220: ami(220)}
    i[ami(220)] = 220
    if i[220] == 284 and i[i[220]] == 220:
        print "hej"

    for x in range(1,n):
        if tmp[tmp[x]] == x:
            sum += tmp[x]
    print sum


    #tmp = 0
    #print amicable(220,1)
    #for x in range(1,10000):
    #    if amicable(x,0) == True:
    #        tmp += x
    #print tmp

if __name__ == "__main__":
    main()
