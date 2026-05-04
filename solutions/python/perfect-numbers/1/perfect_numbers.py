def aliquot_sum(n):

    asum = 0
    for i in range(1, n):
        if n % i == 0:
            asum += i
    return asum

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError('Classification is only possible for positive integers.')
    asum = aliquot_sum(number)
    if asum == number:
        return "perfect"
    if asum < number:
        return 'deficient'
    else:
        return 'abundant'

