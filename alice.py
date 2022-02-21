from Crypto.Util.number import getRandomRange
from sympy.ntheory.residue_ntheory import jacobi_symbol

N = int(input("N ? "))

x = getRandomRange(2, N)
x2 = (x*x) % N
J = jacobi_symbol(x, N)

print(f"x2 = {x2}")

guess = int(input("j_guess ? "))

print(f"x = {x}")
print("Outcome = Heads" if guess == J else "Outcome = Tails")
