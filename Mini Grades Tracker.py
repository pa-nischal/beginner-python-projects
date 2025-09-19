#   Mini grade tracker
#       Input: student names, subjects, grades (read from CSV).
#       Process: store data in a dictionary, calculate averages, highest/lowest scores, letter grades.
#       Output: display report card.

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

with open("mini_grade_tracker.csv","r") as file:
    lines = file.readlines()

lines = lines[1:]

maths_marks = []
english_marks = []
science_marks = []
computer_marks = []

grades = {}
for line in lines:
    values = line.strip().split(",")
    maths_marks.append(int(values[1]))
    english_marks.append(int(values[2]))
    science_marks.append(int(values[3]))
    computer_marks.append(int(values[4]))
    grades[values[0]] = {
        "Maths": int(values[1]),
        "English": int(values[2]),
        "Science": int(values[3]),
        "Computer": int(values[4])
    }

print(f"The average marks in Maths is {sum(maths_marks)/len(maths_marks):.1f}")
print(f"The average marks in English is {sum(english_marks)/len(english_marks):.1f}")
print(f"The average marks in Science is {sum(science_marks)/len(science_marks):.1f}")
print(f"The average marks in Computer is {sum(computer_marks)/len(computer_marks):.1f}")


print("1. Check report card.")
print("2. Display Highest / Lowest marks.")
print("3. Exit")

num = 0
while num != 3:
    num = int(input("\n -->"))
    if num == 1:
        name = input("Enter your name:").strip().title()
        if name in grades:
            print(f"Name: {name}")
            print("")
            print( "Subject   Marks   Grade")
            print(f"Maths      {grades[name]['Maths']}      {get_letter_grade(grades[name]['Maths'])}")
            print(f"English    {grades[name]['English']}      {get_letter_grade(grades[name]['English'])}")
            print(f"Science    {grades[name]['Science']}      {get_letter_grade(grades[name]['Science'])}")
            print(f"Computer   {grades[name]['Computer']}      {get_letter_grade(grades[name]['Computer'])}")
            print("")
            print(f"Percentage - {(grades[name]["Maths"]+grades[name]["English"]+grades[name]["Science"]+grades[name]["Computer"])/4:.2f}")
        else:
            print("You are not in the database!")

    if num == 2:
        print("Highest scores:")
        print(f"Maths - {max(maths_marks)}")
        print(f"English - {max(english_marks)}")
        print(f"Science - {max(science_marks)}")
        print(f"Computer - {max(computer_marks)}")
        print("Lowest scores:")
        print(f"Maths - {min(maths_marks)}")
        print(f"English - {min(english_marks)}")
        print(f"Science - {min(science_marks)}")
        print(f"Computer - {min(computer_marks)}")
