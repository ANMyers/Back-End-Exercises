import sys

class Cars():


	def __init__(self):
		self.car_models = list()
		self.car_makes = list()
		self.generated_list = dict()

	def read_models(self):
		with open('car_models.log', 'r') as car_models:
			for each in car_models:
				each = each.replace('\n', '')
				self.car_models.append(each)

	def read_makes(self):
		with open('car_makes.log', 'r') as car_makes:
			for every in car_makes:
				every = every.replace('\n', '')
				self.car_makes.append(every)

	def generate_list(self):
		
		self.read_models()
		self.read_makes()

		# print("\n---Makes---")
		for make in self.car_makes:
			self.generated_list[make] = list()

			for model in self.car_models:
				if model[0] == make[0]:
					self.generated_list[make].append(model[2:])

		print(self.generated_list)


demonstration = Cars()

if __name__ == "__main__":
	#print(' '.join(sys.argv))
	try:
		if sys.argv[1] == 'read':
			if sys.argv[2] == 'makes':
				demonstration.read_makes()
			elif sys.argv[2] == 'models':
				demonstration.read_models()
			elif sys.argv[2] == 'all':
				demonstration.generate_list()

	except Exception:
		print("You must specify 'read' followed by either 'makes', 'models' or 'all'.")
