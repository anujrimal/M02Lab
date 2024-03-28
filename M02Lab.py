# Author: Anuj Rimal
# File Name: student.py
# Description: This Python app accepts student names and GPAs and tests if the student qualifies for either the Dean's List or the Honor Roll.

def main():
    print("Welcome to the Qualification App!")
    print("Enter 'ZZZ' for last name to quit.")

    while True:
        last_name = input("Enter student's last name: ")
        if last_name == 'ZZZ':
            break

        first_name = input("Enter student's first name: ")
        gpa = float(input("Enter student's GPA: "))

        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(f"Sorry, {first_name} {last_name} does not qualify for any recognition.")

if __name__ == "__main__":
    main()
