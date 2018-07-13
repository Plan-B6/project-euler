'''
An infinite number of people (numbered 1, 2, 3, etc.) are lined up to get a room at Hilbert's newest infinite hotel.
The hotel contains an infinite number of floors (numbered 1, 2, 3, etc.), and each floor contains an infinite number of rooms (numbered 1, 2, 3, etc.).

Initially the hotel is empty. Hilbert declares a rule on how the nth person is assigned a room: person n gets the first vacant room in the lowest numbered floor satisfying either of the following:

the floor is empty
the floor is not empty, and if the latest person taking a room in that floor is person m, then m + n is a perfect square
Person 1 gets room 1 in floor 1 since floor 1 is empty.
Person 2 does not get room 2 in floor 1 since 1 + 2 = 3 is not a perfect square.
Person 2 instead gets room 1 in floor 2 since floor 2 is empty.
Person 3 gets room 2 in floor 1 since 1 + 3 = 4 is a perfect square.

Eventually, every person in the line gets a room in the hotel.

Define P(f, r) to be n if person n occupies room r in floor f, and 0 if no person occupies the room. Here are a few examples:
P(1, 1) = 1
P(1, 2) = 3
P(2, 1) = 2
P(10, 20) = 440
P(25, 75) = 4863
P(99, 100) = 19454

Find the sum of all P(f, r) for all positive f and r such that f × r = 71328803586048 and give the last 8 digits as your answer.
'''


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
