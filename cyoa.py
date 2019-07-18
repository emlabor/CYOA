class Stats:
	def __init__(self, health, strength):
		self.health = health
		self.strength = strength

def instructions():
	print('''THE POWER HAS GONE OUT IN NEW YORK CITY. 
		YOUR TASK IS TO GET HOME BEFORE MIDNIGHT. 
		I WILL BE YOUR HANDS AND EYES. DIRECT ME 
		WITH THE NUMBER KEYS.''')

def show_time(time):
	print("CURRENT TIME: ", time)

def process_input():
	a = input()
	while (a != "1" and a != "2"):
		a = input("CHOOSE 1 OR 2: ")
	return a

def phone_flashlight():
	print('''YOU ARE NOW LOSING POWER. MAKE DECISIONS WISELY.
		1. HEAD WEST	2. HEAD NORTH''')

def west_north():
	a = process_input()

def main():
	stats = Stats(100, 100)
	time = 20.00

	instructions()
	show_time(time)
	print('''BEFORE YOU CAN CONTINUE, YOU NEED A SOURCE OF LIGHT. YOUR PHONE IS AT 15%.
		1. USE YOUR PHONE FLASHLIGHT	2. BUY A REAL FLASHLIGHT''')
	a = process_input()
	if (a == "1"):
		show_time(time)
		phone_flashlight()
	else:
		time += 0.15
		show_time(time)
		print('''YOU ARE IN LINE AT CVS WITH A FLASHLIGHT. AS YOU APPROACH THE REGISTER,
		YOU SEE A SIGN THAT READS: NOT ACCEPTING CARD DUE TO POWER OUTAGE.
		YOU HAVE LESS THAN A DOLLAR IN CASH.
		1. USE YOUR PHONE FLASHLIGHT	2. STEAL THE FLASHLIGHT''')
		a = process_input()
		if (a == "1"):
			show_time(time)
			phone_flashlight()
		else:
			show_time(time)
			print('''THE WOMAN AT THE REGISTER SEES YOU TAKE THE FLASHLIGHT.
		SHE WILL REMEMBER YOUR FACE.
		1. HEAD WEST	2. HEAD NORTH''')

if __name__ == "__main__":
	main()