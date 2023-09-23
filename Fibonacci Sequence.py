def is_perfect_square(x):
    sqrt_x = int(x**0.5)
    return sqrt_x * sqrt_x == x


def is_fibonacci(n):
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)


test_cases = [5, 6, 7, 8]

for N in test_cases:
    if is_fibonacci(N):
        print("Yes")
    else:
        print("No")
