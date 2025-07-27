def display_student_list(student_list):
    """Display the list of student dictionaries"""
    if student_list:
        for student in student_list:
            print(student)

def get_student_details(num_students):
    """Get student details and return a list of dictionaries"""
    students = []
    
    for i in range(num_students):
        name = input("Name: ")
        try:
            age = int(input("Age: "))
            
            # Validate age
            if age <= 10 or age >= 80:
                print("Invalid Input")
                display_student_list(students)
                return students
            
            # Add student to list
            student_dict = {'Name': name, 'Age': age}
            students.append(student_dict)
            
        except ValueError:
            print("Invalid Input")
            display_student_list(students)
            return students
    
    return students

def main():
    all_students = []
    
    while True:
        try:
            num_students = int(input("Enter the no of student details to be created: "))
            
            # Check if number is zero or negative
            if num_students <= 0:
                print("Invalid Input")
                display_student_list(all_students)
                continue
            
            # Get student details
            new_students = get_student_details(num_students)
            all_students.extend(new_students)
            
            # Ask if user wants to add more students
            choice = input("Do you want to add more students' details to the dictionary? If yes, press 1, else press 0: ")
            
            if choice == '0':
                # Display original list
                print("\nHere's the list of student details :")
                display_student_list(all_students)
                
                # Sort by name and display
                sorted_students = sorted(all_students, key=lambda x: x['Name'])
                print("\nHere's the list of student details sorted by name")
                display_student_list(sorted_students)
                break
                
            elif choice == '1':
                continue
                
            else:
                print("Invalid Input")
                # Display original list
                print("Here's the list of student details :")
                display_student_list(all_students)
                
                # Sort by name and display
                sorted_students = sorted(all_students, key=lambda x: x['Name'])
                print("\nHere's the list of student details sorted by name")
                display_student_list(sorted_students)
                break
                
        except ValueError:
            print("Invalid Input")
            display_student_list(all_students)

if __name__ == "__main__":
    main()