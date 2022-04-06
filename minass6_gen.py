def smart_multiply(fun):
    def inner(N1, N2):
        print("The Multiplication of the", N1, "and", N2, "are", N1 * N2)
        N1, N2 = N2, N1
        return fun(N1, N2)

    return inner


@smart_multiply
def multiply(N1, N2):
    print("The Multiplication of the", N1, "and", N2, "are", N1 * N2)


class Generator:
    number1 = int(input("Enter the number1: "))
    number2 = int(input("Enter the number2: "))
    multiply(number1, number2)