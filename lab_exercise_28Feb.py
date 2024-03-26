"""
#************** QUESTION-FN1*******************
input_str=input("Enter a string:")
length=len(input_str)
if length<3:
    print("output:",input_str)
else:
    print("output:",input_str[0:3])

#************** QUESTION-FN2*******************
input_str=input("Enter a string:")
length=len(input_str)
while (length<2):
    print("Invalid Input, Enter string of Min length of two characters")
    input_str=input("Enter a string:")
print("output:",input_str[-2:]*5)

"""

#************** QUESTION-1*******************
#print("""'Single' and "Double" quoted string in Python.""")

#************** QUESTION-2*******************
#print("""'Single', "Double" and \"""Triple\"""quoted string in Python.""")
"""
#************** QUESTION-3*******************
char=input("Enter a alphabet:")
print(f"Integer representation of {char} is {ord(char)}")

#************** QUESTION-4*******************
print('abc'*5)

#************** QUESTION-5*******************
print('-'*50)

#************** QUESTION-6*******************
input_str=input("Enter a string:")
print("output:",input_str.upper())

#************** QUESTION-7*******************
input_str=input("Enter a string:")
print("output:",input_str[:2]+ input_str[-2:])


#************** QUESTION-8*******************
input_str=input("Enter a string:")
print("output:",input_str[0]+input_str[1:].replace(input_str[0],'$'))
"""
#************** QUESTION-9*******************
str1=input("Enter the first string:")
str2=input("Enter the second string:")
print("output:",str2[0]+str1[1:]+" "+str1[0]+str2[1:])
