student = {
    'Alice': 'F',
    'Bob': 'D', 
    'Charlie': 'C',
    'Diana': 'B',
    'Eve': 'A'
}

print("Enter Student name: ")
student_name = input()
print("Enter Student grade: ")
student_grade = input()
student[student_name] = student_grade

student['Charlie'] = 'A'

print("All Student Grades: ")
print(student)