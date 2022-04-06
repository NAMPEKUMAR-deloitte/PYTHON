def Lambda():
    print("Problem1:Using a lambda function take inputs as 4 integers and give the output for equation ax^2+bx+c")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    x = int(input("Enter x: "))
    res = lambda a, b, c, x: (a * x ** 2 + b * x + c)
    print(res(a, b, c, x))

def CountofA():
    print("Problem2:Using map() function and lambda and count() function create a list consisted of the number of occurence of both letters: A and a")
    list1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
    print(list1)
    list2 = list(map(lambda word: word.count("A"), list1))
    print("Number of 'A' :")
    print(list2)
    list3 = list(map(lambda word: word.count("a"), list1))
    print("Number of 'a' :")
    print(list3)
    list4 = list(map(lambda x,y:[x.count("A"),y.count("a")],list1,list1))
    print("Number of 'A' and 'a':")
    print(list4)

Lambda()
print("-------------------------------------------------------------------------")
CountofA()