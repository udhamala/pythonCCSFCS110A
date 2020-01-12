# correct_answers_list = []
# line_list = []
# revised_correct_answers_list = []
# with open('dmvExam.txt', 'r') as f:
#     line_list = list(f.read())
# print(line_list)
#     # for line in f:
#     #     correct_answers_list.append(line)
# for k in line_list:
#     new_k = k.rstrip('\n')
#     revised_correct_answers_list.append(new_k)
# print(revised_correct_answers_list)
correct_answers = ["A", "D", "C", "A", "D", "B"]
question_numbers = []
answers_with_numbers = 2 + 2
# for k in range(len(correct_answers)):
#     question_numbers.append(k + 1)
#
# for numbers, answers in zip(question_numbers, correct_answers):
#     answers_with_numbers.extend((numbers, answers))
# # print(answers_with_numbers)
# # print(correct_answers_list)
# # revised_correct_answers_list = revised_correct_answers_list[0]
# for k in revised_correct_answers_list:
#     final_correct_answers_list.append(k)
# print(correct_answers_list)
# print(revised_correct_answers_list)
# print(final_correct_answers_list)
my_file = open('resultLog.txt', 'w')

my_file.write(str(answers_with_numbers))
my_file.close()


#my_file.writelines(["%s\r\n" % item for item in answers_with_numbers])
