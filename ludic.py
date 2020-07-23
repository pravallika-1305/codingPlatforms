def ludic(nmax):
    yield 1
    lst = list(range(2, nmax + 1))
    while lst:
        yield lst[0]
        del lst[::lst[0]]
n = int(input())
ludics = [l for l in ludic(n)]
print(len(ludics))
