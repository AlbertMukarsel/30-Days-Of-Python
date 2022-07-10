
# Variables in Python
# Day 2: 30 days of python programming
from ast import Num


first_name = 'Alberto'
last_name = 'Mucarsel'
country = 'Ecuador'
city = 'Quito'
age = 25
is_married = False
skills = ['HTML', 'CSS', 'TS', 'Angular', 'Python']
person_info = {
    'firstname':'Alberto', 
    'lastname':'Mucarsel', 
    'country':'Ecuador',
    'city':'Quito'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Alberto', 'Mucarsel', 'Ecuador', 25, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

#Exercises: Level 2
num_one = 5
num_two= 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one**num_two
floor_division = num_one // num_two

