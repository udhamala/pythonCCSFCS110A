"""
Assignment Title: Double Up
Created by: Uttam Dhamala

This program will take a number between 0 and 20 from users
and double up the numbers starting at 1 up to the number of
user choice.  If user input is out of range, program will ask
user to put another number.
Program will print the doubled up numbers from 1 to the user
choice number and also print the sum of doubled up numbers.

"""


def double_up(upper_num):
    sum = 0
    while upper_num > 0:
        new_num = upper_num * 2
        print("Double up ", upper_num, " = ", new_num)
        upper_num -= 1
        sum += new_num
    print("Total = ", sum)


def main():
    upper_num = int(input("Please choose your number: "))
    while (upper_num > 20) or (upper_num < 0):
        upper_num = int(input("Please choose the number between 0 & 20: "))

    while (upper_num < 20) or (upper_num > 0):
        double_up(upper_num)
        break


main()

"""
Sample Runs
-----------Test run with number out of range:-------------
/Users/USA/Desktop/PythonHomeWrk/venv/bin/python /Users/USA/Desktop/PythonHomeWrk/double_up.py
Please choose your number: 23
Please choose the number between 0 & 20: 25
Please choose the number between 0 & 20: -3
Please choose the number between 0 & 20: 

------------Test run with number in range--------------
/Users/USA/Desktop/PythonHomeWrk/venv/bin/python /Users/USA/Desktop/PythonHomeWrk/double_up.py
Please choose your number: 10
Double up  10  =  20
Double up  9  =  18
Double up  8  =  16
Double up  7  =  14
Double up  6  =  12
Double up  5  =  10
Double up  4  =  8
Double up  3  =  6
Double up  2  =  4
Double up  1  =  2
Total =  110

Process finished with exit code 0
"""
