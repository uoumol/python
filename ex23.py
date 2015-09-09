# script name:batch_file_rename.py
#from:https://github.com/geekcomputers/Python/blob/master/batch_file_rename.py
#description:batch rename a group of files in a given directory,once you pass
#			 the current and new extensions

import os
import sys

work_dir=sys.argv[1]
old_ext=sys.argv[2]
new_ext=sys.argv[3]

files=os.listdir(work_dir)
for filename in files:
	file_ext=os.path.splitext(filename)[1]
	if old_ext==file_ext:
		newifle=filename.replace(old_ext,new_ext)
		os.rename(
				os.path.join(work_dir,filename),
				os.path.join(work_dir,newfile))