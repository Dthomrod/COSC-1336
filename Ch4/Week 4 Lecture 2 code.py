





total = 0

numStudents = int(input('How many students will you be entering grades for? '))
numGrades = int(input('How many grades will you be entering for each student? '))

for student in range(1, numStudents +1): #Outer loop
    for grade in range(1, numGrades +1): #inner loop
        print('\nFor Student', student)
        value = float(input('Enter grade ' + str(grade) + ':'))
        total = total + value

    average = total/numGrades
        
    print('The average for student', student, "is", average)
        
    total = 0
                      
