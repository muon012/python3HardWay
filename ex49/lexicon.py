# Game Lexicon

lexicon = {
	'direction': ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back'],
	'verb': ['go', 'stop', 'kill', 'eat'],
	'stop': ['the', 'in', 'of', 'from', 'at', 'it'],
	'noun': ['door', 'bear', 'princess', 'cabinet']
}


def convert_numbers(s):
	# Try to convert the string to an integer if possible, if not, just return the same string back.
	try:
		return int(s)
	except ValueError:
		return s


def scan(sentence):
	results = []
	words = sentence.split()
	for word in words:
		# Loop through the key-value pairs of the lexicon dict until we match the word to any in the dict.
		word_type = "".join([word_types for (word_types, word_values) in lexicon.items() for single_word_value in word_values if single_word_value == word.lower()])
		word = convert_numbers(word)
		if type(word) == int:
			word_type = "number"
		elif word_type not in lexicon.keys():
			word_type = "error"
		results.append((word_type, word))
	return results


sample = "1233 go werweewr FDSDFsdgg2332 princess"
print(scan(sample))

