from random import randint
from random import choice


tasks_passed = 0
correct_answers = 0


def task_type1():
    operands = "+-*"
    a = randint(2, 9)
    b = randint(2, 9)
    operator = choice(operands)
    print(str(a), operator, str(b))
    for i in operator:
        if i == "+":
            return a + b
        elif i == "-":
            return a - b
        else:
            return a * b


def task_type2():
    a = randint(11, 29)
    print(a)
    return a * a


def ask_user(correct_answer):
    global correct_answers, tasks_passed
    try:
        user_answer = int(input())
    except ValueError:
        print("Incorrect format")
        return False
    else:
        if correct_answer == user_answer:
            print("Right!")
            correct_answers += 1
            tasks_passed += 1
            return True
        else:
            print("Wrong!")
            tasks_passed += 1
            return True


difficulty_level = False
while difficulty_level is False:
    try:
        difficulty_level = int(input("1 - simple operations with numbers 2-9\n"
                                     "2 - integral squares 11-29\n"))
    except ValueError:
        print("Incorrect format")
        difficulty_level = False
    if difficulty_level > 2 or difficulty_level < 1:
        difficulty_level = False

while tasks_passed < 5:
    if difficulty_level == 1:
        correct_answer = task_type1()
        while ask_user(correct_answer) is False:
            ask_user(correct_answer)
    else:
        correct_answer = task_type2()
        while ask_user(correct_answer) is False:
            ask_user(correct_answer)

if difficulty_level == 1:
    difficulty_level_description = 'simple operations with numbers 2-9'
else:
    difficulty_level_description = 'integral squares 11-29'
save_result = input(f"Your mark is {correct_answers}/5. Would you like to save your result to the file? Enter yes or no.\n")
correct_answer_yes = ["Yes", "YES", "yes", "y", "Y"]
if save_result in correct_answer_yes:
    user_name = input("What is your name?\n")
    file = open('results.txt', 'a', encoding='utf-8')
    file.write(f'{user_name}: {correct_answers}/5 in level {difficulty_level} ({difficulty_level_description}).\n')
    file.close()
    print('The results are saved in "results.txt".')
