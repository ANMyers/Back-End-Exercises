my_family = {
    'sister': {
        'name': 'Krista',
        'age': 42
    },
    'mother': {
        'name': 'Cathie',
        'age': 70
    }
} # 1. Define a dictionary that contains information about several members of your family. Use the following example as a template.

for key, value in my_family.items():
	print("{} is my {} and is {} years old.".format(value['name'], key, value['age']))
# 2. Using a dictionary comprehension, produce output that looks like the following example.