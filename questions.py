# Given a list of grades (e.g., [67, 90, 78, 85, 92, 70, 83]), write a program that prints
# the highest grade, the lowest grade, and the average grade. Also, classify each grade
# as 'Fail' (below 60), 'Pass' (60-79), or 'Excellent' (80 and above).

# gradeslist = [67, 90, 78, 85, 92, 70, 83] 

# average_grade = sum(gradeslist) / len(gradeslist)
# highest_grade = max(gradeslist) 
# lowest_grade = min(gradeslist)

# print(highest_grade)
# print(lowest_grade)
# print(average_grade)
# for grade in gradeslist:

#     if grade <= 61: 
#         print("Fail")
#     elif grade >= 61 and grade <= 80:
#         print("Pass")
#     else:
#         print("Excellent")

# x = int(input("Enter a number"))
# y = int(input("Enter a number"))

# if x < y:
#     print("x is less than y")
# elif x > y:
#     print("y is greater than x")
# else:
#     print("x = y")

# x = int(input("Enter Number"))
# y = int(input("Enter Number"))
# z = int(input("Enter Number"))

# if x > y < z:
#     print("z is the largest")
# elif x < y < z:
#     print("z is the largest")
# elif x > y > z:
#     print("x is the largest")

# x = "hello, d, g, h"
# y = "f, d, h, j, k, l, z, x, c ,v ,b ,n ,m"
# len(x)     
# len(y)
# if len(x) > len(y):
#     print("x is greater than y")
# else:
#     print("y is greater than x")

# Q. you need to take two strings and check if their first character matches or not. Print yes or no accordingly

# string1 = "sdfkaj"
# string2 = "hello"

# if string1[0] == string2[0]:
#     print("Yes")
# else:
#     print("No")

# Write a Python program to determine the classification of a movie based on its release year and critical rating. Use year_released for the year it came out and rating for its score out of 10. Assume the current year is 2024. Classify the movie as follows:
# If released within the last 5 years:
# Over 8.0 rating: "Modern hit"
# 5.0 to 8.0 rating: "Modern average"
# Below 5.0 rating: "Modern flop"
# If released 5 to 20 years ago:
# Over 8.0 rating: "Recent classic"
# 5.0 to 8.0 rating: "Recent average"
# Below 5.0 rating: "Recent miss"
# If released more than 20 years ago:
# Over 8.0 rating: "Certified classic"
# 5.0 to 8.0 rating: "Old but good"
# Below 5.0 rating: "Old flop"

# If released with Percy Jackson in the name:
# HORIBBBBBBBBLEEEEEEEEEE
# or 
# INSULT TO THE WORLD


# rating = 5

# if 2020 - 2024  and rating <= 8.1:
#     print("modern hit") 
# elif 2020 - 2024 and rating <= 8 and rating >= 5.1:
#     print("Modern average")
# elif  2020 - 2024 and rating <= 5:                           # everythin modern hit?
#     print("Modern flop")
# elif 2004 - 2019  and rating <= 8.1:
#     print("Recent hit")
# elif 2004 - 2024 and rating >= 8 and rating <= 5.1:
#     print("Recent average")
# elif  2004 - 2019 and rating <= 5:
#     print("Recent flop")
# elif 2003 - 1888  and rating <= 8.1:
#     print("Certified classic")
# elif 2003 - 1888 and rating >= 8 and rating <= 5.1:
#     print("Old but good")
# elif  2003 - 1888 and rating <= 5:
#     print("Old flop")

#     print(Percy_Jackson)

# for i in range (1,11):
#     print(i)

# x = int(input("Enter a number"))
# for i in range (1, 60):
#     print(x * i)

# for i in range (1,51):
#     if i % 2 == 0:
#         print(i)

# x = int(input("Enter a number"))
# for i in range (x, 0, -1):
#     print(i)

# x = (input("Enter string"))
# for i in range (len(x)-1):
#     print(x[i])

# for i in range (1, 50):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)

# count = 0
# for i in range (1, 50):
#      if i % 3 == 0 and i % 5 == 0:
#          count += 1
# print(count)

# for i in range (1, 11):       
#     print(i * i)                    

# for i in range (1, 22):
#     if i % 2 == 0:
#         print(i)      

# for i in range (1, 17):
#     if i % 2 == 1:
#         print(i)


# s = {"apple", "bannana", "cherry",}
# string = "bannana"

# if string in s:
#     print("Found")
# else: 
#     print("Not Found")


# s = {1, 2, 3}
# num = 4

# if num in s:
#     print("Found")
# else:
#     print("Not Found")


# s = {1, 2, 3, 4, 5}
# print(len(s))


# a = {1, 2, 3}
# b = {3, 4, 5}
# print(3)

# s = {"aplle", "bannana", "cherry"}
# string = "peach"
# if string in s:
#     print("Found")
# else:
#     print("Not Found")


# a = {1, 2, 3}
# b = {4, 5, 6}
# union_string_len = 6

# union_string = a | b
# if union_string_len == 6:
#     print("No Overlap")
# else:
#     print("Overlap")

l1 = [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
l3 = [4, 5, 6, 7]
ans = set(l1) & set(l2) & set(l3)
print(ans)