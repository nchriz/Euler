import time

start = time.time()
a=['95 64']
a.append('17 47 82')
a.append('18 35 87 10')
a.append('20 04 82 47 65')
a.append('19 01 23 75 03 34')
a.append('88 02 77 73 07 63 67')
a.append('99 65 04 28 06 16 70 92')
a.append('41 41 26 56 83 40 80 70 33')
a.append('41 48 72 33 47 32 37 16 94 29')
a.append('53 71 44 65 25 43 91 52 97 51 14')
a.append('70 11 33 28 77 73 17 78 39 68 17 57')
a.append('91 71 52 38 17 14 91 43 58 50 27 29 48')
a.append('63 66 04 68 89 53 67 30 73 16 69 87 40 31')
a.append('04 62 98 27 23 09 70 98 73 93 38 53 60 04 23')
b = []
for i in a:
    b.append(i.split())

c = [[75]]
d = [[75]]
n = 1
for i in b:
    c.append([])
    d.append([])
    for j in i:
        c[n].append(int(j))
        d[n].append(int(j))
    n+=1

for i in range(0, len(c)-1):
    for j in range(0, len(c[i])):
        d[i+1][j+1] = d[i][j] + c[i+1][j+1]
        if d[i][j] + c[i+1][j] > d[i+1][j]:
            d[i+1][j] = d[i][j] + c[i+1][j]
#max = 0

#for i in d:
#    for j in i:
#        if j > max:
#            max = j

#print max
print time.time()-start
print max(d[len(d)-1])
