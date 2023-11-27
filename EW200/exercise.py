# Write your code here :-)
# how many students do you want to enter?
# enter names
# enter number grades
# output letter grade

num = input("How many students do you want to enter?")
names = input("What are the students names?")
listNames = names.split()
print(listNames)
numGrade = input("What number grade does the student have?")
listGrades = numGrade.split()
print(listGrades)
#numGrade = int(numGrade)
#print(names)
#print(numGrade)

i = 0
while i < int(num):
    if float(listGrades[i]) < 60:
        letGrade = 'F'
    elif float(listGrades[i]) < 70:
        letGrade = 'D'
    elif float(listGrades[i]) < 80:
        letGrade = 'C'
    elif float(listGrades[i]) < 90:
        letGrade = 'B'
    else:
        letGrade = 'A'
    print(f'{listNames[i]} earned a {letGrade}')
    i = i+1




