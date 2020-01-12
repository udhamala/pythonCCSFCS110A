"""
Assignment title: Survivor Calculator
Name: Uttam Dhamala
About Project: This program will have two different functions
               to calculate the survival percentage and the
               survival total. First function will take the
               number of the people in the disaster zone and
               number of people killed as two parameters and
               return the percentage of survivors.
               Second function will take the number of people
               in the disaster zone and percentage of the people
               killed as two parameters and return the total number
               of people survived.
"""
def calculatePct(population, killed):
    survivors = population - killed
    percentage = survivors / population
    return round(percentage, 2)

def calculateTotal(population, killed_percentage):
    killed_number = population * killed_percentage
    survived = population - killed_number
    return round(survived)
# print(calculatePct(500, 20))
# print(calculatePct(100, 25))
# print(calculatePct(1524, 170))
# print(calculateTotal(734, .50))
# print(calculateTotal(100, .25))
# print(calculateTotal(1340, .30))


"""
/Users/USA/Desktop/PythonHomeWrk/venv/bin/python /Users/USA/Desktop/PythonHomeWrk/SurvivorCalculator.py
0.96
0.75
0.89
367
75
938

Process finished with exit code 0
"""

