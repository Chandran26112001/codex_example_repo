"""Tests for the Fibonacci series program."""

import unittest

from fibonacci import fibonacci


class FibonacciTests(unittest.TestCase):
    """Verify Fibonacci series generation and input validation."""

    def test_generates_requested_number_of_terms(self) -> None:
        self.assertEqual(fibonacci(7), [0, 1, 1, 2, 3, 5, 8])

    def test_single_term(self) -> None:
        self.assertEqual(fibonacci(1), [0])

    def test_rejects_non_positive_count(self) -> None:
        for count in (0, -1):
            with self.subTest(count=count), self.assertRaises(ValueError):
                fibonacci(count)


if __name__ == "__main__":
    unittest.main()
