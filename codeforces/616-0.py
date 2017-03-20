a = str(raw_input())
b = str(raw_input())

def reduce_string(s):
    for i in range(len(s)):
        if s[i] != "0":
            return s[i:]
    return "0"

def compare(ra, rb, i):
    for i in range(len(ra)):
        if ra[i] > rb[i]:
            return ">"
        if ra[i] < rb[i]:
            return "<"
    return "="

ra = reduce_string(a)
rb = reduce_string(b)

lra = len(ra)
lrb = len(rb)

if lra > lrb:
    print ">"
elif lra < lrb:
    print "<"
else:
    print compare(ra, rb, 0)

