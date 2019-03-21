import random
import os


class Roll():
	def __init__(self, dice):
		self.dice = dice

	def parse_dice(self):
		split = self.dice.split('d')
		return split

	def roll_dice(self):
		quantity = int(self.parse_dice()[0])
		sides = int(self.parse_dice()[1])

		count = 0
		for i in range(quantity):
			roll = random.randint(1, sides)
			print("Roll {0}: {1}".format(i+1, roll))
			count += roll
		print("Total: {0}".format(count))


	def roll_ability_scores(self, sets=6):

		os.system('cls' if os.name == 'nt' else 'clear')
		print("Rolling ability scores.\n\n")
		DICE_PER_ROLL = 4
		for i in range(sets):
		 	score = []
		 	for j in range(4):
		 		score.append(random.randint(1,6))
		 	
		 	print('Roll 1: {0}\nRoll 2: {1}\nRoll 3: {2}\nRoll 4: {3}'.format(score[0],score[1],score[2],score[3]))
		 	score.sort()
		 	print(score[1] + score[2] + score[3])
		 	print()

if __name__ == "__main__":
	r = Roll('3d6')
	# r.parse_dice()
	r.roll_ability_scores()