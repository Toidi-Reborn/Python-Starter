'''
Program: Attack
Author: Prusko

'''

import random
from enemy import Enemy

Monster1 = Enemy(100, 120, 60, 80)
Monster1.getAttack()
Monster1.getHP()

Monster2 = Enemy(222, 333, 40, 50)
Monster2.getAttack()
Monster2.getHP()
Monster2.getMP()














'''
	enemyAttackL = 60
	enemyAttackH = 80

playerHP = 260



while playerHP > 0:
	dmg = random.randrange(enemyAttackL, enemyAttackH)
	playerHP = playerHP - dmg
	
	if playerHP <= 30:
		playerHP = 30
	print("Enemy issues", dmg, "damage to the player", playerHP)		
	
	if playerHP > 30:
		continue
	
	print("Low Health")
	break
	
'''	

