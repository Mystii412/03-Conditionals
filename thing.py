def print_greeting():
    print("================================")
    print("   WELCOME TO THE MEGA APP")
    print("================================")
    print("This program does many small tasks in a messy way.")
    print("Refactor it into clean functions later.")
    print()

def get_menu_choice():
    """Prints a menu and returns a number representing user choice"""
    print("\n==== MAIN MENU ====")
    print("1) Show 3 student final grades")
    print("2) Class stats (A/B/C/D/F counts) for the 3 students")
    print("3) Add two salaries and compute taxes")
    print("4) Temperature conversions (C<->F)")
    print("5) BMI check for two people")
    print("6) Word formatting lab (title/case/strip)")
    print("7) Coin change (quarters/dimes/nickels/pennies)")
    print("8) Random guessing game (1-10)")
    print("9) Simple geometry pack (areas/perimeters)")
    print("10) Exit")
    choice = input("Choose: ").strip()
    return choice


def print_single_grade(quiz1, quiz2, project, exam, id, name):
    QUIZ_WEIGHT = 0.2
    PROJECT_WEIGHT = 0.25
    EXAM_WEIGHT = 0.50
    s1_qavg = (quiz1 + quiz2) / 2
    s1_final = (s1_qavg * QUIZ_WEIGHT) + (project * PROJECT_WEIGHT) + (exam * EXAM_WEIGHT)
    if s1_final < 60:
        s1_letter = "F"
    elif s1_final < 70:
        s1_letter = "D"
    elif s1_final < 80:
        s1_letter = "C"
    elif s1_final < 90:
        s1_letter = "B"
    else:
        s1_letter = "A"
    print(f"{id} {name} -> {round(s1_final,2)} ({s1_letter})")

def calculate_final(quiz1, quiz2, project, exam):
    QUIZ_WEIGHT = 0.2
    PROJECT_WEIGHT = 0.25
    EXAM_WEIGHT = 0.5

def print_final_grades():

    stu1_id = 101
    stu1_name = "Avery"
    stu1_quiz1 = 78
    stu1_quiz2 = 82
    stu1_project = 90
    stu1_exam = 84

    stu2_id = 102
    stu2_name = "Bailey"
    stu2_quiz1 = 92
    stu2_quiz2 = 88
    stu2_project = 76
    stu2_exam = 90

    stu3_id = 103
    stu3_name = "Casey"
    stu3_quiz1 = 65
    stu3_quiz2 = 71
    stu3_project = 70
    stu3_exam = 72

    print_single_grade(stu1_quiz1, stu1_quiz2, stu1_project, stu1_exam, stu1_id, stu1_name)
    print_single_grade(stu2_quiz1, stu2_quiz2, stu2_project, stu2_exam, stu2_id, stu2_name)
    print_single_grade(stu3_quiz1, stu3_quiz2, stu3_project, stu3_exam, stu3_id, stu3_name)



def main():
    stu1_id = 101
    stu1_name = "Avery"
    stu1_quiz1 = 78
    stu1_quiz2 = 82
    stu1_project = 90
    stu1_exam = 84

    stu2_id = 102
    stu2_name = "Bailey"
    stu2_quiz1 = 92
    stu2_quiz2 = 88
    stu2_project = 76
    stu2_exam = 90

    stu3_id = 103
    stu3_name = "Casey"
    stu3_quiz1 = 65
    stu3_quiz2 = 71
    stu3_project = 70
    stu3_exam = 72
    print_greeting()
    running = True
    while running:
        user_choice = get_menu_choice()
        if user_choice =='1':
            print_single_grade(stu1_quiz1,stu1_quiz2, stu1_project, stu1_exam, stu1_id, stu1_name)
            print_single_grade(stu2_quiz1,stu2_quiz2, stu2_project, stu2_exam, stu2_id, stu2_name)
            print_single_grade(stu3_quiz1,stu3_quiz2, stu3_project, stu3_exam, stu3_id, stu3_name)
        elif user_choice =='2':
            s1_final = print_final_grades(stu1_quiz1,stu1_quiz2, stu1_project, stu1_exam)
            s2_final = print_final_grades(stu2_quiz1,stu2_quiz2, stu2_project, stu2_exam)
            s3_final = print_final_grades(stu3_quiz1,stu3_quiz2, stu3_project, stu3_exam)
            # Letter grade counters (no lists/dicts; only scalars)
            count_A = 0
            count_B = 0
            count_C = 0
            count_D = 0
            count_F = 0
            for final in(s1_final, s2_final, s3_final):
                if s1_final >= 90:
                    count_A = count_A + 1
                elif s1_final >= 80:
                    count_B = count_B + 1
                elif s1_final >= 70:
                    count_C = count_C + 1
                elif s1_final >= 60:
                    count_D = count_D + 1
                else:
                    count_F = count_F + 1
                total_students = 3
                avg_final = (s1_final + s2_final + s3_final) / total_students
                print("--- Stats ---")
                print("A:", count_A, "B:", count_B, "C:", count_C, "D:", count_D, "F:", count_F)
                print("Average final:", round(avg_final, 2))
            


if __name__ == '__main__':
    main()