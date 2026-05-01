# def average(a=9,b=1):
#     print("The average is", (a+b)/2)

# average(4,6)
# average()
# average(1, 5)
# average(5)
# average(b=9)
# average(b = 9, a = 21)

# def name(fname, mname = "John", lname = "Whatson"):
#     print("Hello,", fname, mname, lname)

# name("Amy")

# def average(*numbers):
#     print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("Average is:", sum/len(numbers))

# average(5,5,6,7,4,5)


# def name(**name):
#     print(type(name))
#     print("Hello,", name['fname'], name['mname'], name['lname'])

# name(mname="Buchanan", lname= "Barnes", fname = 'James')

def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)

c = average(5,6,7,1)
print(c)