def count_same_digits(number):
    digit_counts = [0] * 10
    while number > 0:
        digit = number % 10
        digit_counts[digit] += 1
        number //= 10