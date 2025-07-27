# Student Management System

A Python program that helps a training school manage student details by storing them in a list of dictionaries and displaying them in sorted order by name.

## Features

- Add student details (name and age) to a list of dictionaries
- Validate student age (must be between 11 and 79)
- Sort and display students by name
- Handle various input validation scenarios
- Support for adding multiple batches of students

## Usage

Run the main program:
```bash
python3 student_management.py
```

The program will prompt you to:
1. Enter the number of student details to create
2. Enter each student's name and age
3. Choose whether to add more students (1 = yes, 0 = no)

## Input Validation

The program handles the following validation cases:

1. **Invalid student count**: If you enter 0 or negative number, it displays "Invalid Input" and shows existing student data
2. **Invalid age**: If age is ≤10 or ≥80, it displays "Invalid Input" and shows current student data
3. **Invalid choice**: If you enter anything other than '0' or '1' when asked to continue, it displays "Invalid Input" followed by the student list before and after sorting
4. **Invalid age format**: If you enter non-numeric age, it displays "Invalid Input"

## Example Output

```
Enter the no of student details to be created: 2
Name: Angelina
Age: 22
Name: Brad
Age: 25

Do you want to add more students' details to the dictionary? If yes, press 1, else press 0: 1
Enter the no of student details to be created: 2
Name: Ann
Age: 20
Name: Joel
Age: 22

Do you want to add more students' details to the dictionary? If yes, press 1, else press 0: 0

Here's the list of student details :
{'Name': 'Angelina', 'Age': 22}
{'Name': 'Brad', 'Age': 25}
{'Name': 'Ann', 'Age': 20}
{'Name': 'Joel', 'Age': 22}

Here's the list of student details sorted by name
{'Name': 'Angelina', 'Age': 22}
{'Name': 'Ann', 'Age': 20}
{'Name': 'Brad', 'Age': 25}
{'Name': 'Joel', 'Age': 22}
```

## Testing

Run the test script to see various scenarios:
```bash
python3 test_student_management.py
```

## Files

- `student_management.py` - Main program with interactive input
- `test_student_management.py` - Test script demonstrating functionality
- `README.md` - This documentation file