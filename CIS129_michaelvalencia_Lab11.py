# 9.1 question

def main():
    # Open the file 
    with open('grades.txt', 'a') as file:
        while True:
            try:
                grade = input("Enter a grade (or 'q' to quit): ")
                if grade.lower() == 'q':
                    break
                else:
                    #  grade 
                    file.write(grade + '\n')
            except Exception as e:
                print("Error:", e)

if __name__ == "__main__":
    main()
'
# 9.2 question

def main():
    try:
        #  read mode
        with open('grades.txt', 'r') as file:
            grades = file.readlines()
            grades = [float(grade.strip()) for grade in grades]

        #  individual grades
        print("Individual Grades:")
        for grade in grades:
            print(grade)

        # total, count, and average
        total = sum(grades)
        count = len(grades)
        average = total / count

        print("\nTotal:", total)
        print("Count:", count)
        print("Average:", average)
    except FileNotFoundError:
        print("File not found. Make sure you have created the grades.txt file first.")

if __name__ == "__main__":
    main()

# 9.3 question

import csv

def main():
    try:
        #  write mode with newline='' to prevent extra newline characters
        with open('grades.csv', 'w', newline='') as csvfile:
            # Create a CSV writer object
            writer = csv.writer(csvfile)

            #  header row
            writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

            while True:
                first_name = input("Enter student's first name (or 'q' to quit): ")
                if first_name.lower() == 'q':
                    break
                last_name = input("Enter student's last name: ")
                exam1 = int(input("Enter exam 1 grade: "))
                exam2 = int(input("Enter exam 2 grade: "))
                exam3 = int(input("Enter exam 3 grade: "))

                #  student's information CSV file
                writer.writerow([first_name, last_name, exam1, exam2, exam3])

        print("Student records have been written to grades.csv.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()


