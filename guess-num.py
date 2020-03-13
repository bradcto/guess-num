import random

r = random.randint(1, 100)
while True:	
	num = input('Input number for guess : ')
	num =int(num)
	if num == r:
		print('You''re Right')
		break
	elif num > r:
		print('Your num is bigger ')
	elif num < r:
		print('Your num is smaller')
