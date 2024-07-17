#Problem 11
user_string= ""
while True:
    new_string = input("Enter a line: ")
    if new_string:
        user_string+=new_string+ "\n"
    else:
        break
        

print(user_string.lower())