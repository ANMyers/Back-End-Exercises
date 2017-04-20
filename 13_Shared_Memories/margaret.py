import sys
import pickle

class Margaret:

	def __init__(self):
		self.whole_dictionary = dict()
		self.deserialize()

	def add_message(self, message):
		try:
			self.whole_dictionary['Margaret'].append(message)
			self.serialize()
		except KeyError:
			self.whole_dictionary['Margaret'] = list()
			self.whole_dictionary['Margaret'].append(message)
			self.serialize()

	def remove_message(self, message):
		try:
			self.whole_dictionary['Margaret'].remove(message)
			self.serialize()
		except KeyError:
			pass

	def list_messages(self):
		for each in self.whole_dictionary['Margaret']:
			print(each)

	def serialize(self):
		with open('messages.txt', 'wb+') as f:
			pickle.dump(self.whole_dictionary, f)

	def deserialize(self):
		try:
			with open('messages.txt', 'rb+') as f:
				self.whole_dictionary = pickle.load(f)
		except (EOFError, FileNotFoundError):
			pass

message_log = Margaret()


if sys.argv[1] == 'add':
	message_log.add_message(sys.argv[2])
elif sys.argv[1] == 'rm':
	message_log.remove_message(sys.argv[2])
elif sys.argv[1] == 'ls':
	message_log.list_messages()