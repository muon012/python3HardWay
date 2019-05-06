import sys
import random


class Scene(object):

	# The amount of survivors and ammunition stats you have obtained so far
	player_survivors_ammo = [0, 0]

	@staticmethod
	def enter():
		print("This is the Scene class")

	@staticmethod
	def choose_destination():
		print("Keep forward or back?")
		destination = input("Type 'forward' or 'back':  ").lower()
		return destination

	@staticmethod
	def check_survivors():
		print("Do you want to check for survivors?")
		check = input("Y/N: ").lower()
		return check

	@staticmethod
	def check_ammo():
		print("Do you want to check for ammo?")
		check = input("Y/N: ").lower()
		return check

	@classmethod
	def display_stats(cls):
		total_survivors_ammo = cls.player_survivors_ammo
		print("You have rescued: {} survivors, and have {} in ammo.".format(total_survivors_ammo[0], total_survivors_ammo[1]))

	@classmethod
	def update_stats(cls, survivor_count, ammo_count):
		cls.player_survivors_ammo[0] += survivor_count
		cls.player_survivors_ammo[1] += ammo_count

	@classmethod
	def room_stats_flow(cls, room_attribute):

		survivors_input = cls.check_survivors()
		ammo_input = cls.check_ammo()

		# Actions if player decides to scan for survivors
		if survivors_input == 'y':
			if room_attribute[0] == 0:
				print("There are no more survivors. ")
			else:
				room_attribute[0] -= 1
				cls.update_stats(1, 0)  # Update the player's stats in the Scene class attribute
		elif survivors_input == 'n':
			print("I must prioritize the directive.")
		else:
			print("Sorry, command not recognized.")

		# Actions if player decides to scan for ammunition
		if ammo_input == 'y':
			if room_attribute[1] == 0:
				print("There's no more ammo. ")
			else:
				room_attribute[1] -= 1
				cls.update_stats(0, 1)  # Update the player's stats in the Scene class attribute
		elif ammo_input == 'n':
			print("Did not check for ammunition.")
		else:
			print("Sorry, command not recognized.")

		# Display the current stats for the player
		cls.display_stats()

	@staticmethod
	def enemy_intro():
		print("An enemy has entered the room and is ready to attack you.")

	@classmethod
	def attack(cls, following_scene):

		possible_inputs = ["yes", "y", "no", "n"]

		in_combat = input("Do you want to engage in combat with the enemy? ").lower()

		while in_combat not in possible_inputs:
			print("Please enter an appropriate command.")
			in_combat = input("Do you want to engage in combat with the enemy? ").lower()

		if in_combat == 'y' or in_combat == "yes":
			print("You decide to shoot your plasma rifle at the enemy.")

			# Create variable to decide random chance of successful attack
			random_var = random.randint(20, 40)

			# Divisible by 2
			if not random_var % 2:
				print("Enemy is downed!")
				return following_scene
			else:
				print("Attack missed!")
				return 'death'

		elif in_combat == 'n' or in_combat == "no":
			print("You decide to focus on the mission hoping the enemy will not cause too much trouble, but you were "
				  "too unrealistic!")
			return 'death'
		else:
			print("Command not recognized!")
			return 'death'


class Barracks(Scene):

	# The amount of survivors and ammunition in the room
	survivors_ammo = [5, 0]

	def enter(self):

		# Display how many survivors and ammo you have so far.
		super(Barracks, self).display_stats()

		print("\nThis is the Barracks.")

		# Check for survivors/ammo according to user's input
		super(Barracks, self).room_stats_flow(Barracks.survivors_ammo)

		# Randomize the presence of an enemy:
		enemy_presence_randomizer = random.randint(1, 9)

		scene_result = "armory"

		if enemy_presence_randomizer % 2:
			super(Barracks, self).enemy_intro()
			scene_result = super(Barracks, self).attack("armory")

		return scene_result


class Armory(Scene):

	# The amount of survivors and ammunition in the room
	survivors_ammo = [1, 6]

	def enter(self):

		# Display how many survivors and ammo you have so far.
		super(Armory, self).display_stats()

		print("\nThis is the Armory.")

		# Check for survivors/ammo according to user's input
		super(Armory, self).room_stats_flow(Armory.survivors_ammo)

		# Randomize the presence of an enemy:
		enemy_presence_randomizer = random.randint(1, 9)

		scene_result = "engine_room"

		if enemy_presence_randomizer % 2:
			super(Armory, self).enemy_intro()
			scene_result = super(Armory, self).attack("engine_room")

		return scene_result


class EngineRoom(Scene):

	# The amount of survivors and ammunition in the room
	survivors_ammo = [4, 2]

	def enter(self):

		# Display how many survivors and ammo you have so far.
		super(EngineRoom, self).display_stats()

		print("\nThis is the Engine Room.")

		# Check for survivors/ammo according to user's input
		super(EngineRoom, self).room_stats_flow(Armory.survivors_ammo)

		# Randomize the presence of an enemy:
		enemy_presence_randomizer = random.randint(1, 9)

		scene_result = "the_bridge"

		if enemy_presence_randomizer % 2:
			super(EngineRoom, self).enemy_intro()
			scene_result = super(EngineRoom, self).attack("the_bridge")

		return scene_result


class TheBridge(Scene):

	# The amount of survivors and ammunition in the room
	survivors_ammo = [8, 1]

	def enter(self):

		# Display how many survivors and ammo you have so far.
		super(TheBridge, self).display_stats()

		print("\nThis is the Bridge.")

		# Check for survivors/ammo according to user's input
		super(TheBridge, self).room_stats_flow(TheBridge.survivors_ammo)

		# Randomize the presence of an enemy:
		enemy_presence_randomizer = random.randint(1, 9)

		scene_result = "finished"

		if enemy_presence_randomizer % 2:
			super(TheBridge, self).enemy_intro()
			scene_result = super(TheBridge, self).attack("finished")

		return scene_result


class Finished(Scene):

	def enter(self):
		print("\nGood Job! You won.")
		return 'finished'


class Death(Scene):

	def enter(self):
		print("\nYou're dead!")
		input()
		sys.exit(1)


class Map(object):

	scenes = {
		'armory': Armory(),
		'barracks': Barracks(),
		'engine_room': EngineRoom(),
		'the_bridge': TheBridge(),
		'finished': Finished(),
		'death': Death()
	}

	def __init__(self, opening_room):
		self.opening_room = opening_room

	@classmethod
	def next_scene(cls, room):
		event = cls.scenes.get(room)
		return event

	def opening_scene(self):
		return self.next_scene(self.opening_room)
