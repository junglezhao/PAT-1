import sys   
sys.setrecursionlimit(1000000)

def f(m, k, i):
    if i == 1:
        return (m + k - 1) % m
    else:
        return (f(m-1, k, i-1) + k) % m

n = int(raw_input())
print f(n, 3, n) + 1
