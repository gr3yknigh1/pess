def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return fib(n-1) + fib(n-2)


tot = 0
n = 0
fib_n = 0

while True:
    fib_n = fib(n)
    if fib_n > 4000000:
        break

    if fib_n % 2 == 0:
        print(f"+[{n}] {fib_n}")
        tot += fib_n
    else:
        print(f"-[{n}] {fib_n}")    
    n += 1

print(tot, n)