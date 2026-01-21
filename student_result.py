# Student Result Management System

students = []

def add_student(name, score):
    student = {
        "name": name,
        "score": score
    }
    students.append(student)

def display_students():
    print("Student Results")
    for student in students:
        if student["score"] >= 50:
            status = "Pass"
        else:
            status = "Fail"
        print(student["name"], "-", student["score"], "-", status)

def calculate_average():
    total = 0
    for student in students:
        total += student["score"]
    average = total / len(students)
    return average

# Program Execution
add_student("John", 70)
add_student("Mary", 45)
add_student("David", 85)

display_students()
print("Average Score:", calculate_average())
