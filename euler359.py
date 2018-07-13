# Find all factors of a number
def find_factors(n):
    f_list = []
    f_list_2 = []
    count = 1
    while count <= int(n ** 0.5):
        if n % count == 0:
            f_list.append(count)
        count += 1
    for i in f_list:
        if n // i != i:
            f_list_2.append(n // i)
    f_list.extend(f_list_2)
    return f_list


# Returns the nth triangle number
def get_tri_number(n):
    return n * (n + 1) // 2


# Returns the person occupying room r on floor f
def find_person(f, r):
    if f == 1:
        return get_tri_number(r)
    else:
        shift = (f // 2) * 2 - 1
        base_person = get_tri_number(r + shift)
        if f % 2 == r % 2:
            return base_person + f // 2
        else:
            return base_person - f // 2


def main():
    sum = 0
    for i in find_factors(71328803586048):
        sum += find_person(i, 71328803586048 // i)
    print(sum)
    return


main()
