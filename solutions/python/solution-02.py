"""
Formula:
https://math.hmc.edu/funfacts/fibonacci-number-formula/
"""
from __future__ import annotations
import math


sqrt_from_5 = math.sqrt(5)
Phi_n = (1 + sqrt_from_5) / 2
phi_n = (1 - sqrt_from_5) / 2


def fib(n: int) -> int:
    """
    This implementation a lot faster then
    one belowe because of formula above.
    """
    return int((math.pow(Phi_n, n) - math.pow(phi_n, n)) / sqrt_from_5)


def nobby_fib(n: int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return fib(n-1) + fib(n-2)


def main() -> int:

    FIB_LIMIT: int = 4000000

    even_fib_sum = 0
    n = 0
    fib_n = fib(n)

    while fib_n <= FIB_LIMIT:
        
        if fib_n % 2 == 0:
            print(f"+[{n}] {fib_n}")
            even_fib_sum += fib_n
        else:
            print(f"-[{n}] {fib_n}")    
        
        n += 1
        fib_n = fib(n)

    print(f"Answer: {even_fib_sum}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
