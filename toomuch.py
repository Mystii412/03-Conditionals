# ================================================
# Refactor Me: Big Messy Procedural Script (No defs)
# Constraints: NO lists, NO dicts, NO file I/O
# ================================================

import random
import math
import time

# ----------------------------
# Greeting / banner (side-effect printing)
# ----------------------------
print("================================")
print("   WELCOME TO THE MEGA APP")
print("================================")
print("This program does many small tasks in a messy way.")
print("Refactor it into clean functions later.")
print()

# ----------------------------
# Configuration-ish scalars
# ----------------------------
TAX_RATE_LOCAL = 0.0175
TAX_RATE_STATE = 0.031
QUIZ_WEIGHT = 0.25
PROJECT_WEIGHT = 0.25
EXAM_WEIGHT = 0.50

# ----------------------------
# Hard-coded "records" using only scalars (no lists/dicts)
# Each student has separate variables (begs for parameterized functions)
# ----------------------------
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

# ----------------------------
# Menu loop
# ----------------------------
running = True
last_random = 0  # small shared state scalar
tries_remaining = 3  # for guessing game
secret_number = random.randint(1, 10)

while running:
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

    if choice == "1":
        # ----- Student 1 final grade (duplicated pattern) -----
        s1_qavg = (stu1_quiz1 + stu1_quiz2) / 2
        s1_final = (s1_qavg * QUIZ_WEIGHT) + (stu1_project * PROJECT_WEIGHT) + (stu1_exam * EXAM_WEIGHT)
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
        print(f"{stu1_id} {stu1_name} -> {round(s1_final,2)} ({s1_letter})")

        # ----- Student 2 final grade (duplicated again) -----
        s2_qavg = (stu2_quiz1 + stu2_quiz2) / 2
        s2_final = (s2_qavg * QUIZ_WEIGHT) + (stu2_project * PROJECT_WEIGHT) + (stu2_exam * EXAM_WEIGHT)
        if s2_final < 60:
            s2_letter = "F"
        elif s2_final < 70:
            s2_letter = "D"
        elif s2_final < 80:
            s2_letter = "C"
        elif s2_final < 90:
            s2_letter = "B"
        else:
            s2_letter = "A"
        print(f"{stu2_id} {stu2_name} -> {round(s2_final,2)} ({s2_letter})")

        # ----- Student 3 final grade (duplicated again) -----
        s3_qavg = (stu3_quiz1 + stu3_quiz2) / 2
        s3_final = (s3_qavg * QUIZ_WEIGHT) + (stu3_project * PROJECT_WEIGHT) + (stu3_exam * EXAM_WEIGHT)
        if s3_final < 60:
            s3_letter = "F"
        elif s3_final < 70:
            s3_letter = "D"
        elif s3_final < 80:
            s3_letter = "C"
        elif s3_final < 90:
            s3_letter = "B"
        else:
            s3_letter = "A"
        print(f"{stu3_id} {stu3_name} -> {round(s3_final,2)} ({s3_letter})")

    elif choice == "2":
        # Recompute finals (again, intentionally repetitive; should become return-value helpers)
        s1_qavg = (stu1_quiz1 + stu1_quiz2) / 2
        s2_qavg = (stu2_quiz1 + stu2_quiz2) / 2
        s3_qavg = (stu3_quiz1 + stu3_quiz2) / 2

        s1_final = (s1_qavg * QUIZ_WEIGHT) + (stu1_project * PROJECT_WEIGHT) + (stu1_exam * EXAM_WEIGHT)
        s2_final = (s2_qavg * QUIZ_WEIGHT) + (stu2_project * PROJECT_WEIGHT) + (stu2_exam * EXAM_WEIGHT)
        s3_final = (s3_qavg * QUIZ_WEIGHT) + (stu3_project * PROJECT_WEIGHT) + (stu3_exam * EXAM_WEIGHT)

        # Letter grade counters (no lists/dicts; only scalars)
        count_A = 0
        count_B = 0
        count_C = 0
        count_D = 0
        count_F = 0

        # classify s1
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

        # classify s2
        if s2_final >= 90:
            count_A = count_A + 1
        elif s2_final >= 80:
            count_B = count_B + 1
        elif s2_final >= 70:
            count_C = count_C + 1
        elif s2_final >= 60:
            count_D = count_D + 1
        else:
            count_F = count_F + 1

        # classify s3
        if s3_final >= 90:
            count_A = count_A + 1
        elif s3_final >= 80:
            count_B = count_B + 1
        elif s3_final >= 70:
            count_C = count_C + 1
        elif s3_final >= 60:
            count_D = count_D + 1
        else:
            count_F = count_F + 1

        total_students = 3
        avg_final = (s1_final + s2_final + s3_final) / total_students
        print("--- Stats ---")
        print("A:", count_A, "B:", count_B, "C:", count_C, "D:", count_D, "F:", count_F)
        print("Average final:", round(avg_final, 2))

    elif choice == "3":
        # Taxes on two salaries (could become param functions and a void printer)
        try:
            salary1 = float(input("Enter salary 1: "))
            salary2 = float(input("Enter salary 2: "))
        except:
            print("Invalid input.")
            salary1 = 0.0
            salary2 = 0.0

        combined = salary1 + salary2
        local_tax = combined * TAX_RATE_LOCAL
        state_tax = combined * TAX_RATE_STATE
        net = combined - local_tax - state_tax

        # Repeat the same summary twice (wasteful)
        print("\n-- Tax Summary (1) --")
        print("Gross:", round(combined, 2))
        print("Local tax:", round(local_tax, 2))
        print("State tax:", round(state_tax, 2))
        print("Net:", round(net, 2))

        # Pretend second copy needed
        gross_copy = combined
        local_copy = gross_copy * TAX_RATE_LOCAL
        state_copy = gross_copy * TAX_RATE_STATE
        net_copy = gross_copy - local_copy - state_copy
        print("\n-- Tax Summary (2) --")
        print("Gross:", round(gross_copy, 2))
        print("Local tax:", round(local_copy, 2))
        print("State tax:", round(state_copy, 2))
        print("Net:", round(net_copy, 2))

    elif choice == "4":
        # Temperature conversions (could split into pure functions and a menu function without params)
        mode = input("Type 'C2F' or 'F2C': ").strip().upper()
        if mode == "C2F":
            try:
                c = float(input("Enter Celsius: "))
            except:
                c = 0.0
            f = (c * 9/5) + 32
            print(c, "C =", round(f, 2), "F")
        elif mode == "F2C":
            try:
                f = float(input("Enter Fahrenheit: "))
            except:
                f = 0.0
            c = (f - 32) * 5/9
            print(f, "F =", round(c, 2), "C")
        else:
            print("Unknown mode.")

    elif choice == "5":
        # BMI for two people (returns vs void in refactor)
        name_a = input("Name A: ").strip()
        try:
            kg_a = float(input("Weight A (kg): "))
            m_a = float(input("Height A (m): "))
        except:
            kg_a = 0.0
            m_a = 1.0
        bmi_a = kg_a / (m_a * m_a)
        if bmi_a < 18.5:
            cat_a = "Underweight"
        elif bmi_a < 25:
            cat_a = "Normal"
        elif bmi_a < 30:
            cat_a = "Overweight"
        else:
            cat_a = "Obesity"
        print(name_a, "BMI:", round(bmi_a, 2), "-", cat_a)

        name_b = input("Name B: ").strip()
        try:
            kg_b = float(input("Weight B (kg): "))
            m_b = float(input("Height B (m): "))
        except:
            kg_b = 0.0
            m_b = 1.0
        bmi_b = kg_b / (m_b * m_b)
        if bmi_b < 18.5:
            cat_b = "Underweight"
        elif bmi_b < 25:
            cat_b = "Normal"
        elif bmi_b < 30:
            cat_b = "Overweight"
        else:
            cat_b = "Obesity"
        print(name_b, "BMI:", round(bmi_b, 2), "-", cat_b)

    elif choice == "6":
        # Word formatting lab (lots of side-effect prints; could be parameterized)
        raw1 = input("Enter a phrase: ")
        raw2 = input("Enter another phrase: ")
        t1 = raw1.strip()
        t2 = raw2.strip()
        print("Title 1:", t1.title())
        print("Upper 1:", t1.upper())
        print("Lower 1:", t1.lower())
        print("Swap  1:", t1.swapcase())
        print("Title 2:", t2.title())
        print("Upper 2:", t2.upper())
        print("Lower 2:", t2.lower())
        print("Swap  2:", t2.swapcase())

        # duplicate substring search logic without lists
        sub = input("Substring to find: ").strip()
        pos1 = t1.find(sub)
        pos2 = t2.find(sub)
        if pos1 >= 0:
            print("Found in phrase 1 at index", pos1)
        else:
            print("Not found in phrase 1")
        if pos2 >= 0:
            print("Found in phrase 2 at index", pos2)
        else:
            print("Not found in phrase 2")

    elif choice == "7":
        # Coin change (no lists; just math and scalar counters)
        try:
            cents = int(input("Enter cents (0-999): ").strip())
        except:
            cents = 0
        if cents < 0:
            cents = 0
        if cents > 999:
            cents = 999

        q = cents // 25
        r = cents % 25
        d = r // 10
        r = r % 10
        n = r // 5
        p = r % 5

        # print twice (intentionally repetitive)
        print("Quarters:", q, "Dimes:", d, "Nickels:", n, "Pennies:", p)
        print("Coins -> Q:", q, "| D:", d, "| N:", n, "| P:", p)

    elif choice == "8":
        # Random guessing game (could be multiple small functions with/without params)
        print("Guess the number (1-10)!")
        print("You have", tries_remaining, "tries left.")
        try:
            guess = int(input("Your guess: ").strip())
        except:
            guess = -1

        if guess == secret_number:
            print("Correct! You win!")
            # reset game
            secret_number = random.randint(1, 10)
            tries_remaining = 3
        else:
            tries_remaining = tries_remaining - 1
            if guess > secret_number:
                print("Too high.")
            elif guess < secret_number and guess != -1:
                print("Too low.")
            else:
                print("Invalid guess.")
            if tries_remaining <= 0:
                print("Out of tries. The number was", secret_number)
                secret_number = random.randint(1, 10)
                tries_remaining = 3
        last_random = secret_number  # arbitrary shared scalar update

    elif choice == "9":
        # Geometry pack (duplicate computations; candidates for value-returning funcs)
        mode = input("square/rect/circle/tri: ").strip().lower()
        if mode == "square":
            try:
                side = float(input("Side length: "))
            except:
                side = 0.0
            area = side * side
            perim = 4 * side
            print("Square area:", round(area, 3))
            print("Square perimeter:", round(perim, 3))
            # duplicate "reporting"
            print("Square Summary -> A:", round(area, 3), "P:", round(perim, 3))

        elif mode == "rect":
            try:
                w = float(input("Width: "))
                h = float(input("Height: "))
            except:
                w = 0.0
                h = 0.0
            area = w * h
            perim = 2 * w + 2 * h
            print("Rectangle area:", round(area, 3))
            print("Rectangle perimeter:", round(perim, 3))
            print("Rectangle Summary -> A:", round(area, 3), "P:", round(perim, 3))

        elif mode == "circle":
            try:
                r = float(input("Radius: "))
            except:
                r = 0.0
            area = math.pi * r * r
            circ = 2 * math.pi * r
            print("Circle area:", round(area, 3))
            print("Circle circumference:", round(circ, 3))
            print("Circle Summary -> A:", round(area, 3), "C:", round(circ, 3))

        elif mode == "tri":
            try:
                base = float(input("Base: "))
                height = float(input("Height: "))
                a = float(input("Side a: "))
                b = float(input("Side b: "))
                c = float(input("Side c: "))
            except:
                base = 0.0
                height = 0.0
                a = 0.0
                b = 0.0
                c = 0.0
            area = 0.5 * base * height
            perim = a + b + c
            print("Triangle area:", round(area, 3))
            print("Triangle perimeter:", round(perim, 3))
            print("Triangle Summary -> A:", round(area, 3), "P:", round(perim, 3))
        else:
            print("Unknown shape.")

    elif choice == "10":
        print("Saving (not really, just pretending).")
        print("Goodbye.")
        running = False

    else:
        print("Invalid choice. Try again.")

# End of program (no functions were harmed—or written—in the making of this file)
