# Given a list of grades (e.g., [67, 90, 78, 85, 92, 70, 83]), write a program that prints
# the highest grade, the lowest grade, and the average grade. Also, classify each grade
# as 'Fail' (below 60), 'Pass' (60-79), or 'Excellent' (80 and above).

gradeslist = [67, 90, 78, 85, 92, 70, 83] 

average_grade = sum(gradeslist) / len(gradeslist)
highest_grade = max(gradeslist) 
lowest_grade = min(gradeslist)

print(highest_grade)
print(lowest_grade)
print(average_grade)
for grade in gradeslist:

    if grade <= 61: 
        print("Fail")
    elif grade >= 61 and grade <= 80:
        print("Pass")
    else:
        print("Excellent")