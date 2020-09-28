import random

r = random.randint(1,100)
count = 0 
while True:
	count += 1 #count + 1
	num = input('guess the number:')
	num = int(num)
	if num == r:
		print('bomb')
		print('this is', count, 'times')
		break
	elif num < r:
		print('try a bigger number')
	elif num > r: 
		print('try a smaller number')
	print('this is', count, 'times')