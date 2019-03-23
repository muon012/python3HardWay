class Song(object):

	"""
	I have added an extra function according to the study drills from the book.
	"""

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

	def sing_this_variable(self, lyrics_list):
		for line in lyrics_list:
			print(line)


happy_bday = Song([
	"Happy birthday to you",
	"I don't want to get sued",
	"So I'll stop right there"
	])

bulls_on_parade = Song([
	"They rally around tha family",
	"With pockets full of shells"
	])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

hokey_pokey = [
	"You put your right foot in",
	"You put your right foot out",
	"You put your right foot in",
	"You put your right foot out",
	"And you shake it all about",
	"You do the hokey pokey",
	"And you turn yourself around",
	"That's what is all about"
]

hp = Song("The lyrics are passed as an argument to another method")
print()
hp.sing_this_variable(hokey_pokey)
