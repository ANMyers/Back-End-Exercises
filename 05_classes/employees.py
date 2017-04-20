
class Employee():

    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date

    def get_name(self):
        return self.name

    def get_title(self):
    	return self.title

    def get_date(self):
    	return self.start_date

    def get_info(self):
    	print("\n-----{}-----".format(self.name))
    	print("This {} started on {}".format(self.title, self.start_date))


class Company():

    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date
        self.employees = set()

    def get_name(self):        
        return self.name

    def add_employee(self, employee):
    	self.employees.add(employee)

    def remove_employee(self, employee):
    	self.employees.discard(employee)

    def list_employees(self):
    	print("\n-----------{}---------".format(self.name))
    	for each in self.employees:
    		print("{} works as {} beginning on {}".format(each.name, each.title, each.start_date))

    def test_run(self):
    	return self.employees


new_company = Company("TinkerBoodle", "Tinker Experts", "Yesterday")

adam = Employee("Adam", "Master of everything", "Beginning of time")
jeremy = Employee("Jeremy", "Python of life", "Before Dirt")
nick = Employee("Nick", "Hero of the Python", "After Dirt")

new_company.add_employee(adam)
new_company.add_employee(jeremy)
new_company.add_employee(nick)


new_company.list_employees()

for each in new_company.employees:
	each.get_info()









