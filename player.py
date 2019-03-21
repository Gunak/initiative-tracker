import random


class Character():
	def __init__(self, name, health, AC, initiative):
		self.name = name
		self.health = health
		self.AC = AC
		self.initiative = initiative

	def roll_initiative(self):
		pass