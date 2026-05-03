# letter = "Hey my name is {} and I am from {}"
# country = "India"
# name = "Ayush"

# print(letter.format(name,country))

letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Ayush"

print(letter.format(country, name))

print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")

# txt = "For only {price: .2f} dollars!"
# print(txt.format(price = 49.09999))
price = 49.09999
txt = f"For only {price: .2f} dollars!"
print(txt)

print(f'{2 * 30}')