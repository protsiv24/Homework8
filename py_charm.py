def count_same_digits(number):
    digit_counts = [0] * 10
    while number > 0:
        digit = number % 10
        digit_counts[digit] += 1
        number //= 10

def test_function():
    even_numbers = []
    for num in range(1, 21):
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
result = test_function()
print(result)