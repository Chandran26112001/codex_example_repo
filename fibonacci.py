"""Print a Fibonacci series with a user-specified number of terms."""


def fibonacci(count: int) -> list[int]:
    """Return the first ``count`` numbers in the Fibonacci series.

    Args:
        count: Number of terms to generate. It must be positive.

    Raises:
        ValueError: If ``count`` is not positive.
    """
    if count <= 0:
        raise ValueError("count must be positive")

    series: list[int] = []
    first, second = 0, 1

    for _ in range(count):
        series.append(first)
        first, second = second, first + second

    return series


def main() -> None:
    """Read the term count from standard input and print the series."""
    try:
        count = int(input("Enter the number of terms: "))
    except ValueError:
        print("Please enter a whole number.")
        return

    try:
        series = fibonacci(count)
    except ValueError:
        print("Please enter a positive number.")
        return

    print("Fibonacci series:", *series)


if __name__ == "__main__":
    main()
