# Find unit digit of a number
def unit_digit(n):
    digits = 1
    temp_n = n
    while n >= 10:
        n /= 10
        digits += 1
    n = temp_n
    while digits > 1:
        n -= n % (10 ** digits)
        digits -= 1
    return n


# Check whether a number is prime
def check_if_prime(n):
    try:
        n = int(n)
        # n equals 2 or 3
        if n == 2 or n == 3:
            return True
        # n is divisible by two or three
        if n % 2 == 0 or n % 3 == 0:
            return False
        # n is odd
        else:
            i = 5
            while i ** 2 <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
    except ValueError:
        return False


# Check whether a number is prime generating
def check_if_prime_gen(n):
    count = 1
    while count <= int(n ** 0.5) + 1:
        if n % count == 0:
            if not check_if_prime(count + n // count):
                return False
        count += 1
    return True


def main():
    all_int = 2
    total_sum = 1
    while all_int <= 100000000:
        if check_if_prime_gen(all_int):
            total_sum += all_int
        all_int += 4
    print(total_sum)
    return


main()
