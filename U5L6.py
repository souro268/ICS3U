def f(n):
    sym = '#'
    if n == 1:
        return sym
    if n == 0:
        return
    else:
        
        print(sym*n)
        return f(n-1)
print(f(12))

