DEFAULT_N = 10
def sum_first_n_loop(n):
    """Return the sum 1 + 2 + ... + n using a loop."""
    total = 0
    for k in range(1, n + 1):
        total += k
    return total
def main():
    result = sum_first_n_loop(DEFAULT_N)
    print(f"sum(1, ..., {DEFAULT_N}) = {result}")
if __name__ == "__main__":
    main()

