import math
INF = float('inf')

def numberOfDiv(n):
    x = 0
    nsqrt = math.sqrt(n)
    for i in range(1, int(nsqrt)+1):
        if n%i == 0:
            x += 2
    if nsqrt*nsqrt == n:
        x-=1
    return x

def tri(stop):
    sum = 0
    n = 1
    while n < stop:
        sum += n
        yield sum
        n += 1

def proj12():
    n = 1
    sum = 0
    while True:
        sum += n
        tmp = 2
        max = sum
        for x in range(2,int(max**0.5)+1):
            if not n%x:
                tmp+=2
                max = max/x
        if tmp>5:
            return sum, tmp
        n+=1

def main():
    #n = 7
    #sum = 0
    #tmp = 0
    #for x in range(1,n+1):
    #    sum += x
    #    if n%x:
    #        tmp+=1
    #sum, tmp = proj12()
    #print tmp
    #print sum
    stop = 500
    for x in tri(INF):
         num = numberOfDiv(x)
         if num > stop:
             print("x: " + str(x) + " num: " + str(num))
             break

if __name__ == "__main__":
    main()
