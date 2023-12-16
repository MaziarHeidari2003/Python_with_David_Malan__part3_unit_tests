import csv


"""
students = []
with open('students.csv') as file:
  reader = csv.DictReader(file)
  for row in reader:
    students.append({"name":row['name'],"home": row['home']} )




for student in sorted(students,key=lambda student: student['name']):
  #the thing is how to sort the dictionaries
  print(f'{student['name']} is from {student['home']}') 
"""

name = input('Whats your name? ')
home = input('Where is your home? ')

with open('students.csv','a') as file :
  writer = csv.writer(file)
  writer.writerow([name,home()]) 
