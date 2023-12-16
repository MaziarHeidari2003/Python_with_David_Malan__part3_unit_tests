"""
with open('students.csv') as file:
  for line in file:
    row = line.rstrip().split(',')
    print(f'{row[0]} is in {row[1]}')
"""
"""
students = []
with open('students.csv') as file:
  for line in file:
    name,house = line.rstrip().split(',')
    students.append(f'{name} is in {house}')

for student in sorted(students):
  print(student)
"""

students = []
with open('students.csv') as file:
  for line in file:
    name,home = line.rstrip().split(',')
    #student = {}
    #student['name'] = name
    #student['house'] = house
    student = {'name': name, 'home': home}
    students.append(student)


for student in sorted(students,key=lambda student: student['name']):
  #the thing is how to sort the dictionaries
  print(f'{student['name']} is from {student['home']}')    
