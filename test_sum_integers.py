from sum_integers import sum_first_n_loop
def main():
    test_cases = {
        0: 0,
        1: 1,
        5: 15,
        10: 55,
        100: 5050,
    }
    for n, expected in test_cases.items():
        computed = sum_first_n_loop(n)
        assert computed == expected, (
            f"n={n}: expected {expected}, obtained {computed}"
        )
    print("All tests passed.")
if __name__ == "__main__":
    main()
