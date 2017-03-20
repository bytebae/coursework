from math import ceil

input = raw_input()
m, n = input.split(" ",2)

if int(ceil(int(m)/2) * int(n)) < int(ceil(int(n)/2) * int(m)):
    print int(ceil(int(n)/2) * int(m))
else:
    print int(ceil(int(m)/2) * int(n))