import pickle

class Notes:

	def __init__(self):
		self.all_notes = []
		try:
			self.all_notes = self.deserialize()
		except FileNotFoundError:
			pass

	def list_notes(self):
		[
			print(str(key) + ': ' + note)
			for key,note in enumerate(self.all_notes)
		]

	def prompt(self):
		note = input("Enter quick note > ")

		if note == "ls":
			self.list_notes()

		elif note == "rm":
			self.list_notes()
			deleted = input("Which one? > ")
			del(self.all_notes[int(deleted)])

		elif note != "quit":
			self.all_notes.append(note)
			self.serialize()

		if note != 'quit': self.prompt()

	def serialize(self):
		with open('notes.txt', 'wb+') as f:
			pickle.dump(self.all_notes, f)

		# with open('notes.txt', 'rb') as f:
		# 	binary = f.read()

		# return binary


	def deserialize(self):
		try:
			with open('notes.txt', 'rb+') as f:
				self.all_notes = pickle.load(f)
		except EOFError:
			pass

		return self.all_notes






