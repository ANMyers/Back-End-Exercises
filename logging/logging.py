import sys
from datetime import datetime
from time import time

global file_name

def read_log():
	""" Reads from the log file"""
	with open(file_name, 'r') as log_messages:
		print(log_messages.read())

def log(message):
	"""Log a message to the log file
	use "cat messages.log" to show content

	Arguments:
		message -- Any string
	"""

	with open(file_name, 'a+') as logger:
		timestamp = time()
		logger.write("{0}: {1}\n".format(
			datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'),
			str(message)
			))

if __name__ == "__main__":
	try:
		file_name = sys.argv[1]
		if sys.argv[2] == 'r':
			read_log()
		elif sys.argv[2] == 'a':
			log(' '.join(sys.argv[3:]))
	except TypeError:
		pass



