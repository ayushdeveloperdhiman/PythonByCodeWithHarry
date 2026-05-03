tup = (1, 5, 76, 342, 32, "green", True)
# tup[0] = 90
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

# tup1 = (1)
# print(type(tup1), tup1)

# tup1 = (1,)
# print(type(tup1), tup1)

if 342 in tup:
    print("Yes 342 is present in this tuple")

tup2 = tup[1:4]
print(tup2)