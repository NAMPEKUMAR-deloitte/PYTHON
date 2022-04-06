from collections import Counter
#1
print("Return all the duplicate values from list of arraylist: ")
arr = [ [1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4] ]
for i in arr:
    d=dict(Counter(i))
    for j in d:
        if d[j]>1:
            print(j,"->",d[j],end=" ")
    print()
print()

#2
list1 = ["Hello ", "take "]

list2 = ["Dear", "Sir"]
list3 = []
list3.append(list1[0]+list2[0])
list3.append(list1[0]+list2[1])
list3.append(list1[1]+list2[0])
list3.append(list1[1]+list2[1])
print(list3)
#3
print("Extend list")
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)
print(list1)