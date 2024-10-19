#STRING METHODS IN PYTHON =>    

name = "Nishant Kumar"
print(name.upper())  #converts string to upper case

print(name.strip(" "))   #strips the string using provided character

print(name.replace("nishant","abc"))   #replaces characters in strings

print(name.split(" "))  # splits and converts the string to list 

print(name.capitalize())  #capitalises the first letter of string

print(name.center(50," "))  # centers the string as per the value provided and character 

print(name.count("n"))   # counts the repetitions of the provided character in the given string

print(name.endswith("a"))   # returns true if string ends with given character

print(name.endswith("t",0,7))   # slices the string and then returns true if it ends with provided character

print(name.find("an"))   #returns index of the first occurance of the provided input

print(name.index("K"))   # provides index of first occurance of the given character 

print(name.isalnum())    # return true if string only contains chars like A-Z,a-z,0-9 only!!

print(name.isalpha())   # returns true if string only contains chars like A-Z,a-z only!!

print(name.islower())    # returns true if all characters are in lower case in string

print(name.isupper())    # returns true if all characters are in upper case in string    
 
print(name.isprintable())   # returns true if string is printable (characters like \n are not printable)

print(name.isspace())     # returns true if string only contains white spaces

print(name.istitle())     # returns true if first letter of every word in string is capital

print(name.startswith("N"))    #returns true if string starts with given character

print(name.title())       # it capitalises the first letter of every word in the string