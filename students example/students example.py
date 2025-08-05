def input_students():
    students = []

    while True:
        print("Enter student details:")

        student_id = input("ID: ")
        student_name = input("Name: ")
        student_age = input("Age: ")

        student = (student_id, student_name, student_age)
        students.append(student)

        cont = input("Add another student? (y/n): ").lower()
        if cont != 'y':
            break

    return students

def main():
    student_list = input_students()
    print("\nList of students (tuples):")
    for s in student_list:
        print(s)

if __name__ == "__main__":
    main()
