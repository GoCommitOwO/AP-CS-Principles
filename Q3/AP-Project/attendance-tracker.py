import pandas as pd


class AttendanceTracker:
    def __init__(self):
        self.attendance_data = pd.DataFrame(columns=['Name', 'Days_Attended', 'Days_Missed', 'Days_Excused'])

    def add_student(self, name):
        new_student = pd.DataFrame({'Name': [name], 'Days_Attended': [0], 'Days_Missed': [0], 'Days_Excused': [0]})
        self.attendance_data = pd.concat([self.attendance_data, new_student], ignore_index=True)

    def mark_attendance(self, index, is_present, is_excused=False):
        if 0 <= index < len(self.attendance_data):
            if is_present:
                self.attendance_data.at[index, 'Days_Attended'] += 1
            else:
                self.attendance_data.at[index, 'Days_Missed'] += 1
                if is_excused:
                    self.attendance_data.at[index, 'Days_Excused'] += 1
        else:
            print(f"Invalid index {index}.")

    def display_attendance(self):
        print(self.attendance_data)


# Create an AttendanceTracker instance
attendance_tracker = AttendanceTracker()

# Get the number of students from the user
num_students = int(input("Enter the number of students: "))

# Add students to the tracker
for i in range(num_students):
    student_name = input(f"Student {i + 1}'s name: ")
    attendance_tracker.add_student(student_name)

# Get the number of days
num_days = int(input("Enter the number of days: "))

# Loop through the range of days
for day in range(1, num_days + 1):
    print(f"\nDay {day}:")

    # User input to mark attendance
    for i in range(num_students):
        is_present = input(f"Is {attendance_tracker.attendance_data.at[i, 'Name']} present? (y/n): ").lower() == 'y'

        # Ask for excused absence only if the student is absent
        is_excused = False
        if not is_present:
            is_excused = input(
                f"Is {attendance_tracker.attendance_data.at[i, 'Name']}'s absence excused? (y/n): ").lower() == 'y'

        # Mark attendance based on user input
        attendance_tracker.mark_attendance(i, is_present, is_excused)

# Display final attendance
print("\nFinal Attendance:")
attendance_tracker.display_attendance()
