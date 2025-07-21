password_list = []
# i = 0
# while i < 10:
#     user_input = input("Enter a password:")
#     password_list.append(user_input)
#     choice_input = input("enter another?")
#     if choice_input == 'y':
#         i += 1
#     else:
#         break
# print(password_list)

while True:
    password = input("Enter a password:")
    password_type = input("Type of password:")

    password_list.append({
        "password":password, 
        "label":password_type
        })

    choice_input = input("enter another?").lower()
    if choice_input != 'y':
        break

with open('results.txt','a') as file:
    for item in password_list:
        file.write(f"{item}\n") 
print(f"saved passwords:{password_list}")
