import os
 
dir = "/mnt/"

name_end = "string_to_remove"
file_extension = ".txt"

for root, dirs, files in os.walk(dir):

	for name in files:

		if name.endswith(name_end):

			filename1 = os.path.join(root, name)
			filename2 = name.split(name_end)[0]

			NewFileName = os.path.join(root, filename2+file_extension)

			print(filename1)
			print(NewFileName)

			os.rename(filename1, NewFileName)