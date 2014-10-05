def split(n):
    single = 0
    tens = 0
    hundred = 0
    tmp = 0
    while n > 0:
        if not tmp:
            single = n%10
            n = n/10
            tmp = 10
        elif tmp == 10:
            tens = n%10
            n = n/10
            tmp = 100
        elif tmp == 100:
            hundred = n%10
            n = n/10
            tmp = 1000
        #print n
    return single, tens, hundred

def main():
    wordcount = {"1":3, "2":3, "3":5, "4":4, "5":4, "6":3, "7":5, "8":5, "9":4, "10": 3, "11":6, "12":6, "13":8, "14":8, "15":7, "16":7, "17":9, "18":8, "19":8,"20":6, "30":6, "40":5, "50":5, "60":5, "70":7, "80":6, "90":6 }
    sum = 0
    for x in range(0,1000):
        s, t, h = split(x)
        tmp = 0
        if h > 0:
            #print h
            tmp += wordcount[str(h)] + 7
            if t > 0 or s > 0:
                tmp += 3
        if t > 0:
            #print t
            tmp += wordcount[str(t*10)]
        if s > 0:
            #print s
            tmp += wordcount[str(s)]
        print tmp, x
        sum += tmp
    sum += 3 + 8
    print sum

if __name__ == "__main__":
    main()
