Student Record Management System

A simple Python program that collects student details, calculates their average score, assigns a grade, and allows multiple student entries.

⸻
 Author

Mohamed C Saccoh


 License

This project is licensed under the MIT License – you are free to use, modify, and distribute this software with proper attribution.


 Description

This program:
	•	Takes student name and ID as input
	•	Accepts three subject marks
	•	Calculates the average score
	•	Assigns a grade based on the average
	•	Displays the result
	•	Repeats the process for multiple students until the user exits


 How It Works
	1.	User enters student details (name and ID)
	2.	User inputs three marks
	3.	The system calculates the average
	4.	A grade is assigned:
	•	A → 80 and above
	•	B → 60–79
	•	C → Below 60
	5.	The result is displayed
	6.	User chooses whether to continue or stop

  """
Student Record Management System

Author: Mohamed C Sankoh
License: MIT License
"""

def average(m1, m2, m3):
    return (m1 + m2 + m3) / 3

def grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    else:
        return "C"

while True:
    print("\nEnter Student Details")

    name = input("Enter name: ")
    student_id = input("Enter ID: ")

    m1 = float(input("Enter mark 1: "))
    m2 = float(input("Enter mark 2: "))
    m3 = float(input("Enter mark 3: "))

    avg = average(m1, m2, m3)
    g = grade(avg)

    print("\n--- Student Result ---")
    print("Name:", name)
    print("ID:", student_id)
    print("Average:", avg)
    print("Grade:", g)

    choice = input("\nAdd another student? (yes/no): ")
    if choice.lower() != "yes":
        break

        How to Run
	1.	Install Python (version 3 or higher)
	2.	Copy the code into a file, e.g. student_system.py
	3.	Run the program:

  python student_system.py

  Example Output

  Enter Student Details
Enter name: John
Enter ID: 101
Enter mark 1: 75
Enter mark 2: 80
Enter mark 3: 70

--- Student Result ---
Name: John
ID: 101
Average: 75.0
Grade: B



