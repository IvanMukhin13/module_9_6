def func(n):
    for i in n:
        yield i
    for i in range(len(n)):
        if i + 1 < len(n):
            a = n[i] + n[i + 1]
            yield a
    yield n

a = func('abc')
for i in a:
    print(i)
