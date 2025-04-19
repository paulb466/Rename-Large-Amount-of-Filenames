import os
 
dir = "/mnt/"

name_start = "Project789.988-"

for root, dirs, files in os.walk(dir):

	for name in files:

		if name.startswith(name_start):

			filename1 = os.path.join(root, name)
			filename2 = name.split(name_start)[1]

			NewFileName = os.path.join(root, filename2)

			print(filename1)
			print(NewFileName)

			os.rename(filename1, NewFileName)