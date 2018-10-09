def flatterer(flattererDef):
	print("Welcome to",flattererDef)
	myName = input("What is your name?")
	if(myName == "Alex"):
		print(myName,"is great!")
	else:
		print("Hello",myName)

flatterer("Alex's Flatterer")