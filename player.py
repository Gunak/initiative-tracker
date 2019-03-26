from creature import Creature


# class Player(Creature):
# 	def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma, name):
# 		super().__init__( strength, dexterity, constitution, intelligence, wisdom, charisma)
# 		self.name = name

class Player(Creature):
	def __init__(self, name):
		Creature.__init__(self)
		self.name = name
		

	def __repr__(self):
		return "In Player class"