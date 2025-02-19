def calculate_grade(marks):
    average = sum(marks) / len(marks)
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    elif average >= 50:
        return "E"
    else:
        return "Fail"

def save_result(student_name, marks, grade):
    filename = "student_grades.txt"
    try:
        with open(filename, "r") as file:
            content = file.read()
    except FileNotFoundError:
        content = ""

    with open(filename, "w") as file:
        if not content:  
         file.write(f"{student_name:<15} {str(marks):<20} {grade}\n")

def main():
    student_name = input("Enter student name: ")
    try:
        marks = list(map(int, input("Enter marks separated by space: ").split()))
        
        if not marks:
            print("Error: No marks entered!")
            return

        grade = calculate_grade(marks)
        
        print("\nStudent Grade Report")
        print("====================")
        print(f"Student Name: {student_name}")
        print(f"Marks: {marks}")
        print(f"Grade: {grade}")

        save_result(student_name, marks, grade)
        print("Result saved successfully!")

    except ValueError:
        print("Error: Please enter valid integer marks.")

if __name__ == "__main__":
    main()

