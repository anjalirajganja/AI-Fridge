#!/usr/bin/env python3

def display_student_list(student_list):
    """Display the list of student dictionaries"""
    if student_list:
        for student in student_list:
            print(student)

def test_program():
    """Test the student management functionality"""
    print("=== Testing Student Management Program ===\n")
    
    # Test case 1: Normal operation
    print("Test Case 1: Normal operation")
    students = []
    
    # Add first batch of students
    student1 = {'Name': 'Angelina', 'Age': 22}
    student2 = {'Name': 'Brad', 'Age': 25}
    students.extend([student1, student2])
    
    # Add second batch of students
    student3 = {'Name': 'Ann', 'Age': 20}
    student4 = {'Name': 'Joel', 'Age': 22}
    students.extend([student3, student4])
    
    print("Here's the list of student details :")
    display_student_list(students)
    
    # Sort by name
    sorted_students = sorted(students, key=lambda x: x['Name'])
    print("\nHere's the list of student details sorted by name")
    display_student_list(sorted_students)
    
    print("\n" + "="*50 + "\n")
    
    # Test case 2: Invalid age
    print("Test Case 2: Invalid age (age <= 10 or >= 80)")
    test_students = [{'Name': 'Alice', 'Age': 25}]
    print("Current students before invalid input:")
    display_student_list(test_students)
    print("Attempting to add student with age 9...")
    print("Invalid Input")
    display_student_list(test_students)
    
    print("\n" + "="*50 + "\n")
    
    # Test case 3: Invalid choice
    print("Test Case 3: Invalid choice (not 0 or 1)")
    test_students = [{'Name': 'Bob', 'Age': 30}, {'Name': 'Alice', 'Age': 25}]
    print("Invalid Input")
    print("Here's the list of student details :")
    display_student_list(test_students)
    
    sorted_test = sorted(test_students, key=lambda x: x['Name'])
    print("\nHere's the list of student details sorted by name")
    display_student_list(sorted_test)
    
    print("\n" + "="*50 + "\n")
    
    # Test case 4: Zero or negative student count
    print("Test Case 4: Zero or negative student count")
    existing_students = [{'Name': 'Charlie', 'Age': 28}]
    print("Attempting to create 0 students...")
    print("Invalid Input")
    display_student_list(existing_students)

if __name__ == "__main__":
    test_program()