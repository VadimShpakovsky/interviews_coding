def sum_digits(number):
    result = 0
    for c in str(number):
        result += int(c)

    return result


def max_pair_sum(numbers):
    max_sum = -1
    for i, n1 in enumerate(numbers):
        for j, n2 in enumerate(numbers):
            if j > i and n1 + n2 > max_sum:
                max_sum = n1 + n2

    return max_sum


def collect_numbers_sums(numbers):
    sums = dict()

    for number in numbers:
        number_sum = sum_digits(number)
        if number_sum in sums:
            sums[number_sum].append(number)
        else:
            sums[number_sum] = [number]

    return sums


def solution(numbers):
    sums = collect_numbers_sums(numbers)

    max_sum = -1
    for same_sum_numbers in sums.values():
        if len(same_sum_numbers) > 1:
            _sum = max_pair_sum(same_sum_numbers)
            max_sum = max(_sum, max_sum)

    return max_sum
