# Simple contact book

# copyright of this code has Abdirizak abdullahi hussein
con = False
while con == False:
	print('Simple contact book ')
	print()
	print('1.Add contact')
	print('2.search contact')
	print('3.change existing contact')
	print('0.Exit')
	User = input()
	if User == '1':
		print()
		print('Add new contact')
		Name = input('Enter contact name: ')
		Phone = input('Enter contact phone: ')
		print()
		print('Saved successfully!')
		print('Name = ' + Name)
		print('Phone = ' + Phone)
		print()
	elif User == '2':
			print()
			print('Search contact .........')
			search = input('Enter contact name or phone: ')
			if search == Name or search == Phone:
				print()
				print('View ...')
				print('Name = ' + Name)
				print('Phone = ' + Phone)
			else:
				print()
				print('No contact found yet ! ')
	if User == '0':
		con = True
	if User == '3':
		print()
		print("Change exit contact")
		print()
		print('Choose what you wanna to change: ')
		print()
		print('1.change name ')
		print('2.change phone number ')
		Ver = input()
		if Ver == '1':
			print()
			nam = input('Enter the name of the contact: ')
			if nam == Name:
				Name = input('Enter new_name:  ')
			else:
				print()
				print('this name not founded ! ')
				print()
		if Ver == '2':
			print()
			nam = input('Enter the Phone  of the contact: ')
			if nam == Phone:
				Phone = input('Enter new_phone:  ')
			else:
				print()
				print('this phone  not founded ! ')
				print()
