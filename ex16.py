from sys import argv

script,filename = argv

print("wr're going to erase %r." % filename)
print("if you don't want that, hit CTRL-C(^c)")
print("if you do want that, hit RETURN")

input('?')

print("opening the file ...")
target = open(filename)
print(target.read())

target = open(filename,'w')
print("Tuncating the file. Goodbye!")
target.truncate()

print("now i'm going to ask you for three lines.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("i'm going to write these to the file")

target.write(line1+"\n"+line2+"\n"+line3+"\n")
target.write("\n")
target.write("%s %s" %(line1,line2))
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally, we close it")
target.close()