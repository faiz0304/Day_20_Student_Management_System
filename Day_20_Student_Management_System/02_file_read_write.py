# 02_file_read_write.py
# Goal: Store student names and marks in a file, then read them.

student_marks = {"Faiz": 99, "Ali": 86, "Hassan": 75}
FILENAME = "students_marks.txt"

# Step 1: Write data to file
with open(FILENAME, "w", encoding="utf-8") as f:
    for name, mark in student_marks.items():
        f.write(f"Name : {name} | Marks : {mark}\n")

print("Data written successfully to file.\n")

# Step 2: Read data back from file
with open(FILENAME, "r", encoding="utf-8") as f:
    marks = f.read()

print("File Content:")
print(marks)
