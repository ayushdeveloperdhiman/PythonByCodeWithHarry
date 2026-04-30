name = "Ayush"
friend = "Rohan"
anotherFriend = 'Lovish'
# apple = "He said, \"I want to eat an apple\"."
# apple = 'He said,' \
# 'Hi, Ayush ' \
# 'I am good ' \
# ' "I want to eat an apple".'

apple = '''He said,
Hi, Ayush
I am good
"I want to eat an apple".
'''

str = """Whispers of the Wind
The wind sings low through quiet trees,
A whisper carried on the breeze.
It speaks of lands both far and near,
A soothing voice that all can hear.
It shakes the leaves, it skips the grass,
And sings to us, then softly passes. """

print("Hello, " + name)
# print(apple)
print(str)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) Throws an error

print("Let's use a for loop\n")

for character in apple:
    print(character)

