from random import randint
""" This Module is for Exercises BANGAZON_01 - BANGAZON_05 on 
https://github.com/nashville-software-school/bangazon-llc/tree/master/orientation/exercises/bangazon

	Classes: Department, HumanResources, Sales, Administration

	Notes: Comments at bottom demonstrate instructions listed per exercise
"""

class Department:
	"""Creates the groundwork for the retrieval and setting a department's values

	Methods: add_policy, remove_policy, meet, get_budget
	"""
	def __init__(self):
		"""Initializes the Department class

		Arguments:
			n/a
		"""
		self.employees = set()
		self.name = "bob"

	@property
	def employee_count(self):
		""" Retrieves the value of employees

		Arguments:
			n/a
		"""
		try:
			return self.__employee_count
		except AttributeError:
			return ''

	@employee_count.setter
	def employee_count(self, val):
		""" Sets the value of employees

		Arguments:
			val - String
		"""
		self.__employee_count = val

	@property
	def name(self):
		""" Retrieves the value of name

		Arguments:
			n/a
		"""
		try:
			return self.__name
		except AttributeError:
			return ''

	@name.setter
	def name(self, name):
		""" Sets the value of name

		Arguments:
			name - String
		"""
		self.__name = name


	@property
	def supervisor(self):
		""" Retrieves the value of supervisor

		Arguments:
			n/a
		"""
		try:
			return self.__supervisor
		except AttributeError:
			return ""

	@supervisor.setter
	def supervisor(self, name):
		""" Sets the value of supervisor

		Arguments:
			supervisor - String
		"""
		self.__supervisor = name

	def add_policy(self, policy_name, policy_text):
		"""Adds a policy, as a tuple, to the dict of polices, values are policy names

		Arguments:
			policy_name - String
			policy_text - String
		"""
		self.policies[policy_name] = policy_text


	def remove_policy(self, policy_name):
		"""Removes a policy from the dictionary of policies

		Arguments:
			policy_name - String
		"""
		try: 
			del self.policies[policy_name]
		except KeyError:
			pass

	def meet(self):
		""" Shows the meeting point of the department

		Arguments:
			n/a
		"""
		return "Employees will meet in the Hackery at 12PM."

	def get_budget(self, budget=1000):
		""" Retrieves the budget for the department if exists, if not budget will default to 1000

		Arguments:
			budget - integer (optional)
		"""
		try:
			return self.budget
		except AttributeError:
			self.budget = budget
			return self.budget

	def add_employee(self, employee):
		""" Adds an employee to the department

		Arguments:
			employee - instance of class Employee
		"""
		self.employees.add(employee)

	def get_employees(self):
		""" returns a set of employees that have been added to the department

		Arguments:
			n/a
		"""
		print("\n----------Department {}'s Employees----------".format(self.name))
		for each in self.employees:
			print("\n{} {}'s information:".format(each.first_name, each.last_name))
			for key,value in each.__dict__.items():
				if '__' in key:
					key = key.split('__')[1]
				print("  {} has a value of {}".format(key.replace("_"," "), value))
		return self.employees

	def remove_employee(self, employee):
		""" removes an employee from the employees set

		Arguments:
			employee - instance of class employee
		"""
		self.employees.remove(employee)


class HumanResources(Department):
	"""Class for representing Human Resources department

	Methods: __init__, meet, get_budget
	"""

	def __init__(self, name, supervisor, employee_count):
		"""Initializes HumanResources Class

		Arguments:
			name - String
			supervisor - String
			employee_count - Integer
		"""
		super().__init__()
		self.policies = dict()
		self.name = name
		self.supervisor = supervisor
		self.employee_count = employee_count

	def meet(self):
		""" Shows the meeting point of the department

		Arguments:
			n/a
		"""
		return "Employees will meet in the Smoke Pit at 3PM."

	def get_budget(self):
		""" Retrieves the budget for the department Plus 500

		Arguments:
			n/a
		"""
		self.budget = super().get_budget() + 500
		return self.budget


class Sales(Department):
	"""Class for representing Sales department

	Methods: __init__, meet, get_budget
	"""

	def __init__(self, name, supervisor, employee_count):
		"""Initializes Sales Class

		Arguments:
			name - String
			supervisor - String
			employee_count - Integer
		"""
		super().__init__()
		self.policies = dict()
		self.name = name
		self.supervisor = supervisor
		self.employee_count = employee_count

	def meet(self):
		""" Shows the meeting point of the department

		Arguments:
			n/a
		"""
		return "Employees will meet in Classroom 1 at 8AM."

	def get_budget(self):
		""" Retrieves the budget for the department Plus 1000

		Arguments:
			n/a
		"""
		self.budget = super().get_budget() + 1000
		return self.budget

class Administration(Department):
	"""Class for representing Administration department

	Methods: __init__, meet, get_budget
	"""

	def __init__(self, name, supervisor, employee_count):
		"""Initializes Administration Class

		Arguments:
			name - String
			supervisor - String
			employee_count - Integer
		"""
		super().__init__()
		self.policies = dict()
		self.name = name
		self.supervisor = supervisor
		self.employee_count = employee_count

	def meet(self):
		""" Shows the meeting point of the department

		Arguments:
			n/a
		"""
		return "Employees will meet in the Parking Lot at 11AM."

	def get_budget(self):
		""" Retrieves the budget for the department Plus 1500

		Arguments:
			n/a
		"""
		self.budget = super().get_budget() + 1500
		return self.budget

class Employee:
	"""Class for representing each employee

	Methods: __init__, eat
	"""
	def __init__(self, first_name, last_name):
		"""Initializes Employee Class

		Arguments:
			first_name - String
			last_name - String
		"""
		self.first_name = first_name
		self.last_name = last_name

	def eat(self, food=None, companions=None):
		""" Allows each employee to view where, and what they've eaten

		Arguments:
			food - String (optional)
			companions - list (optional)
		"""
		self.places_to_eat = ["Burger King", "Arby's", "Paneara Bread", "Noshville"]
		random_number = randint(0, 3)
		random_place_to_eat = self.places_to_eat[random_number]


		if companions is not None:
			list_of_strings = list()
			for each in companions:
				list_of_strings.append(each.first_name)
			combined_string = ', '.join(list_of_strings)
			if food is not None:
				print("\n{} {} ordered {} and {} all ate at {}".format(self.first_name, self.last_name, food, combined_string, random_place_to_eat))
			else:
				print("\n{} {} and {} all ate at {}".format(self.first_name, self.last_name, combined_string, random_place_to_eat))
			return random_place_to_eat
		else:
			if food is not None:
				print("\n{} {} ate {} at the office.".format(self.first_name, self.last_name, food))
			else:
				print("\n{} {} ate at {}.".format(self.first_name, self.last_name, random_place_to_eat))
			return random_place_to_eat

		
class FullTime:
	"""Class for representing full-time employee

	Methods: __init__
	"""
	def __init__(self):
		""" Initializes the full-time class, sets the hours per week to 40

		Arguments:
			n/a
		"""
		self.hours_per_week = 40

class PartTime:
	"""Class for representing part-time

	Methods: __init__
	"""
	def __init__(self, days_off):
		""" Initializes the part-time class, sets the hours per week to 24

		Arguments:
			n/a
		"""
		self.hours_per_week = 24
		self.days_off = days_off

	@property
	def days_off(self):
		return self.__days_off

	@days_off.setter
	def days_off(self, days_off):
		try:
			days_off = ', '.join(days_off)
			self.__days_off = days_off
		except AttributeError:
			self.__days_off = days_off

class AccessCard:
	"""Class for representing access card authorization

	Methods: __init__
	"""
	def __init__(self, check_in=True):
		""" Initializes the access card class, sets the access card to true

		Arguments:
			check_in - Boolean (True, False)
		"""
		self.access_card = True
		self.check_in_with_security = check_in

class HRPersonnel(Employee, FullTime):
	"""Class for representing HR personel

	Methods: __init__
	"""
	def __init__(self, first_name, last_name):
		""" Initializes the HRPersonel class, setting the intial values

		Arguments:
			first_name - string
			last_name - string
		"""
		super().__init__(first_name, last_name)
		AccessCard.__init__(self, False)
		FullTime.__init__(self)

class AdminPersonnel(Employee, PartTime):
	"""Class for representing Admin personel

	Methods: __init__
	"""
	def __init__(self, first_name, last_name, days_off):
		""" Initializes the HRPersonel class, setting the intial values

		Arguments:
			first_name - string
			last_name - string
			days_off - list of strings
		"""
		super().__init__(first_name, last_name)
		AccessCard.__init__(self, True)
		PartTime.__init__(self, days_off)


"""BANGAZON_01 Exercise"""
# 1. Create three more classes for departments of your choosing.
# 2. Create some instances of each department.
# 3. Assign values to the properties of each.
Example_Department = Department()
HR = HumanResources("Human Resources", "Jeremy", 2)
Sales = Sales("Sales", "Adam", 2)
Admin = Administration("Administration", "Angela", 4)

# 4. Use print() to output the name of each of your department instances.
print("\n------Exercise 01------")
print(" HR's Department name: {}\n".format(HR.name), "Sales's Department name: {}\n".format(Sales.name), "Adminstration's Department name: {}\n".format(Admin.name))

"""BANGAZON_02 Exercise"""
"""
 1. Choose one of the general methods that you created in the Department class 
	for overriding. For example, the meet() method which handles the 
	logic of how teammates in that department gather for a meeting.
 2. Override that method in all of your derived classes, giving each a more 
 	specialized implementation. For example, you could output a different 
 	meeting place for each department.
"""
print("\n------Exercise 02------")
print("Origial Meeting: \n", Example_Department.meet())
print("\nHR Meeting: \n", HR.meet())

"""
1. Now make a method on Department named get_budget(). 
	It will set, and return, the base budget that each department 
	gets each year. You pick what that number is.
2. Override that method in each of the derived classes.
3. Make sure you invoke the parent class' overridden method with the super 
	keyword (e.g. super().get_budget()). That will set the base budget.
4. Now add, or subtract, from that base budget inside the derived class' 
	override method to adjust that specific department's budget.
"""
print("\n Default Budget: {}\n".format(Example_Department.get_budget()), "HR's Budget: {}".format(HR.get_budget()))

"""BANGAZON_03 Exercise"""
"""
1. Create a new class to represent an Employee.
2. It's constructor should accept two parameters.
		First name of employee
		Last name of employee
3. Define a method named eat() that will allow it to be invoked with the following four signatures.
		i. eat() - Will select a random restaurant name from a list of strings, print to console that the employee at at that restaurant, and also return the restaurant.
		ii. eat(food="sandwich") - Will output that the employee ate that specific food at the office.
		iii. eat(companions=[Sam, Dean, Alice]) - Will select a random restaurant name from a list of strings, print to console that the employee at that restaurant, and also output the first name of each employee in the specified list.
		iv. eat("pizza", [Sam, Dean, Alice]) - Will select a random restaurant name from a list of strings, print to console that the employee at that restaurant, and ordered the specified food, with the first name of the teammates specified in the list.

"""
# Instructions 1-2
Adam = Employee('Adam', 'Myers')
Harper = Employee('Harper', 'bangazon')
Angela = Employee('Angela', 'Thumbs Down')
Steve = Employee('Steve', 'Brownlee')

# Instructions 3. i
print("\n------Exercise 03------")

Adam.eat()

#Instructions 3. ii
Adam.eat(food="Pizza")

#Instructions 3.iii
Adam.eat(companions=[Harper, Angela, Steve])

#Instructions 3. iv
Adam.eat("Pizza", [Harper, Angela, Steve])


"""BANGAZON_04 Exercise"""
"""
1. Consider separating the location of a department from its inherent properties. 
	Perhaps one location needs an access card, while others don't. 
	One may require people to check in with security and others don't.
2. Consider the possibility that some Employees may have a physical handicap 
	that changes their working conditions. Some handicaps are temporary, 
	and others may be added after the Employees is hired. You don't want 
	those reflected in the base Employee inheritance chain, but in a 
	separate chain altogether.
"""
HR_Adam = HRPersonnel("Adam", "Myers")
HR_Harper = HRPersonnel("Harper", "Potato")
HR_Angela = HRPersonnel("Angela", "Sandwhich")


Admin_Potato = AdminPersonnel("Potato", "Salad", ["Wednesday", "Sunday"])
Admin_Bobby = AdminPersonnel("Bobby", "Eugene", ["Thursday", "Monday"])
Admin_Jeffy = AdminPersonnel("Jeffy", "Eugene", ["Tuesday", "Saturday"])

print("\n------Exercise 04------\n")
print("Its {} that {} has a Access Card and works {} hours a week\n".format(HR_Adam.access_card, HR_Adam.first_name, HR_Adam.hours_per_week))

"""BANGAZON_05 Exercise"""
"""
1. add_employee(self, employee) - Add an employee to the set. 
	The employee parameter accepts an existing instance of an employee.
2. remove_employee(self, employee) - Removes an employee from the set. 
	The employee parameter accepts an existing instance of an employee.
3. get_employees(self) - Returns the set of employees.
"""
print("\n------Exercise 05------")

HR.add_employee(HR_Adam)
HR.add_employee(HR_Harper)
HR.add_employee(HR_Angela)
Admin.add_employee(Admin_Potato)
Admin.add_employee(Admin_Bobby)
Admin.add_employee(Admin_Jeffy)

HR.get_employees()
Admin.get_employees()


# for each in dir(employee):
# 	if not each.startswith('__'):
# 		print("Employee's {} is {}".format(each, employee[each])




