# Function to calculate average
def average(m1, m2, m3):
    return (m1 + m2 + m3) / 3

# Function to get grade
def grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    else:
        return "C"

# Loop to allow multiple students
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
    if choice != "yes":
        break