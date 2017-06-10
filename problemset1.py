import math


def ith_prime(ith):
    i = 1
    result = 2
    counter = 1
    while i < ith:
        if is_prime(2*counter + 1):
            result = 2*counter + 1
            i += 1

        counter += 1

    return result


def is_prime(n):
    result = True
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            result = False

    return result


def sum_log_primes(n):
    sum_log = math.log(2)
    counter = 1
    while 2*counter + 1 < n:
        if is_prime(2*counter + 1):
            sum_log += math.log(2*counter + 1)

        counter += 1

    print(sum_log, n, sum_log/n)

    return None

