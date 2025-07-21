password_list = []

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
