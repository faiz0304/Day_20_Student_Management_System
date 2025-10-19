# 01_basic_average.py
# Goal: Calculate average marks of students using a dictionary.

student_marks = {"Faiz": 99, "Ali": 86, "Hassan": 75}

# Extracting keys and values
names = student_marks.keys()
marks = student_marks.values()

# Calculating average
average_marks = sum(marks) / len(marks)

# Displaying all students with marks
for name, mark in student_marks.items():
    print(f"{name} : {mark}")

# Display average marks
print("Average Marks:", average_marks)
