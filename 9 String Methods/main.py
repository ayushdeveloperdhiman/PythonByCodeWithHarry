# Strings are immutable
a = "!!!Ayush!! !!!!!!!!! Ayush"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip('!'))
print(a.replace("Ayush", "John"))
print(a.split())
blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

str1 = "Welcome to the console!!!"
# print(len(str1))
# print(len(str1.center(50)))
print(str1.center(50))
print(a.count("Ayush"))
print(str1.endswith("!!!"))
print(str1.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find('is'))
print(str1.find('ishh'))
print(str1.index('is'))
# print(str1.index('ishh'))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())

str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

# str1 = "We wish you a Merry Christmas\n"
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())

str1 = "                " #using Spacebar
print(str1.isspace())
str2 = "                " #using Tab
print(str2.isspace())

str1 = "World Health Organization"
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is an Interpreted Language"
print(str1.startswith("Python"))
print(str1.swapcase())

str1 = "His name is Dan. He is an honest man."
print(str1.title())