import random, sys

# Load dictionary
with open("test.csv") as f:
	dictionary = f.readlines()
i = 0
for x in dictionary:
	dictionary[i] = dictionary[i].rstrip("\n")
	i += 1

# Intro text
print("Anagram brute-forcer")
print("WARNING: Painfully inefficient...")
print("...but fun")
print("We randomise the anagram and search for it in")
print("~58,000 dictionary words")

try:
	sys.argv[1]
except:
	pass
else:
	# If --help called then show help and close
	if sys.argv[1] == "--help" or "help" or "?":
		print("solver.py 1 2 3")
		print("arg 1 - an anagram to solve")
		print("arg 2 - Whether or not to find all possibilities or just the first (1 or 0, where 1 is all)")
		print("arg 3 - Whether or not to log attempt number (1 or 0, where 1 is log all)")
		print("or solver.py --help for this help screen")
		
		# Exit
		sys.exit()

# Get parameters or user input
# Look to see is the parameters are defined
try:
	sys.argv[1]
	sys.argv[2]
	sys.argv[3]
except:
	# Get the users anagram to solve
	inputVal = raw_input("Enter your anagram (Or 'demo' for a demo):\n")
	
	# If they wanted a demo, arrange that for them
	if inputVal == "demo":
		# Randomly select a word we have in our stockpile
		tval = random.randint(10, 100)
		inputVal = dictionary[tval]
		
		# Randomise it
		inputVal = ''.join(random.sample(inputVal,len(inputVal)))
		print("Using '" + inputVal + "' for a demo")
		
		# Ask the user if they want to cheat and be told it before its cracked
		if raw_input("Do you want the answer now? (y/n):\n").lower() == "y":
			print("It's '" + dictionary[tval] + "'")
	
	# Ask if the user wants to have every possible solution be found or only the first we find
	findAll = raw_input("Should we keep going and find all possible anagrams (y/n) (default n):\n")
	if findAll.lower() == "y":
		findAll = 1
	else:
		findAll = 0
	
	# Ask the user if they want to see the attempt numbers or only the solutions
	logAttempts = raw_input("Should we log all attempts (y/n) (default y):\n")
	if logAttempts.lower() == "n":
		logAttempts = 0
	else:
		logAttempts = 1
else:
	# If the parameters are defined then  use them
	inputVal = sys.argv[1]
	findAll = sys.argv[2]
	logAttempts = sys.argv[3]

# Setup
found = []
tries = []
print("Spinning up")
attempt = 1

# Start brute force loop
while 1:
	# Generate random version of anagram
	val = ''.join(random.sample(inputVal,len(inputVal)))
	
	# Check its not already been tried
	if val not in tries:
		# Look for it in the dictionary
		if val in dictionary:
			# Check that that word has not already been found
			if val not in found:
				# Log the word
				print("Attempt: " + str(attempt) + ": We found one '" + str(val) + "'")
				# If the user chose to only find one word then exit now
				# else remember this word so we don't test it again
				if findAll == 0:
					print("Spinning down")
					break;
				else:
					found.append(val)
		# Log the attempt number but only if its a multiple of 1000
		# to reduce console spam
		if (attempt % 1000) == 0:
			if logAttempts == 1:
				print("Attempt: " + str(attempt))
			
		# Increment the attempt
		attempt += 1
		
		# Remember this try so we don't do it again
		tries.append(val)

# Stop the program exiting immediately
raw_input("Press enter to exit")
