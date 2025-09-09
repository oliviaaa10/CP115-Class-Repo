# Students Classification System
# Get student information
student_name = input("Enter student name: ")
gpa = float(input("Enter GPA (0.0-4.0): "))
credit_hours = int(input("Enter credit hours: "))

if ( gpa >= 3.8 ) and ( credit_hours >= 12 ):
    classification = "Dean's List"
elif ( gpa >= 3.5 ) and ( credit_hours >= 12):
    classification = "Honor Roll"
elif gpa >= 2.0:
    classification = "Good Standing"
elif gpa < 2.0:
    classification = "Academic Probation"
else:
    classification = "Part-time students"

# Display results
print(f"\nStudent: {student_name}")
print(f"GPA: {gpa}")
print(f"Credit Hours: {credit_hours}")
print(f"Classification: {classification}")
