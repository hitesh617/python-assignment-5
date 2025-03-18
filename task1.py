#  Create a Dictionary of Student Marks


student_data = {
    "Alice": 95, 
    "Bob": 85, 
    "John": 98,
    "ronin": 76
}

name = input("Enter the student's name: ")
if name in student_data:
    print(f"{name}'s marks: {student_data[name]}")
else:
    print("Student not found.")    