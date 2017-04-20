zoo = ("Lion", "Tigers", "Bears", "Oh My") # 1. Create a tuple named zoo that contains your favorite animals.

print("\nzoo indexing on 'Tigers': {} \n".format(zoo.index("Tigers"))) # 2. Find one of your animals using the .index(value) method on the tuple.

for animal in zoo: # 3. Determine if an animal is in your tuple by using for value in tuple.
	if animal is "Bears":
		print("{} was found in the zoo.\n".format(animal))


(potato, tomato, gloves, desk) = zoo # 4. Create a variable for each of the animals in your tuple with this cool feature of Python.
print("Variable for each animal: {}\n".format(desk))

zoo = list(zoo) # 5. Convert your tuple into a list.

zoo.extend(["Giraffe", "Badger", "Cat"]) # 6. Use extend() to add three more animals to your zoo.

print("List: {}\n".format(zoo))

zoo = tuple(zoo) # 7. Convert the list back into a tuple.

print("Tuple list: {}\n".format(zoo))
