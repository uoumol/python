def print_two(*args):
	arg1, arg2 = args
	print("arg1: %r, arg2: %r" % (arg1, arg2))
	
def print_two_again(arg1,arg2):
	print("arg1: %r, arg2: %r" % (arg1, arg2))
	
def print_none():
	print("I got nothin'.")
	
def print_one(arg1):
	print("arg1: %r" % arg1)
	
print_two("huang","lan")
print_two_again("huang","lan")
print_one('first')
print_none()
