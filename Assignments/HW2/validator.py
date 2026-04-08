
grade = int(input("Enter the student's final grade (0-100): "))
if grade >= 90:
    print("Status: Honors")
elif 60 <= grade < 90:
    print("Status: Passed")
else:
    print("Status: Failed - Please contact the advisor.")



