def flatterer(flattererDef):
	print("Welcome to",flattererDef)
	myName = input("What is your name?")
	if(myName == "Alex"):
		print(myName,"is handsome and good at snuggles!")
	else:
		print("Hello",myName)

flatterer("Alex's Flatterer")