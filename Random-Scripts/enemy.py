'''
Program: Attack - Classes
Author: Prusko

'''

class Enemy:
	def __init__(self, hp, mp, atkL, atkH):
		self.hp = hp
		self.mp = mp
		self.atkL = atkL
		self.atkH = atkH
	
	def getAttack(self):
		print("Attack Low is", self.atkL)
		print("Attack High is", self.atkH)

	def getHP(self):
		print("HP:", self.hp)
		return self.hp
		
	def getMP(self):
		print("MP:", self.mp)
		return self.mp