n = 130010
sum = 1
largest = 0
while n > 1:
    if not n%2:
        n = n/2
    else:
        n = 3*n + 1
    if n > largest:
        largest = n
    sum += 1

print sum
print largest
