# mystr = "                               "
# print(mystr)
# print(type(mystr))


# print(mystr[10]) 
# print(mystr[32])    
# print(mystr[-3])     
# print(mystr[-8])      
# print(mystr[30])  
# print(mystr[3])     
# print(mystr[-35])  
# mystr = "Leonardo and Ostap are learning python"

# List slicing

# start is included but end is not included.  
# print(mystr[0:8])  gf
# print(mystr[-39:-30])
# print(mystr[0:-30])
# print(mystr[-39:8])
# print(mystr[32:39])
# print(mystr[-6:])
# print(mystr[32:])
# print(mystr[-6:39])
# substring_2 = original_string[3:10:2]
# print(substring_2)

# origional_string = "               PyThon Is A powErful progRamming lanGUagE        .          "
# reversed_string = original_string[-1:-41:-1]
# print(reversed_string[5:13:1])
# print(original_string[-1:-41:-1])
# print(original_string[-9:-1:1])
# print(original_string[-9:41:1])
# print(original_string[33:-1:1])
# print(original_string[33:41:1])
# print(original_string[6:15:2])
# print(original_string[6])
# print(original_string[8])
# print(original_string[10])
# print(original_string[12])
# print(original_string[14])
# print(original_string[0:10:3])
# mystr = "Python is very easy"
# print(mystr[0:5:2])
# string function 
# print (origional_string.lower())
# print (origional_string.upper())
# print (origional_string.capitalize())

# The count function counts the amount of Letters you put in the brackets in double hashtags.  
# print (origional_string.count("r"))
# print (origional_string.count("q"))

# The find function give you the index of the charicter that you are searching for 
# ,but if the charicter that you are searching for is not present it will 
# give you -1 as a value

# print (origional_string.find("i"))
# print (origional_string.find("I"))
# print (origional_string.find("lanGUagEge"))
# print (origional_string.find("z"))

# The index function is the same as the find function except the index function give
# you an error when the charicter you have serched for is not present in the string

# print (origional_string.index("i")) 
# print (origional_string("z"))

# The endswith fuction checks if the string ends with the particular word searched.  

# print (origional_string.endswith("lanGUagE "))
# print (origional_string.startswith("PyThon"))

# The numeric function checks if the string has any numbers  in it 

# origional_string = "1234567890"
# print (origional_string.isnumeric())    

# THe isalnum function will check if your string has any numbers 
# or letters ,but can only have numbers or letters or the value will 
# appear false spaces = symbols 

# string_2 = "Pythonisaverypowerfulpreogramminglanguage1"
# print (string_2.isalnum())

# Replace changes all the values of the string (which equal the first value) with the second value given.
# print(mystr.replace("a","Hello"))

# The split function cuts out all of the values given and replaces them with ', '.
# print(mystr.split("p")) 

# THe stip function removes all of teh spaces in the string befire and after the text.
# print(mystr.strip())

# The lstip function removes all the spaces on the left hand sinde of the string.
# print(mystr.lstrip())

# The rstrip function removes all the spaces on the right hand sinde of the string.
# print(mystr.rstrip())

# The islower function checks if all your string is lower case.
# print(mystr.islower())

# The isupper function checks if all your string is upper case.
# print(mystr.isupper())

# This function is used to check if a string can be a title of a page or not and changes it to be a title or not.
# print(mystr.title())

# The swapcase fuction changes all of the cases in a string.
# print(mystr.swapcase())

# The isalpha function checks if the string only has alphabetical values and nothing else.
# print(mystr.isalpha())

# The isnumeric function checks if the string only has numbers and nothing else.
# print(mystr.isnumeric())