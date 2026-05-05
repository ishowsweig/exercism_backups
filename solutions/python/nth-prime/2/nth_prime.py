"""Module aids in identifying and accessing prime numbers."""
def is_prime(number: int) -> bool:
    """Check if a number is Prime."""
    if number < 2: return False
    if number == 2: return True
    if number % 2 == 0: return False
    for num in range(2, int(number**0.5)+1):
        if number % num == 0:
            return False
    return True

PRIME_NUMBERS = [number for number in range(1000000) if is_prime(number)]

def prime(number):
    """Determines the nth prime number, where n is number."""
    if number == 0:
        raise ValueError('there is no zeroth prime')
    if number < 0:
        raise ValueError('there are no negative prime')
    return PRIME_NUMBERS[number-1]
