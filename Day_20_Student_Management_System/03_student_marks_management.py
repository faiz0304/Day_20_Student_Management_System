# 03_student_marks_management.py
# Goal: Manage student marks with file handling (view, add, update, delete, average).


def show_student_details(FILENAME):
    """Reads and returns student data from file."""
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"File '{FILENAME}' not found.")
        return ""


def write_student_details(FILENAME, s_names, s_marks):
    """Writes all student names and marks back to file."""
    try:
        with open(FILENAME, "w", encoding="utf-8") as f:
            for name, mark in zip(s_names, s_marks):
                f.write(f"Name : {name} | Marks : {mark}\n")
        print("Student file updated successfully.")
    except Exception as e:
        print("Error while writing file:", e)


def student_name_marks(student_info):
    """Extracts names and marks from text data."""
    students = student_info.split("\n")
    names, marks = [], []
    for line in students:
        parts = line.split(" ")
        if len(parts) >= 7:
            name = parts[2]
            try:
                mark = int(parts[6])
            except ValueError:
                print(f"Skipping invalid mark in line: {line}")
                continue
            names.append(name)
            marks.append(mark)
    return names, marks


def average_student_marks(s_marks):
    """Calculates average marks."""
    return round(sum(s_marks) / len(s_marks), 2) if s_marks else 0


def add_students_marks(FILENAME):
    """Appends new student data to file."""
    try:
        with open(FILENAME, "a", encoding="utf-8") as f:
            name = input("Enter Student Name: ").capitalize()
            try:
                mark = int(input("Enter Student Marks: "))
            except ValueError:
                print("Invalid marks. Please enter a number.")
                return
            f.write(f"Name : {name} | Marks : {mark}\n")
        print(f"Student '{name}' added successfully.")
    except Exception as e:
        print("Error while adding student:", e)


def update_students_marks(FILENAME):
    """Updates marks of an existing student."""
    student_info = show_student_details(FILENAME)
    s_names, s_marks = student_name_marks(student_info)
    if not s_names:
        print("No data found to update.")
        return

    name = input("Enter Student Name to Update: ").capitalize()
    if name in s_names:
        try:
            mark = int(input(f"Enter New Marks for {name}: "))
        except ValueError:
            print("Invalid marks.")
            return
        s_index = s_names.index(name)
        old_mark = s_marks[s_index]
        s_marks[s_index] = mark
        print(f"Updated: {name}'s marks from {old_mark} → {mark}")
        write_student_details(FILENAME, s_names, s_marks)
    else:
        print(f"Student '{name}' not found.")


def delete_students_marks(FILENAME):
    """Deletes a student record."""
    student_info = show_student_details(FILENAME)
    s_names, s_marks = student_name_marks(student_info)
    if not s_names:
        print("No data found to delete.")
        return

    name = input("Enter Student Name to Delete: ").capitalize()
    if name in s_names:
        idx = s_names.index(name)
        deleted_name = s_names.pop(idx)
        deleted_mark = s_marks.pop(idx)
        write_student_details(FILENAME, s_names, s_marks)
        print(f"🗑️ Deleted: {deleted_name} ({deleted_mark} marks)")
    else:
        print(f"Student '{name}' not found.")


def main():
    """Main program menu."""
    FILENAME = "students_marks.txt"
    print("=== 🎓 Welcome to Student Marks Management System ===")

    while True:
        print(
            """
------ Menu ------
1. Show All Students
2. Average Marks
3. Add Student
4. Update Student
5. Delete Student
6. Exit
"""
        )
        choice = input("Enter Choice (1–6): ")

        if choice == "1":
            student_info = show_student_details(FILENAME)
            print(student_info or "No data available.")
        elif choice == "2":
            student_info = show_student_details(FILENAME)
            _, s_marks = student_name_marks(student_info)
            print("Average Marks:", average_student_marks(s_marks))
        elif choice == "3":
            add_students_marks(FILENAME)
        elif choice == "4":
            update_students_marks(FILENAME)
        elif choice == "5":
            delete_students_marks(FILENAME)
        elif choice == "6":
            print("Exiting... Data saved successfully.")
            break
        else:
            print("Invalid input! Try again.")


if __name__ == "__main__":
    main()
