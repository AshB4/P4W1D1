
first_name = "Ashley"
last_name = 'Broussard'
age = 22
tuition = 15000.00
active_status = True

print("----Enrollment Report----")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Age: {age}")
print(f"Tuition Balance: ${tuition:.2f}")
print(f"Enrollment Status: {'Active' if active_status else 'Inactive'}")
print("----End of Report----")

del tuition

