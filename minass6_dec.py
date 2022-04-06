def fib(number):
    first_number = 0
    second_number = 1
    if number == 1:
        print(first_number)
    else:
        print(first_number)
        print(second_number)
        for i in range(2, number):
            return_number = first_number + second_number
            first_number = second_number
            second_number = return_number
            yield return_number


class Decorator:

    number = int(input("Enter the value : "))
    values = fib(number)
    print("The first ", number, " Fibonacci numbers are ")
    for i in values:
        print(i)