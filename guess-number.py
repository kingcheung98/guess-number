import random
start = input('minimum of random number period:')
end = input('maximum of random number period:')
start = int(start)
end = int(end)

r = random.randint(start, end)
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