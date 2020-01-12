"""
Title: Payroll Program
This payroll Program will calculate the hours and pay rate for employees
and display the two dimension list of employees, with employee ID, Name,
Hours worked, Pay rate and Total wages. Any number of employee record can
be displayed upon user request.
Created by: Uttam Dhamala
"""


def main():
    payroll = hire()
    paycheck(payroll)


def paycheck(payroll):
    print(payroll)


def hire():
    payroll = []
    new_hire = True
    while new_hire:
        response = input("Are you adding new_hire? Type 'Y' for Yes and 'N' for No: ")
        if response == "Y":
            employee_id = len(payroll) + 1
            employee_name = input("Name: ")
            hours = int(input("Hours Worked: "))
            pay_rate = int(input("Pay Rate: "))
            wages = pay_rate * hours
            employees = [employee_id, employee_name, hours, pay_rate, wages]
            payroll.append(employees)
        else:
            new_hire = False
    return payroll


main()

"""
---------------Test Run with multiple employees---------------------
/Users/USA/Desktop/PythonHomeWrk/venv/bin/python /Users/USA/Desktop/PythonHomeWrk/payrollProgram.py
Are you adding new_hire? Type 'Y' for Yes and 'N' for No: Y
Name: Uttam 
Hours Worked: 40
Pay Rate: 26
Are you adding new_hire? Type 'Y' for Yes and 'N' for No: Y
Name: John
Hours Worked: 38
Pay Rate: 25
Are you adding new_hire? Type 'Y' for Yes and 'N' for No: Y
Name: Sapati
Hours Worked: 39
Pay Rate: 26
Are you adding new_hire? Type 'Y' for Yes and 'N' for No: N
[[1, 'Uttam ', 40, 26, 1040], [2, 'John', 38, 25, 950], [3, 'Sapati', 39, 26, 1014]]

Process finished with exit code 0
--------------------------------------------------------
--------------Test run with no employee-----------------
/Users/USA/Desktop/PythonHomeWrk/venv/bin/python /Users/USA/Desktop/PythonHomeWrk/payrollProgram.py
Are you adding new_hire? Type 'Y' for Yes and 'N' for No: N
[]

Process finished with exit code 0
---------------------------------------------------------
--------------Test run with 1 employee-------------------
/Users/USA/Desktop/PythonHomeWrk/venv/bin/python /Users/USA/Desktop/PythonHomeWrk/payrollProgram.py
Are you adding new_hire? Type 'Y' for Yes and 'N' for No: Y
Name: Sushi
Hours Worked: 40
Pay Rate: 29
Are you adding new_hire? Type 'Y' for Yes and 'N' for No: N
[[1, 'Sushi', 40, 29, 1160]]

Process finished with exit code 0
"""
