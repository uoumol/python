from sys import argv
from os.path import exists

script,file1,file2= argv

source = open(file1).read()
print(source)

file_again=open(file2,'w')
file_again.write(source)

file_change.close()