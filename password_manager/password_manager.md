# Porject #1
```python
#ver1
print("enter username")
user_input = input("")
print(user_input)

#ver1.1
user_input = input("enter username:")
print(user_input)

#ver1.3
password_list = []
user_input = input("enter username:")
print(user_input)

#ver1.4
password_list = []
user_input = input("enter username:")
password_list.append(user_input)
print(user_input)

#ver2
password_list = []
choice = False
user_input = input("enter username:")
password_list.append(user_input)
# print(user_input)

#ver2.1
password_list = []
choice = bool
user_input = input("enter username:")
password_list.append(user_input)
# print(user_input)

#ver2.2
password_list = []
choice = ("Do you want to enter a password [y/n]")
if choice = True
user_input = input("enter username:")
password_list.append(user_input)
# print(user_input)

#ver2.3
password_list = []
choice = ("Do you want to enter a password [y/n]")
if choice == 'y':
	user_input = input("enter username:")
	password_list.append(user_input)
else choice == 'n':
# print(user_input)

#ver2.4
password_list = []
choice = ("Do you want to enter a password [y/n]")
if choice == 'y':
	user_input = input("enter username:")
	password_list.append(user_input)
else:
	pass
print(user_input)

#ver2.5
password_list = []
choice = ("Do you want to enter a password [y/n]")
while choice == 'y':
	user_input = input("enter username:")
	password_list.append(user_input)
else:
	pass
print(password_list)

#ver3
password_list = []

#ver3.1
password_list = []
user_input = input("enter a password: ")
user_input.apppend(password_list)
print(password_list)

#ver3.2
password_list = []
user_input = input("enter a password: ")
password_list.append(user_input)
print(password_list)

#ver4
password_list = []
for i in range(5):
	user_input = input("enter a password: ")
	password_list.append(user_input)
	i + 1
print(password_list)

#ver4.1
password_list = []
for i in range(5):
	user_input = input("enter a password: ")
	password_list.append(user_input)
	choice_input = input("continue[y/n]?")
	if choice_input == 'y':
		i + 1
	else:
		break
print(password_list)

#ver4.2
password_list = []
# for i in range(5):
user_input = input("Enter a password:")
password_list.append(user_input)
choice_input = input("enter another?")
if choice_input == 'y':
	i + 1
else:
	print("exit")
print(password_list)

#ver5
password_list = []
i = 0
while i > 0:
	user_input = input("Enter a password:")
	password_list.append(user_input)
	choice_input = input("enter another?")
	if choice_input == 'y':
		i += 1
	else:
		print("exit")
print(password_list)

#ver5.1
while True:
	user_input = input("Enter a password:")
	password_list.append(user_input)
	choice_input = input("enter another?")
	if choice_input != 'y':
		break
print(password_list)

#ver5.2
while True:
	user_input = input("Enter a password:")	
	password_list.append(user_input)	
	choice_input = input("enter another?").lower()	
	if choice_input != 'y':
		break
print(f"saved passwords:{assword_list}")

#ver5.3
while True:
	password = input("Enter a password:")
	password_type = input("Type of password:")
	password_list.append(password + password_type)
	choice_input = input("enter another?").lower()
	if choice_input != 'y':
		break
print(f"saved passwords:{password_list}")

#ver5.3.1
password_list = []
password_label = []
	while True:
	password = input("Enter a password:")
	password_type = input("Type of password:")
	password_list.append(password)
	password_label.append(password_type)
	choice_input = input("enter another?").lower()
	if choice_input != 'y':
		break
print(f"saved passwords:{password_list}")

#ver5.3.2
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
print(f"saved passwords:{password_list}")

#ver6
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
print(f"saved passwords:{password_list}")

with open('results.txt','w') as file:
	file.write(password_list)

#ver6.1
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
results = password_list.to_str()
with open('results.txt','w') as file:
	file.write(results)
print(f"saved passwords:{password_list}")

#ver6.1.1
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
```