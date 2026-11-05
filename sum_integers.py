DEFAULT_N = 100
def sum_first_n_loop(n):
    """Return 1 + 2 + ... + n using direct accumulation.
    The function assumes that n is a nonnegative integer.
    """
    total = 0
    for k in range(1, n + 1):
        total += k
    return total
def main():
    result = sum_first_n_loop(DEFAULT_N)
    print(f"sum(1, ..., {DEFAULT_N}) = {result}")
if __name__ == "__main__":
    main()

