# Making my own game similar to exercise 35.

import random
import sys


def sword_attack(player, npc):

	# Choose a random number from 0 - 50
	ran_num = random.randint(0, 51)

	print("You attack with a swift, albeit medium to low strength, slash to your enemy.")

	# If ran_num is divisible by 5, then the attack is strong enough to kill the enemy.
	if ran_num % 5 == 0:
		print("Your attack is strong enough to deal a killing blow..\n\n")
		dead(npc)
	else:
		print("Oh, no! Your attack was not strong enough to deplete the enemy's Hit Points.")
		enemy_turn(player, npc)


def lance_attack(player, npc):
	print("You decided to use a heavy weapon.")
	print("However, this move is too slow so the enemy has a chance to move before you.")
	print("If the enemy's move is not enough to kill you, you win on the next turn.")
	print("{} has initiated his move...\n\n".format(npc))
	enemy_turn(player, npc, lance_attack_call=True)


def reinforcements(player, npc):
	print("You call for reinforcements.")

	# random number to decide the luck of calling this move.
	call_for_help = random.randint(1, 51)

	# I will use the fact that any non-zero value evaluates to True. So in this case, after the number has been
	# divided and there is a remainder, a non-zero value, it means the number is not divisible evenly. It also means
	# the parentheses evaluates to True. But by using "not" I am asking for the opposite, in this case, I'm asking for
	# numbers divisible by 10.
	if not (call_for_help % 10):  # If number is divisible by 10
		print("FOR THE EMPEROR!!!!")
		print("Help has arrived, the Emperor's Guard is here to annihilate all the darkness in front of them.")
		dead(npc)
	elif not (call_for_help % 4):  # If number divisible by 4
		print("Help has arrived..... for {}!".format(npc))
		dead(player)
	else:
		print("You are alone in this quest!!")
		print("No one came to your help")
		enemy_turn(player, npc)


def negotiate(player, npc):
	print("You ask {} if he would like to finish this battle next time as it seems you're both equally "
		  "matched.".format(npc))
	print("He asks if you can guess a type of an item he has in his legendary inventory, then he will retreat as a"
		  "gesture of respect for someone knowledgeable in Legendary artifacts.")

	inventory = [
		"ring of fire", "axe of despair", "staff of the forbidden one",
		"lance of anubis", "hammer of olympus", "dagger of the damned", "crystal of helena",
		"shield of a thousand bones", "bow of dragons", "sword of a thousand truths"
	]

	user_guess = input("Enter the type of weapon he might have: ")

	# Set a boolean variable to determine if and when to run the enemy_turn() function.
	loop_continue = True

	for item in inventory:
		item_type = item.split(" ")[0]
		if user_guess == item_type:
			print("That's correct, I have a {}.".format(item_type))
			print("Now tell me the full name of this Legendary Item.")

			item_full_name_guess = input("Type in the name now: ").upper()

			if item_full_name_guess == item.upper():
				print("You're correct, its name is the {}".format(item_full_name_guess))
				run(npc)  # This function has an exit code to exit the loop after been called.
			else:
				print("Blasphemy! Let's us finish this duel.")
				loop_continue = False
				break

	if not loop_continue:
		enemy_turn(player, npc)


def run(target, lose_xp=False):
	print("{} decided to leave.".format(target))
	print("Both parties survived this encounter until the next time they meet again for a decisive duel.")
	if lose_xp:
		print("No XP earned =(")
	sys.exit(0)


def dead(character):
	print("{} is no more!".format(character))
	sys.exit(0)


def enemy_turn(player, npc, lance_attack_call=False):

	# The boolean lance_attack_call is used to know if the lance_attack function invoked this enemy_turn function

	# Create the random number to decide the luck of the actions
	randy = random.randint(1, 51)

	print("The enemy charges at you. He uses his psychic and necromatic powers against you.\n\n\n")

	if randy % 5 == 0:
		print("but..\nThere is a moment of hesitation coming from the enemy.")
		print("It seems he had been made aware of something, or perhaps given up.")
		start(player, npc)
	elif randy % 10 == 0 and lance_attack_call:
		print("There is a moment of hesitation coming from the enemy.")
		print("Your lance attack strikes {} with tremendous power.".format(npc))
		dead(npc)
	else:
		print("The enemy succeeds in striking you.")
		print("'In the face of death, I shall have no remorse'")
		dead(player)


def intro():
	print("You are fighting the legendary Dark Paladin. You are both at each other's end.")
	print("It is your turn to move and finish this quest or perish in your noble sacrifice.")
	print("Choose wisely as your option may leave him alive on the next turn and kill you.")


def start(player, npc):
	print("""What would you like to do:
	1) Use one-handed sword (It's swift and he can't block it on time, but it is not strong and might not kill him).
	2) Use Lance of Helena (A heavy weapon sure to kill him, but too slow and he will move before you).
	3) Call for reinforcements (You will forgo your turn and wait for help to arrive. It might be a legion, or no one).
	4) Negotiate and convince him to stop his evil ways.
	5) Run (End the skirmish and lose all XP but still be alive).
	""")

	while True:

		choice = input("\nEnter the number: ")

		if choice == "1":
			sword_attack(player, npc)
		elif choice == "2":
			lance_attack(player, npc)
		elif choice == "3":
			reinforcements(player, npc)
		elif choice == "4":
			negotiate(player, npc)
		elif choice == "5":
			run(player, lose_xp=True)
		else:
			print("That is not a choice!")


me = input("Choose your name: ")
enemy = "The Dark Paladin of Chaos"
intro()
start(me, enemy)
