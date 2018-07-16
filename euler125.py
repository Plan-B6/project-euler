# Returns the sum of consecutive squares from a^2 to n^2 inclusive
def sum_of_consec_squares(a, n):
    a_sum = a * (a - 1) * (2 * a - 1) // 6
    n_sum = n * (n + 1) * (2 * n + 1) // 6
    return n_sum - a_sum


def get_upper_bound(n):
    return int(((n - 1) / 2) ** 0.5) + 1


def get_digit_num(n):
    num_list = [int(i) for i in str(n)]
    return len(num_list)


def get_mid_digit(n):
    num_list = [int(i) for i in str(n)]
    return num_list[len(num_list) // 2]


def check_if_palindromic(n):
    num_list = [int(i) for i in str(n)]
    shift = 0
    length = len(num_list)
    for i in range(length // 2):
        if num_list[i] != num_list[length - shift - 1]:
            return False
        shift += 1
    return True


def check_if_square_sum(n):
    upper_bound = get_upper_bound(n)
    for i in range(1, upper_bound + 1):
        for j in range(1, upper_bound + 1):
            if i >= j:
                continue
            sum = sum_of_consec_squares(i, j)
            if sum > n:
                break
            elif sum == n:
                return True
    return False


def main():
    total_sum = 0
    j = 1
    while j <= 10 ** 8:
        if check_if_palindromic(j):
            if check_if_square_sum(j):
                total_sum += j
                print(j)
            digit_num = get_digit_num(j)
            if get_mid_digit(j) == 9:
                j += 1
                continue
            if digit_num % 2 == 1:
                j += 10 ** (digit_num // 2)
            else:
                j += 10 ** (digit_num // 2) + 10 ** (digit_num // 2 - 1)
        else:
            j += 1
    print(total_sum)
    return


main()