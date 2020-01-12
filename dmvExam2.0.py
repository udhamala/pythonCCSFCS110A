"""
Program name: Dmv Exam Version 2.0
Created by: Uttam Dhamala
Program DMV Exam Version 2.0  asks questions to users and ask to choose correct answers
from given choices. If user choose incorrect format of input, then
user will be given another chance to put their answer.
If user put correct format of answer program will calculate the number of
correct and incorrect answers and gives user the result with their
pass/fail status and also displays the number and answers correctly and
incorrectly answered. Addition to Version 1, this version will get correct answer
list from dmvExamAnswers.txt file. This version will record the result to resultLog.txt file.
"""


def main():
    questions()


def questions():
    sum = 0  # Calculates the numbers of questions
    answers = []  # Stores user answers
    correct_ans_list = []  # Stores correct answers
    wrong_ans_list = []  # Stores wrong answers
    user_correct_answers = []  # Stores index numbers +1 for correct answers, ie, question numbers
    user_wrong_answers = []  # Stores index numbers +1 for wrong answers, ie, question numbers
    correct_pair = []  # Stores pair of question number and answer for correct answers
    wrong_pair = []  # Stores pair of question number and answer for wrong answers
    num_correct_ans = 0  # Accumulates the number of correct answers
    num_wrong_ans = 0  # Accumulates the number of wrong answers
    correct_answers = []
    #Reading the answer from dmvExamAnswers.txt
    with open('dmvExamAnswers.txt', 'r') as f:
        line_list = list(f.read())
    for k in line_list:
        new_k = k.rstrip('\n')
        correct_answers.append(new_k)
    # First while loop for questions:
    while sum < 20:
        answer = input(sum + 1)
        if answer != "A" and \
                answer != "B" and \
                answer != "C" and \
                answer != "D":
            print("Input Error: ")
            print("Please choose from given input. A, B, C, D: ")
        else:
            sum += 1
            answers.append(answer)
    for i in range(len(answers)):
        if answers[i] == correct_answers[i]:
            num_correct_ans += 1
            user_correct_answers.append(i + 1)
            correct_ans_list.append(answers[i])
        else:
            num_wrong_ans += 1
            user_wrong_answers.append(i + 1)
            wrong_ans_list.append(answers[i])
    percentage = num_correct_ans / len(answers) * 100
    print("You answered", percentage, "% correctly.")
    # Creates pair of correct answers with Question #s.
    for idx, item in zip(user_correct_answers, correct_ans_list):
        correct_pair.extend((idx, item))
    print(correct_pair)
    if num_correct_ans >= 15:
        print("Congratulations you passed.")
        my_file = open('resultLog.txt', 'a')
        my_file.write("You answered " + str(percentage) + "% correctly.\n")
        my_file.write("Congratulations you passed.\n")
        my_file.close()
    else:
        print("Sorry, you didn't pass. Need at least 15 correct answers (75%) to pass. ")
        my_file = open('resultLog.txt', 'a')
        my_file.write("You answered " + str(percentage) + "% correctly.\n")
        my_file.write("Sorry, you didn't pass. Need at least 15 correct answers (75%) to pass. \n")
        my_file.close()
    print("You answered following", num_wrong_ans, "questions incorrectly.")
    # Creates pair of incorrect answers with Question numbers.
    for idx, item in zip(user_wrong_answers, wrong_ans_list):
        wrong_pair.extend((idx, item))
    print(wrong_pair)


main()

"""
----------Test run with wrong and right format of inputs------------
/Users/USA/Desktop/PythonHomeWrk/venv/bin/python /Users/USA/Desktop/PythonHomeWrk/dmvExam.py
1A
2D
3C
4B
51
Input Error: 
Please choose from given input. A, B, C, D: 
5F
Input Error: 
Please choose from given input. A, B, C, D: 
5%
Input Error: 
Please choose from given input. A, B, C, D: 
5A
6D
7F
Input Error: 
Please choose from given input. A, B, C, D: 
7Z
Input Error: 
Please choose from given input. A, B, C, D: 
7G
Input Error: 
Please choose from given input. A, B, C, D: 
7A
8D
9C
10B
11D
12G
Input Error: 
Please choose from given input. A, B, C, D: 
12A
13#
Input Error: 
Please choose from given input. A, B, C, D: 
131
Input Error: 
Please choose from given input. A, B, C, D: 
134
Input Error: 
Please choose from given input. A, B, C, D: 
135
Input Error: 
Please choose from given input. A, B, C, D: 
13A
14D
15C
16F
Input Error: 
Please choose from given input. A, B, C, D: 
16B
17A
18A
19A
20D
You answered 10.0 % correctly.
[2, 'D', 9, 'C']
Sorry, you didn't pass. Need at least 15 correct answers (75%) to pass. 
You answered following 18 questions incorrectly.
[1, 'A', 3, 'C', 4, 'B', 5, 'A', 6, 'D', 7, 'A', 8, 'D', 10, 'B', 11, 'D', 12, 'A', 13, 'A', 14, 'D', 15, 'C', 16, 'B', 17, 'A', 18, 'A', 19, 'A', 20, 'D']

Process finished with exit code 0

----------------Test run with all correct answers--------------------
/Users/USA/Desktop/PythonHomeWrk/venv/bin/python /Users/USA/Desktop/PythonHomeWrk/dmvExam.py
1B
2D
3A
4A
5C
6A
7B
8A
9C
10D
11B
12C
13D
14A
15D
16C
17C
18B
19D
20A
You answered 100.0 % correctly.
[1, 'B', 2, 'D', 3, 'A', 4, 'A', 5, 'C', 6, 'A', 7, 'B', 8, 'A', 9, 'C', 10, 'D', 11, 'B', 12, 'C', 13, 'D', 14, 'A', 15, 'D', 16, 'C', 17, 'C', 18, 'B', 19, 'D', 20, 'A']
Congratulations you passed.
You answered following 0 questions incorrectly.
[]

Process finished with exit code 0

...................Result log of different outputs..................
You answered 90.0% correctly.
Congratulations you passed.
You answered 15.0% correctly.
Sorry, you didn't pass. Need at least 15 correct answers (75%) to pass. 

...................Correct answers list on .txt file................
BDAACABACDBCDADCCBDA

"""
