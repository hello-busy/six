#!/usr/bin/env python3
"""
Six - A simple program demonstrating various aspects of the number 6
"""

def main():
    """Main function to demonstrate the number 6"""
    print("Welcome to Six!")
    print("=" * 20)
    
    # Basic number 6
    print(f"The number: {6}")
    
    # Mathematical properties of 6
    print(f"6 is a perfect number: {is_perfect_number(6)}")
    print(f"6 factorial: {factorial(6)}")
    print(f"6 squared: {6 ** 2}")
    print(f"6 cubed: {6 ** 3}")
    
    # Divisors of 6
    divisors = get_divisors(6)
    print(f"Divisors of 6: {divisors}")
    
    # Sum of divisors (excluding the number itself)
    proper_divisors = [d for d in divisors if d != 6]
    print(f"Sum of proper divisors: {sum(proper_divisors)}")


def is_perfect_number(n):
    """Check if a number is perfect (sum of proper divisors equals the number)"""
    if n <= 1:
        return False
    
    divisors = get_divisors(n)
    proper_divisors = [d for d in divisors if d != n]
    return sum(proper_divisors) == n


def factorial(n):
    """Calculate factorial of a number"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def get_divisors(n):
    """Get all divisors of a number"""
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


if __name__ == "__main__":
    main()