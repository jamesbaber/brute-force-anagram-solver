import random, sys

with open("test.csv") as f:
	dictionary = f.readlines()
i = 0
for x in dictionary:
	dictionary[i] = dictionary[i].rstrip("\n")
	i += 1

print("Anagram brute-forcer")
print("WARNING: Painfully inefficient...")
print("...but fun")
print("We randomise the anagram and search for it in")
print("~58,000 dictionary words")

try:
	sys.argv[1]
	sys.argv[2]
	sys.argv[3]
except:
	inputVal = raw_input("Enter your anagram (Or 'demo' for a demo):\n")
	if inputVal == "demo":
		tval = random.randint(10, 100)
		inputVal = dictionary[tval]
		inputVal = ''.join(random.sample(inputVal,len(inputVal)))
		print("Using '" + inputVal + "' for a demo")
		if raw_input("Do you want the answer now? (y/n):\n").lower() == "y":
			print("It's '" + dictionary[tval] + "'")
	
	
	findAll = raw_input("Should we keep going and find all possible anagrams (y/n) (default n):\n")
	if findAll.lower() == "y":
		findAll = 1
	else:
		findAll = 0
		
	logAttempts = raw_input("Should we log all attempts (y/n) (default y):\n")
	if logAttempts.lower() == "n":
		logAttempts = 0
	else:
		logAttempts = 1
else:
	inputVal = sys.argv[1]
	findAll = sys.argv[2]
	logAttempts = sys.argv[3]

found = []
tries = []

print("Spinning up")

attempt = 1
while 1:
	val = ''.join(random.sample(inputVal,len(inputVal)))
	if val not in tries:
		if val in dictionary:
			if val not in found:
				print("Attempt: " + str(attempt) + ": We found one '" + str(val) + "'")
				if findAll == 0:
					print("Spinning down")
					break;
				else:
					found.append(val)
		if (attempt % 1000) == 0:
			if logAttempts == 1:
				print("Attempt: " + str(attempt))
		attempt += 1
		tries.append(val)

print("" * 10)
raw_input("Press enter to exit")
