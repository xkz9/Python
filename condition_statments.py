# '''
# mood = input ("Do you want to eat ice cream?🍦 ")
# mood = mood.lower()
# ant to eat. Leave me alone!🤬")
# '''if mood == "yes":
#     print("Here. Have one!😊")
# else:
#     print("I dont w
# print("What do you want to eat. \n1. Sushi\n2. Kimchi Fried rice\n3. Kimchi noodles\n4. Wine soaked brisket with a side of caviar and jacket potatoes.") 

# if 3 == 4:
#     print("Equal")
# elif (3 > 4):
#     print("greater")
# else:
#     print("less")

# x = 4
# if x == 4:
#     print("equal")
# elif x >= 4:
#     print("greater or equal")
# elif x > 4:
#     print("greater")
# else:
#     print("default")

# if 3 > 4 or 5 > 4:
#     print("one")
# elif 8 > 4 and 6 > 4:
#     print("two")
# else:
#     print("none")

# T and T = T
# T and F = F
# F and T = F
# F and F = F
# F or F = F 
# F or T = T
# T or T = T
# T or T = F
    
# if 3 > 4 or 5 < 4:
#     print("one")
# elif 8 > 4 and 6 > 4:
#     print("two")
# else:
#     print("none")

# if not(3 < 4):
#     print("one")
# elif 4 > 3:
#     print("two")
# else:
#     print("none")

# if not(4 > 6) and not(8 > 5):
#     print("one")
# elif 4 > 5 or not(5 == 5):
#     print("two")
# else:
#     print("none")

# When there are multiple if statments check all of them and conider the last if 
# statment to the end as a seperate block. Only one statement will execute from there

# if 4 > 3:
#     print("three")
# if 4 > 2:
#     print("four")
# if 5 > 4:
#     print("five")
# elif 4 == 4:
#     print("six")
# elif 4 > 3:
#     print("seven")
# else:
#     print("default")

# if 4 < 3:
#      print("three")
# if 4 > 2:
#      print("four")
# if 5 < 4:
#      print("five")
# elif 4 != 4:
#      print("six")
# elif 4 > 3:
#      print("seven")
# else:
#      print("default")

# x = 3 
# y = 12
# if x <= y and x > 0:
#     print("three")
# if x > y or y < 11:
#     print("four")
# if not(x < 4) and y < 24:
#     print("five")
# elif y != 4:
#     print("six")
# elif y >= x:
#     print("seven")
# else:
#     print("default")

# x = 12
# y = 3
# z = 11
# if (x == 2 and x < 3):
#      print(x)
# if x != 5:
#     print("whatever")
# if x != 5 and y >= 5 and z <= 13:
#      print("its gonna happen")
# if z != 0 or x == 2:
#      print("you say")
# if (not(y < 10)):
#     print("you say")
# elif (x < 10 or x < 5):
#      print("okkkkkkk")
# elif (y < 10 or y <= 0):
#     print("pikachu")
# elif(z == 0 or y ==5):
#     print("pikaboo")
# else:
#     print("Default value")

# nested if/else
# if 3 > 4 and 5 < 3:
#     if 4 > 0 or 5 == 8:
#         print("Nested")

# if 3 < 4 and 5 > 3:
#      if 4 > 0 or 5 == 8:
#          print("Nested")

# if 3 < 4 and 5 > 3:
#       if 4 > 0 or 5 == 8:
#           print("Nested")
#       if 7 >= 6 or 3 != 0:
#         print("nested again")
#       elif (5 - 4) <= 0:
#         print("23")
#       else:
#         print("nested default")
# else:
#     ("outside")

# x = 10
# y = 12
# if x > y:
#     print("x > y")
# elif x < y:
#     print("x < y")
# else:
#     print("x == y")

# a = 5
# b = 5
# if a > b:
#     print("a is greater")
# elif a == b:
#     if a + b == 10:
#         print("Sum is 10")
#     else:
#         print("a is equal to b but sum is not 10")
# else:
#     print("b is greater")

# x = 15
# if x < 10:
#     print("Less than 10")
# elif 10 <= x <= 20:
#     print("In range 10-20")
# else:
#     print("Greater than 20")

# age = 25
# if age < 18:
#     if age < 12:
#         print("Child")
#     else:
#         print("Teen")
# elif age < 30:
#     if age < 21:
#         print("Young Adult")
#     else:
#         print("Adult")
# else:
#     print("Senior")

# a = 2
# b = 4
# if a > b:
#     print("A")
# elif a < b:
#     if b - a > 1:
#         print("B - A > 1")
#     else:
#         print("B - A <= 1")
# else:
#     print("A == B")

# if n % 2 == 0:
#         return "Even"
# elif n % 3 == 0:
#         return "Divisible by 3"
# else:
#         return "Other"

# a, b, c = 10, 20, 30
# if a > b:
#     if b > c:
#         result = "A"
#     else:
#         result = "B"
# elif a < b:
#     if a > c:
#         result = "C"
#     else:
#         result = "D"
# else:
#     result = "E"
# print(result)

# x = 5
# y = -5
# if x > 0:
#     if y > 0:
#         print("Both positive")
#     else:
#         print("x positive, y not positive")
# elif x <= 0:
#     if y <= 0:
#         print("Both not positive")
#     else:
#         print("y positive, x not positive")

# x, y, z = 15, 10, 5
# if x > y > z:
#     print("Descending")
# elif x < y < z:
#     print("Ascending")
# else:
#     print("Neither")

# age = 65
# status = "senior" if age > 60 else "adult"
# if status == "adult":
#     category = "Working class"
# elif status == "senior":
#     if age > 70:
#         category = "Retired"
#     else:
#         category = "Almost retired"
# else:
#     category = "Undefined"
# print(category)

# x = 8
# y = 3
# if x / y > 2:
#     print("x is more than twice y")
# elif x / y == 2:
#     print("x is twice y")
# else:
#     print("x is less than twice y")

# temperature = 30
# humidity = 85
# if temperature > 28 and humidity > 80:
#     comfort = "Hot and humid"
# elif temperature > 28 or humidity > 80:
#     comfort = "Hot or humid"
# else:
#     comfort = "Comfortable"
# print(comfort)