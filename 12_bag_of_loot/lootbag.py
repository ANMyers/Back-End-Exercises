import sys
import uuid

class bag_o_loot():

	def __init__(self):
		pass

	def add_present(self, child, toy):
		""" Allows user to add a toy to a child's list
		
		Arguments:
			child - String
			toy - String
		 """

		child_id = uuid.uuid4() #universially unique id
		try:
			set_child_list = set()
			delivered_child_list = list()
			children_list = set()
			with open('children/delivered.log', 'r') as delivered_list:
				delivered_child_list = delivered_list.read().split('\n')
				for kid in delivered_child_list:
					if ';;' not in kid:
						pass
					else:
						children_name, delivered = kid.split(';;')
						children_list.add(children_name)
				need_to_add = True
				for each in children_list:
					if each == child:
						need_to_add = False
					else:
						pass
				if need_to_add == True:
					delivered_child_list.append("{};;False".format(child))
					delivered_child_list = '\n'.join(delivered_child_list)
					with open('children/delivered.log', 'w') as delivered_list:
						delivered_list.write(delivered_child_list)
				else:
					pass

		except FileNotFoundError:
			with open('children/delivered.log', 'w') as child_list:
				child_list.write("{};;False\n".format(child))

		try:
			with open('children/children.log', 'r') as child_list:
				set_child_list = child_list.read().split('\n')
				set_child_list = set(set_child_list)

				set_child_list.add("{}".format(child))
				set_child_list = '\n'.join(set_child_list)

			with open('children/children.log', 'w') as child_list:
				child_list.write(set_child_list)

		except FileNotFoundError:
			with open('children/children.log', 'w') as child_list:
				child_list.write("{}\n".format(child))


		try:
			with open('children/{}.log'.format(child), 'a+') as present_list:
				present_list.write("{}\n".format(toy))

		except FileNotFoundError:
			with open('children/{}.log'.format(child), 'w') as present_list:
				present_list.write("{}\n".format(toy))


	def remove_present(self, child, toy):
		""" Allow the user to remove a present from a child's list

		Arguemnts:
			child - String
			toy - String
		"""
		present_list = list()

		try:
			with open("children/{}.log".format(child), 'r') as presents:
				presents_list = presents.read().split('\n')
				for each in presents_list:
					if toy == each:
						presents_list.remove(each)
					else:
						print("\n{}'s list does not contain {}\n".format(child, toy))
				presents_list = '\n'.join(presents_list)

			with open("children/{}.log".format(child), 'w') as presents:
				presents.write(presents_list)

		except FileNotFoundError:
			print("Child by that name does not exist on the presents list.")

	def list_presents(self, child):
		""" Allow the user to list the presents for a particular child

		Arguemnts:
			child - String
		"""
		try:
			with open("children/{}.log".format(child), 'r') as presents:
				print("{}'s listed presents: \n{}".format(child, presents.read()))
				returned_list = list()
				for each in presents:
					returned_list.append(each)
				return returned_list


		except FileNotFoundError:
			print("{} does not have any presents.".format(child))

	def list_children(self):
		""" Allow a user to list all the children who have present lists

		Arguemnts:
			n/a
		"""
		with open('children/children.log', 'r') as child_list:
			print("\n----Children----")

			print(child_list.read())
			childrens_list = list()
			for each in child_list:
				childrens_list.append(each)
			return childrens_list


	def list_all_presents(self):
		""" Allow the user to list all presents for all children

		Arguemnts:
			n/a
		"""
		with open('children/children.log', 'r') as child_list:
			for each in child_list:
				try:
					each = each.replace('\n', '')
					print("\n---{}'s presents---".format(each))
					with open('children/{}.log'.format(each), 'r') as child_presents:
						print(child_presents.read())
						list_of_presents = list()
						for each in child_presents:
							list_of_presents.append(each)
						return list_of_presents
						
				except FileNotFoundError:
					pass

	def get_if_delivered(self, child):
		""" Allow the user to show whether a child's presents have been delivered

		Arguments:
			child - String
		"""
		dictionary_of_child = dict()
		with open('children/delivered.log', 'r') as delivered_list:
			delivered_child_list = delivered_list.read().split('\n')
			for kid in delivered_child_list:
				if ';;' not in kid:
					pass
				else:
					children_name, delivered = kid.split(';;')
					if child == children_name:
						dictionary_of_child[child] = dict()
						dictionary_of_child[child]['delivered'] = delivered
						print("{}'s delivered value is {}".format(child, delivered))
						return dictionary_of_child[child]
			print("Child not found")

	def deliver_to_child(self, child, if_delivered=True):
		""" Allow the user to change whether a child's presents have been delivered

		Arguments:
			child - String
		"""

		dictionary_of_child = dict()
		delivered_child_list = list()

		with open('children/delivered.log', 'r') as delivered_list:
			delivered_child_list = delivered_list.read().split('\n')
			for kid in delivered_child_list:
				if ';;' not in kid:
					pass
				else:
					if child in kid:				
						dictionary_of_child[child] = dict()
						if if_delivered == 'True':
							kid.replace('False', 'True')
							dictionary_of_child[child]['delivered'] = True
							print("{}'s delivered value is {}".format(child, True))
							with open('children/delivered.log', 'w') as delivered_list:
								delivered_child_list = '\n'.join(delivered_child_list)
								delivered_list.write(delivered_child_list)
						else:
							kid.replace('True', 'False')
							dictionary_of_child[child]['delivered'] = False
							print("{}'s delivered value is {}".format(child, False))
							with open('children/delivered.log', 'w') as delivered_list:
								delivered_child_list = '\n'.join(delivered_child_list)
								delivered_list.write(delivered_child_list)

		return dictionary_of_child[child]

		
demonstration = bag_o_loot()

if len(sys.argv) is 4:
	if sys.argv[1] == 'add':
		demonstration.add_present(sys.argv[2], sys.argv[3])
	elif sys.argv[1] == 'remove':
		demonstration.remove_present(sys.argv[2], sys.argv[3])
	elif sys.argv[1] == 'if' and sys.argv[2] == 'delivered':
		demonstration.get_if_delivered(sys.argv[3])
	else:
		print("That command is not recognized, sorry :(")
elif len(sys.argv) is 3:
	if sys.argv[1] == 'ls' and sys.argv[2] == 'all':
		demonstration.list_children()
	elif sys.argv[1] == 'ls' and sys.argv[2] is not 'all':
		demonstration.list_presents(sys.argv[2])
	elif sys.argv[1] == 'delivered':
		demonstration.deliver_to_child(sys.argv[2])
	else:
		print("That command is not recognized, sorry :(")
elif len(sys.argv) is 2:
	if sys.argv[1] == 'ls':
		demonstration.list_all_presents()
	elif sys.argv[1] == 'help':
		print("\nkeyword: 'add' \n\n{}".format(demonstration.add_present.__doc__))
		print("\nkeyword: 'remove' \n\n{}".format(demonstration.remove_present.__doc__))
		print("\nkeyword: 'ls' + 'all' \n\n{}".format(demonstration.list_children.__doc__))
		print("\nkeyword: 'ls' + child's name \n\n{}".format(demonstration.list_presents.__doc__))
		print("\nkeyword: 'ls' \n\n{}".format(demonstration.list_all_presents.__doc__))
	else:
		print("That command is not recognized, sorry :(")
else:
	print("That command is not recognized, sorry :(")


