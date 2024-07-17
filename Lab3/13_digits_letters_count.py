#problem 13
string = input("Enter a string: ")
letter=0
digit = 0
for character in string:
    if character.isalpha():
        letter+=1
    elif character.isdigit():
        digit+=1 
    

print(f"The number of letters is: {letter}")
print(f"The number of digits is: {digit}")