import pandas as pd
from tabulate import tabulate
import random


#sort that data!!!


class AttendanceTracker:
    def __init__(self):
        self.attendance_data = pd.DataFrame(columns=['Name', 'Days Attended', 'Total Days Missed', 'Excused Absences', 'Unexcused Absences'])

    def add_student(self, name):
        new_student = pd.DataFrame({'Name': [name], 'Days Attended': [0], 'Total Days Missed': [0],
                                    'Excused Absences': [0], 'Unexcused Absences': [0]})
        self.attendance_data = pd.concat([self.attendance_data, new_student], ignore_index=True)

    def mark_attendance(self, index, is_present, is_excused=False):
        if 0 <= index < len(self.attendance_data):
            if is_present:
                self.attendance_data.at[index, 'Days Attended'] += 1
            else:
                self.attendance_data.at[index, 'Total Days Missed'] += 1
                if is_excused:
                    self.attendance_data.at[index, 'Excused Absences'] += 1
                else:
                    self.attendance_data.at[index, 'Unexcused Absences'] += 1
        else:
            print(f"Invalid index {index}.")

    def display_attendance(self):
        print(tabulate(self.attendance_data, headers='keys', tablefmt='pretty', showindex=False))

    def class_statistics(self):
        total_days = self.attendance_data['Days Attended'].sum() + self.attendance_data['Total Days Missed'].sum()
        overall_percentage = (self.attendance_data['Days Attended'].sum() / total_days) * 100 if total_days > 0 else 0

        most_absent_student = self.attendance_data.loc[
            self.attendance_data['Total Days Missed'] == self.attendance_data['Total Days Missed'].max(), 'Name'].tolist()

        most_truant_student = self.attendance_data.loc[
            self.attendance_data['Unexcused Absences'] == self.attendance_data['Unexcused Absences'].max(), 'Name'].tolist()

        return overall_percentage, most_absent_student, most_truant_student

# Expanded list of random student names
names = ["Alice", "Bob", "Charlie", "David", "Ezra", "Frank", "Grace", "Harry", "Ivy", "Jack", "Katherine", "Leo", "Mia", "Noah", "Olivia", "Peter", "Quinn", "Riley", "Sophia", "Thomas", "Uma (not Thurman)", "Vincent", "Willow", "Xander", "Yara", "Z. Scott Loving"]

# Create an AttendanceTracker instance
attendance_tracker = AttendanceTracker()

# Get the number of students from the user
num_students = int(input("Enter the number of students: "))

# Ask if the user wants to generate names automatically
generate_names = input("Do you want to generate names automatically? (yes/no): ").lower()

# If generating names automatically, use random names
if generate_names == 'yes':
    for i in range(num_students):
        student_name = random.choice(names)
        attendance_tracker.add_student(student_name)
else:
    for i in range(num_students):
        student_name = input(f"Student {i + 1}'s name: ")
        attendance_tracker.add_student(student_name)

# Get user input for generating random data or manual input
generate_random_data = input("Do you want to generate random data? (yes/no): ").lower()

if generate_random_data == 'yes':
    while True:
        try:
            num_days = int(input("Enter the number of days to simulate: "))
            break  # Break out of the loop if the input is a valid integer
        except ValueError:
            print("Please enter a valid number.")

    # Loop through the range of random days
    for day in range(1, num_days + 1):
        print(f"\nDay {day}:")

        # Mark random attendance for each student
        for i in range(num_students):
            is_present = random.choices([True, False], weights=[0.95, 0.05])[0]  # 95% chance of being present

            # Ask for excused absence only if the student is absent
            is_excused = False
            if not is_present:
                is_excused = random.choices([True, False], weights=[0.75, 0.25])[0]  # 75% chance of being excused

            # Mark attendance
            attendance_tracker.mark_attendance(i, is_present, is_excused)

else:
    while True:
        try:
            num_days = int(input("Enter the number of days: "))
            break  # Break out of the loop if the input is a valid integer
        except ValueError:
            print("Please enter a valid number.")

    # Loop through the range of days
    for day in range(1, num_days + 1):
        print(f"\nDay {day}:")

        # User input to mark attendance
        for i in range(num_students):
            is_present = input(f"Is {attendance_tracker.attendance_data.at[i, 'Name']} present? (y/n): ").lower() == 'y'

            # Ask for excused absence only if the student is absent
            is_excused = False
            if not is_present:
                is_excused = input(f"Is {attendance_tracker.attendance_data.at[i, 'Name']}'s absence excused? (y/n): ").lower() == 'y'

            # Mark attendance based on user input
            attendance_tracker.mark_attendance(i, is_present, is_excused)

# Display final attendance
print("\nFinal Attendance:")
attendance_tracker.display_attendance()

# Display class statistics
percentage, most_absent_student, most_truant_student = attendance_tracker.class_statistics()
print(f"\nOverall Percentage of Classes Attended: {percentage:.2f}%")

if most_absent_student:
    print(f"Most Absent Student(s): {', '.join(most_absent_student)}")
else:
    print("All students attended every class.")

if most_truant_student:
    print(f"Most Truant Student(s): {', '.join(most_truant_student)}")
else:
    print("No students were truant.")
