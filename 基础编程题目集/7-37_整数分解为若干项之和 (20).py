# search + back track
def f(n, cur, curSum, arr):
    if curSum == n:
        global ans
        ans.append(list(arr))
        return
    elif curSum > n:
        return
    else:
        for i in xrange(cur, n+1):
            arr.append(str(i))
            f(n, i, curSum+i, arr)
            arr.pop(-1)

n = int(raw_input())
ans = []
f(n, 1, 0, [])
r = ''
for index, value in enumerate(map(lambda x: '%d=%s' % (n, '+'.join(x)), ans)):
    if index != 0 and index % 4 == 0:
        r += '\n%s' % value
    elif index == 0:
        r += '%s' % value
    else:
        r += ';%s' % value
print r
