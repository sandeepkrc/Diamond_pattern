def print_prime_star_pattern(n):
    """
    Prints a symmetrical star pattern for a given number `n`.

    The pattern consists of two parts:
    - An upper half, where the number of stars increases with each row.
    - A lower half, where the number of stars decreases with each row.

    Args:
        n (int): The number of rows for the upper half of the pattern.

    Example for n = 4:
       *
      ***
     *****
    *******
     *****
      ***
       *
    """

    # Upper half of the pattern
    for i in range(n):
        spaces = " " * (n - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)

    # Lower half of the pattern
    for i in range(n - 1):
        spaces = " " * (i + 1)
        stars = "*" * (2 * (n - i - 2) + 1)
        print(spaces + stars)

if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    print_prime_star_pattern(n)
