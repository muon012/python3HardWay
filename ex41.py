import random
from urllib.request import urlopen
import sys

WORD_URL = "https://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class %%%(%%%):":
		"Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)":
	"class %%% has-a __init__ that takes self, and *** params.",
	"class %%%(object):\n\tdef ***(self, @@@)":
	"class %%% has-a function *** that takes self and @@@ params.",
	"*** = %%%()":
	"Set *** to an instance of class %%%.",
	"***.***(@@@)":
	"From *** get the *** function, call it with params self, @@@.",
	"***.*** = '***'":
	"From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
	WORDS.append(str(word.strip(), encoding="utf-8"))


def convert(snippet, phrase):

	# random.sample(list_object, k)
	# this method returns a list of length k with random elements from list_object. The value k must be less than
	# or equal to the length of list_object.
	class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]

	# string_object.count(substring_object, start, end)
	# this method returns the number of occurrences of substring_object in string_object. You can also decide where to
	# start and end looking for these occurrences in the string (optional).
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []

	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1, 3)
		param_names.append(', '.join(random.sample(WORDS, param_count)))

	for sentence in snippet, phrase:
		result = sentence[:]  # this makes a copy of sentence and assigns it to result

		# fake class names
		for word in class_names:
			# replace(old_string, new_string, count)
			# this string method replaces all the occurrences of 'old_string' in a string with 'new_string. You can also
			# decide how many times to replace that with 'count' (optional) instead of all which is the default when
			# 'count' is not specified.
			result = result.replace("%%%", word, 1)

		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)

		# fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)

		results.append(result)

	return results


# keep going until they hit CTRL + D
try:
	while True:
		snippets = list(PHRASES.keys())
		random.shuffle(snippets)

		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question

			print(question)

			input("> ")
			print(f"ANSWER: {answer}\n\n")
except EOFError:
	print("\nBye")


