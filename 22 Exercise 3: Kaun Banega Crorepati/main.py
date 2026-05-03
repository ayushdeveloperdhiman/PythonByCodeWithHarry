print("Welcome to Kaun Banega Crorepati.\n\n")
questions = [
    [
        "Which of the following is a valid way to comment in Python?",
        "What is the result of the following expression in Python: 5 + 2 * 3",
        "What will be the output of the following code snippet?\n a = 5\nb = 2\nprint(a // b)\n",
        "How do you concatenate two strings in Python?",
        "What is the purpose of the __dict__ attribute in Python?",
        "How do you create a multiline string in Python?",
        "How do you convert a floating-point number to an integer in Python?",
        "How do you convert a list of strings to a single string in Python?"
    ],

    [
        [
            "A. // This is a comment",
            "B. # This is a comment",
            "C. <!-- This is a comment -->",
            "D. /* This is a comment */"
        ],

        [
            "A. 21",
            "B. 17",
            "C. 11",
            "D. 1"
        ],

        [
            "A. 2.5",
            "B. 2",
            "C. 2.0",
            "D. 2.00"
        ],

        [
            "A. str1 . str2",
            "B. str1 + str2",
            "C. str1 , str2",
            "D. concat(str1, str2)"
        ],

        [
            "A. To access the dictionary of a list",
            "B. To store the attributes of an object",
            "C. To define a dictionary in Python",
            "D. To convert a dictionary to a list"
        ],

        [
            'A. "This is a multiline string"',
            "B. 'This is a multiline string'",
            'C. """This is a multiline string"""',
            "D. (a and b)"
        ],

        [
            "A. int(number)",
            "B. float_to_int(number)",
            "C. number.int()",
            "D. convert(int, number)"
        ],

        [
            'A. "".join(list)',
            "B. str(list)",
            "C. convert(list, str)",
            'D. " ".join(list)'
        ]
    ],

    ['B', 'C', 'B', 'B', 'B', 'C', 'A', 'D']
]
score = 0
question_count = 1
for question in questions[0]:
    print('Q'+str(question_count)+'.',question, end="\n\n")
    count = 0
    for options in questions[1][question_count-1]:
        if count == 4:
            break
        print(options)
        count += 1
    answer = input("Enter (A,B,C or D only): ").lower()
    if answer == questions[2][question_count-1].lower():
        score += 1
        print("Correct Answer")
    else:
        print("Wrong Answer")
    print()
    question_count += 1  

print("You Scored:", score)
