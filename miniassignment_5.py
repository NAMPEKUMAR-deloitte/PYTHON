from functools import reduce

print("Problem 1 : Convert a number to positive if it's negative in the list. Only pass those that are converted from negative to positive to the new list.")
lst1 = [-1000, 500, -600, 700, 5000, -90000, -17500]
negNum = list(map(lambda x: -x, list(filter((lambda x: x < 0), lst1))))
print(negNum)
print("---------")


print("Problem 2 :Take the first two values, run the function on them. Then take the result and the next value and have a multiplication between them. etc. When no more values are left, return the last result")
lst1 = [-1000, 500, -600, 700, 5000, -90000, -17500]
print(reduce(lambda x, y: x * y, lst1))
print("---------")


print("Problem 3 :Using zip and dict functions create a dictionary which has its key-value pairs coming from lst1 and lst2.")
lst1 = ["Netflix", "Hulu", "Sling", "Hbo"]
lst2 = [198, 166, 237, 125]
res= dict(zip(lst1, lst2))
print(dict(res))
print("---------")