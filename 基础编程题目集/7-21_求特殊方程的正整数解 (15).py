n = int(raw_input())
isOk = False
for x in xrange(1, 101):
    for y in xrange(x, 101):
        if x*x+ y*y == n:
            isOk = True
            print x, y
if not isOk:
    print 'No Solution'

