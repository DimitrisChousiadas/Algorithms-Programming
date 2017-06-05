"""
    The super digit of an integer N can be calculated using the following rules:
    - If N has only one digit, then its super digit is N.
    - Otherwise, the super digit of N is equal to the super digit of the digit-sum of N (the digit-sum of N is defined as the sum of its digits).

    Given a number N and a numbers K, we want to calculate the super digit of P,
    where P is the number that created by concatenating N with itself K times.
    E.g. if N = 123 and K = 4 then P = 123123123123

    We can do that in two ways:
        - calculate the super digit of n, multiply that with K and, then, find the super digit of that result.
        - observe that the super digit of a number x is x mod 9 (or 9, if x mod 9 == 0).
          Then, the super digit of P will be N*K mod 9 (or 9, if N*K mod 9 == 0).
"""

def super_digit (n, acc):
    if n == 0 and acc < 10:
        return acc
    elif n == 0:
        return super_digit(acc, 0)
    else:
        return super_digit(n // 10, acc + n % 10)

n, k = map(int, input().strip().split())
print(super_digit(k * super_digit(n, 0), 0))
print(n*k % 9 if n*k % 9 else 9)
