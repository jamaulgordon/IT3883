# Program Name: Assignment2.py
# Course: IT3883/W02
# Student Name: Jamaul Gordon
# Assignment Number: Lab2
# Due Date: 02/07/25
# Purpose: Calculate the final averages for a group of students and print the results in descending order by grade

# Open the input file
file_name = "Assignment2input.txt"

try:
    with open(file_name, "r") as file:
        students = []
        
        # Read each line and process student data
        for line in file:
            data = line.split()
            name = data[0]
            scores = [int(num) for num in data[1:]]
            average = sum(scores) / len(scores)
            students.append((name, round(average, 2)))

    # Sort by average score in descending order
    students.sort(key=lambda x: x[1], reverse=True)

    # Print results
    for student in students:
        print(student[0], student[1])

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
