import random

random_numbers = list()
squared_numbers = list()

for each in range(20):
	random_numbers.append(random.randint(0,49))

print("\nTwenty random numbers: {}\n".format(random_numbers))

for each in random_numbers:
	squared_numbers.append(each * each)

print("Squared numbers: {}\n".format(squared_numbers))