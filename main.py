all_students_data = {}


def calculate_student_result():
    global all_students_data
    student_record = {}
    name_of_student = input("Enter student's name: ")

    subjects = ["Math", "Python", "Java", "English", "C++"]

    marks_obtained = 0
    subjects_dict = {}

    i = 0
    while i < len(subjects):
        
        current_subject = subjects[i]
        each_subject_marks = int(input(f"Enter the marks obtained in {current_subject} out of 100: "))
        subjects_dict[current_subject] = each_subject_marks
        marks_obtained += each_subject_marks
        i += 1

    student_record["Marks"] = subjects_dict

    percentage = (marks_obtained * 100) // len(subjects) * 100

    # print(student_record)
    def check_grades(p):
        if p >= 80:
            return "A"
        elif p >= 60:
            return "B"
        elif p >= 40:
            return "C"
        elif p > 0 and p < 40:
            return "Fail"
        else:
            return "invalid input"

    grade = check_grades(percentage)
    student_record["Grade"] = grade


    all_students_data[name_of_student] = student_record


    return all_students_data
calculate_student_result()



should_stop = False

while not should_stop:
    is_there_any_other_student = input("is there any other student: ").lower()
    if is_there_any_other_student == "yes":
        calculate_student_result()
    else:
        print("End of the record")
        print(all_students_data)
        should_stop = True


import pandas as pd

df = pd.DataFrame(all_students_data)

df.to_csv("students.csv", index=False)

