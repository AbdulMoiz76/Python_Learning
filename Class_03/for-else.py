successful = False

for number in range(3):
    print("Attempt")
    if (successful):
        print("Successful")
        break
else:
     print("Unsuccessful")


table = int(input("Enter your number:  "))

for table_num in range (1,11):
    print(f"{table} * {table_num} = {table * table_num}")

student_name = input("Enter your name: ")
name = ["Ali", "Ahmed", "Mubeen", "Sulman", "Hassan", "Abdul rehman", "Ali Raza"]

for present in range(1,10):
    if student_name == name[present-1]:
        print("Marked attendance")
        break
else:
    print("Attendance not marked Please try again")