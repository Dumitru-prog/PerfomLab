n = int(input())
m = int(input())

def seq(n,m):
    yield 1
    for i in range(m-1, n*m, m-1):
        v = i % n + 1
        if v == 1: return
        yield v

print(list(seq(n,m)))