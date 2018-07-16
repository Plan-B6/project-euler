def main():
    count = 1
    answer = 0
    while count < 1000:
        if count % 3 == 0:
            answer += count
        if count % 5 == 0 and count % 3 != 0:
            answer += count
        count += 1
    print(answer)


main()
