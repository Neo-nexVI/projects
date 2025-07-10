'''
Project #1: Password Manager
Description: A simple password manager using python
Purpose: stores a password for a user
Date: 2025-07-10
'''

password_list = []

while True:
	username      = input("Enter you're username:")
	password      = input("Enter you're password:")
	password_type = input("What type of password: (email,work,personal)")
	password_list.append({
		"username":username,
		"password":password,
		"label"   :password_type
		})
	
	user_choice = input("Enter another password?").lower()
	if user_choice != 'y':
		break

with open('results.txt','a') as file:
	for item in password_list:
		file.write(f"{item}\n")
print(f"saved passwords:{password_list}")