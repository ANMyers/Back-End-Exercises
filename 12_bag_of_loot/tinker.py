import sys

class bag_o_loot:
	def __init__(self, name="Bag 'O' Loot"):
		self.name = name
		self.presents = dict()

	def add_present(self, kid, present):
		if kid in self.presents.items():
			self.presents[kid].add(present)
		else:
			self.presents[kid] = list()
			self.presents[kid].add(present)

	def remove_present(self, kid, present):
		del self.presents[kid]

	def list_presents(self, kid):
		for key, value in self.presents.items():
			print("{} is getting {}.".format(key, value))

	def list_kids_getting_a_presents(self, kid):
		print("\n----Kids Getting Presents----")
		for each in self.presents.items():
			print("{}\n".format(each))

if len(sys.argv) is 4:
	if sys.argv[1] == 'add':
		print("\nYou want to add {} to {}'s list.\n".format(sys.argv[3], sys.argv[2]))
	elif sys.argv[1] == 'remove':
		print("\nYou want to remove {} from {}'s list\n".format(sys.argv[3], sys.argv[2]))
	else:
		print("That command is not recognized, sorry :(")
elif len(sys.argv) is 3:
	if sys.argv[1] == 'ls':
		print("\nYou want to list {}'s presents\n".format(sys.argv[2]))
	else:
		print("That command is not recognized, sorry :(")
elif len(sys.argv) is 2:
	if sys.argv[1] == 'ls':
		print("\nYou want to display all kid's lists\n")
	else:
		print("That command is not recognized, sorry :(")
else:
	print("That command is not recognized, sorry :(")