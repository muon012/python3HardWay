from ex45_scenes import Map, Scene, Barracks, Armory, Death


class Engine(object):

	def __init__(self, opening_map):
		self.opening_map = opening_map

	def play(self):

		# Set the current(first) scene as the map passed to this class.
		current_scene = self.opening_map.opening_scene()
		# Set the last scene as the next_scene method with argument 'finished'.
		last_scene = self.opening_map.next_scene('finished')

		# Make sure the current_scene is not the last_scene, the scene with 'death'
		while current_scene != last_scene:
			# The next scene name will be returned from the enter() method from the current_scene
			next_scene_name = current_scene.enter()
			current_scene = self.opening_map.next_scene(next_scene_name)

		# We enter to the current_scene with its method enter()
		current_scene.enter()


game_map = Map('barracks')
game_engine = Engine(game_map)
game_engine.play()