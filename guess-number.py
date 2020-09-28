import random

r = random.randint(1,100)
while True:
	num = input('guess the number:')
	num = int(num)
	if num == r:
		print('bomb')
		break
	elif num < r:
		print('try a bigger number')
	elif num > r: 
		print('try a smaller number')