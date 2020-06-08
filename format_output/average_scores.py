"""
Program: average_scores.py
Author: Lorenzo Quintanar
Last date modified: 06/07/2020

The purpose of this program is to find the average of three test scores.
The input is an integer representing the test score
The output is a float representing the average.
"""
def average():
    score1 = int(input('Enter first test score: '))
    score2 = int(input('Enter second test score: '))
    score3 = int(input('Enter third test score: '))
    average_scores = (score1 + score2 + score3) / 3.0
    return average_scores


if __name__ == '__main__':
    last_name = input('Enter your last name: ')
    first_name = input('Enter your first name: ')
    age = input('Enter your age: ')
    average_scores = average()
    print(f"{last_name},{first_name} age: {age} Average grade: {average_scores:.2f}")
    #ignore this line!!  print(last_name+','+first_name, 'Age:',age,'Average grade:',(f'{average_scores:.2f}'))

    #the program works as intended. We ask user for first and last name, their age, and ask user to
    #give us 3 test scores. Then we print the user input(last name, first name, age) and print the average.
    #test failed in the beginning but after writing code test successfully passes. The average is formatted to
    #only display 2 decimal points.
