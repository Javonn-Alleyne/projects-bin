from pywebio.input import input
from pywebio.output import put_text

password_list = []

def password_manager():
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
    put_text(password_list)
    
if __name__ == '__main__':
    password_manager()

# with open('results.txt','a') as file:
#     for item in password_list:
#         file.write(f"{item}\n") 
# print(f"saved passwords:{password_list}")