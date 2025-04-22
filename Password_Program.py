
print("Your password must meet the below criteria. It must be: \n"
" - At least 8 characters long. \n "
"- Contain at least one uppercase letter (A-Z). \n"
" - Contain at least one number (0-9). \n"
" - Contain at least one special character (e.g !@#$%^&*()_+). \n")

password = input("Enter your password: ")

special_chars = ["!", "@", "#", "$", "%", "^", "&", "_", "+", "(", ")"]
numbs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


inp_password = list(password)

has_special_chars = True
has_numbs = True
has_upper = False

for item in inp_password:
    if item not in special_chars:
        has_special_chars = False
    if item not in numbs:
        has_numbs = False
    if item.isupper():
        has_upper = True


if has_special_chars and has_numbs or has_upper:
    print("That is a strong password. Well done!")
elif len(password) < 8:
    print("Password too short. Try again.")
else:
    print("Password is weak to moderate. Try again and make sure to follow the criteria above.")

