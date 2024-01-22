# states = ['Abia','Kaduna','Katsina','Lagos','Ogun','Oyo','Enugu','Rivers']
# # print(states[6])
# for x in states:
#     print(x)

# print (states)

# i = 0
# while i < len(states):
#     print(states[i])
#     i = i +1

#create a list of names then traverse through the list using for loops and while loops

# Country = ['Nigeria','America','Ghana','Brazil','Canada','France','Germany']
# for x in Country:
#     print(x)

# i = 0
# while i < len(Country):
#     print(Country[i])
#     i = i +1

#Create a list of ages then find the sum of all ages in the list and their average 

# ages = [5,6,8,36,38,81]
# for x in ages:
#     print(x)

# print(ages)

# i = 0
# sum = 0

# while i < len(ages):
#     sum += ages[i]
#     i += 1
# print(f'sum of ages {sum}')
# average = sum / len(ages)
# print(f'average of ages {average}')
# sum_result = 0
# sum_result = sum(ages)
# while i < len(ages):
#     print('sum',sum_result) 


# classes = [1,2,3,7,20,25,35,40,60]
# i = 0
# sum = 0
# while i < len(classes):
#     sum += classes[i] 
#     i += 1
# print(f'sum of classes {sum}')

# average = sum / len(classes)
# print(f'average of classes{average}')

# names = ['Jamal', 'Amal','Faeez','Hashim','Zainab']
# for x in names: 
#     print(x)

# i = 0
# while i < len(names):
    # print(names [i])
    # i += 1

#functions

# def subtract(a,b,c):
#     return a - b - c 
# print(subtract(8,4,2))

# print(subtract(10,8,6))

# def total (a,b,c):
#     return a + b + c 
# print(total (70,10,20))

# def add (x,y,z): 
#     return (x + y + z)
# print (add (6,2,2))

#dict
# vehicles = ['mercedes','Toyota','Honda','Nissan','Audi']
# model = ['2023','2016','2022','2014','2019']
# type = ['salon', 'wagon','wagon','salon','salon'] 

# vehicles = {'vehicles': 'mercedes', 'model': '2023', 'type': 'salon'}  
# print(vehicles) 
    
#EXERCISE
# Jamal = 2018
# Amal = 2017
# def your_age_is (a,b):
#     return (a - b)
# print (your_age_is (2023, Jamal))

# user_name = input('enter name')
# def age (a,b):
#     return a - b 
# print (age (2023,2017))
#print(f'{name} your age is, (age (2023,2017)')

# username = input ('enter username:')
# birth_year = input ('enter birth_year:')
# age = 2023 - int (birth_year)
# print(f'{username} your are {age} years old')
def guess_age (username,birth_year):
    age = (2023 - birth_year)
    return f'{username} you are {age} years old'
print(guess_age ('ahmad', 2010)) 




