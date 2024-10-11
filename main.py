print("Hello world")
n = int(input("Введите число: "))

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} - високосный год.")
else:
    print(f"{year} - не високосный год.")

def is_palindrome(s):
    cleaned_s = ''.join(s.split()).lower()
    return cleaned_s == cleaned_s[::-1]
user_input = input("Введите строку или число: ")
if is_palindrome(user_input):
    print(f'"{user_input}" - палиндром.')
else:
    print(f'"{user_input}" - не палиндром.')
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
number = int(input("Введите неотрицательное целое число: "))
if number < 0:
    print("Факториал не определен для отрицательных чисел.")
else:
    print(f"Факториал {number} = {factorial_iterative(number)}")

def is_prime(n):
    if n <= 1:
        return False 
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
number = int(input("Введите целое число: "))
if is_prime(number):
    print(f"{number} - простое число.")
else:
    print(f"{number} - не простое число.")

def sum_of_digits(n):
    total = 0
    for digit in str(abs(n)):
        total += int(digit)
    return total
number = input("Введите целое число: ")
if number.lstrip('-').isdigit():
    digit_sum = sum_of_digits(int(number))
    print(f"Сумма всех цифр числа {number} = {digit_sum}.")
else:
    print("Пожалуйста, введите корректное целое число.")

def fibonacci_until(max_value):
    fib_sequence = []
    a, b = 0, 1
    while a <= max_value:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
max_value = int(input("Введите максимальное значение для последовательности Фибоначчи: "))
fib_sequence = fibonacci_until(max_value)
print(f"Последовательность Фибоначчи до {max_value}: {fib_sequence}")