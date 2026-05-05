def is_prime(n: int) -> bool:
    """Check if a number is Prime."""
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

PRIME_NUMBERS = [i for i in range(1000000) if is_prime(i)]

def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    if number < 0:
        raise ValueError('there are no negative prime')
    return PRIME_NUMBERS[number-1]
