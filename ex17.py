from sys import argv ; from os.path import exists; script, from_file, to_file = argv ; print(f"Copying from {from_file} to {to_file}") ; in_file = open(from_file).read(); print(f"The input in file is {len(in_file)} bytes long") ; print(f"Does the output file exists? {exists(to_file)}") ; print("Ready, hit RETURN to continue, CTRL + C to abort.") ; input(); out_file = open(to_file, 'w') ; out_file.write(in_file) ; print("Alright, all done.") ; out_file.close()

# You don't need to close "in_file" because using "read()" automatically closes the file after.

