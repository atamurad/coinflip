#!/usr/bin/python3

from Crypto.Util.number import getPrime
from sympy.ntheory.residue_ntheory import jacobi_symbol
from typing import Tuple
import random


def xgcd(a: int, b: int) -> Tuple[int, int, int]:
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    # Extended Euclidean algorithm. Ref: Wikipedia
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


# Solve modular square root
def solve(factors, x2):
    """
    Solve modular square root
    """
    p = factors[0]
    q = factors[1]
    N = p*q

    # p and q are primes with 3 (mod 4)
    # Ref: https://www.rieselprime.de/ziki/Modular_square_root
    r1 = pow(x2, (p+1)//4, p)
    r2 = pow(x2, (q+1)//4, q)

    g, v2, v1 = xgcd(p, q)

    assert((v2*p + v1*q) % N == 1)
    assert(v1*q % p == 1)
    assert(v2*p % q == 1)

    sol = []
    sol.append((r1*v1*q + r2*v2*p) % N)
    sol.append((r1*v1*q - r2*v2*p) % N)
    sol.append((-r1*v1*q + r2*v2*p) % N)
    sol.append((-r1*v1*q - r2*v2*p) % N)

    # check all 4 solutions
    counter_m1 = 0
    counter_p1 = 0
    for i in sol:
        assert(i*i % N == x2)
        j = jacobi_symbol(i, N)
        if j == -1:
            counter_m1 += 1
        if j == +1:
            counter_p1 += 1

    # Two solutions should have Jacobi symbol +1
    # Other two should have -1
    assert(counter_m1 == 2)
    assert(counter_p1 == 2)

    return sol


def generate_N():
    p = getPrime(80)
    while p % 4 != 3:
        p = getPrime(80)

    q = getPrime(80)
    while q % 4 != 3:
        q = getPrime(80)
    return p*q, (p, q)


N, factors = generate_N()

print(f"N = {N}")

x2 = int(input("x2 ? "))

solutions = solve(factors, x2)

guess = random.choice([-1, 1])
print(f"j_guess = {guess}")

x = int(input("x ? "))

if (x*x) % N == x2:
    J = jacobi_symbol(x, N)
    print("Outcome = Heads" if guess == J else "Outcome = Tails")
else:
    print("Time to call The Judge.")
