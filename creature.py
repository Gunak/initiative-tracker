class Creature:
	"""Base class of creatures, either controlled by the DM or Players themselves."""

	def __init__(self, strength=10, dexterity=10, constitution=10, intelligence=10, wisdom=10, charisma=10):
		self.strength = strength
		self.dexterity = dexterity
		self.constitution = constitution
		self.intelligence = intelligence
		self.wisdom = wisdom
		self.charisma = charisma

	# def __repr__(self):
	# 	return "Creature class __repr__"

	# def __str__(self):
	# 	return f"\nstrength: {self.strength}\ndexterity: {self.dexterity}\nconstitution: {self.constitution}\nintellegence: {self.intelligence}\nwidsom: {self.wisdom}\ncharisma: {self.charisma}"
	