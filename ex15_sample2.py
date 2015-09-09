def again():
	print("type the filename again:")
	file_again=input('>')
	
	txt_again=open(file_again)
	
	print(txt_again.read())
while again()!=0:
	again()
	break