import sys, ast

script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
	line = language_file.readline()

	if line:
		print_line(line, encoding, errors)
		return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
	next_lang = line.strip()
	raw_bytes = next_lang.encode(encoding, errors=errors)
	cooked_string = raw_bytes.decode(encoding, errors=errors)

	print(raw_bytes, "<===>", cooked_string)


def decoder():
	with open('ex23_encoded.txt') as f:
		for line in f:
			print(ast.literal_eval(line).decode('utf8'))


languages = open("ex23_languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
print("\n\nHere are the languages decoded from binary:\n\n")
decoder()
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode("utf-8"))

# # Copying the strings from ex23_languages.txt into binary onto another file (ex23_encoded.txt)
# with open("ex23_languages.txt", "r") as fl:
# 	line = fl.readline()
# 	while line:
# 		line = line.strip().encode("utf-8", errors="strict")
# 		with open("ex23_encoded.txt", "a") as encod_file:
# 			print(line, file=encod_file)
# 		line = fl.readline()
