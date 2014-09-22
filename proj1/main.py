n = int(raw_input("Give the number: "))
sum = 0

for i in xrange(n):

    sum += i if ((i%3)==0 or (i%5)==0) else 0
    #sum += ((i%3)==0 or (i%5)==0) ? i : 0 
    #if(i%3)==0:
    #    sum += i
    #elif(i%5)==0:
    #    sum += i

print(sum)
