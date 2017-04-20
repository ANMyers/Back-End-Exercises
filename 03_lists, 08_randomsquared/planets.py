import random # Importing random to allow for random generation of numbers for satelites on line 22

# Exercise
#-------------------

planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter") # 1. Use append() to add Jupiter and Saturn at the end of the list.
planet_list.append("Saturn")

planet_list.extend(["Uranus", "Neptune"]) # 2. Use the extend() method to add another list of the last two planets in our solar system to the end of the list.

planet_list.insert(2, "Earth") # 3. Use insert() to add Earth, and Venus in the correct order.
planet_list.insert(0, "Venus") # 3. Use insert() to add Earth, and Venus in the correct order.

planet_list.append("Pluto") # 4. Use append() again to add Pluto to the end of the list.

rocky_planets = planet_list[0:4] # 5. Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.

del planet_list[len(planet_list) - 1] # 6. Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.

# Iterating Over Planets

list_of_tuples = list() # 1. Create another list containing tuples. Each tuple will hold the name of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on. (e.g. ('Cassini', 'Saturn')).

for each in planet_list:
	tuple_list = ('Sat{}{}{}'.format(random.randint(0,9), random.randint(0,9), random.randint(0,9)), each, 'Dummy Planet')
	list_of_tuples.append(tuple_list)

for planet in planet_list: # 2. Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which sattelites have visited.
	for tuple_itself in list_of_tuples:
		if planet in tuple_itself:
			print("---------{}---------".format(planet))
			print("  {} has visited.".format(tuple_itself[0]))
			print("\n")



print("Whole Planet List: {}".format(planet_list))
print("Rocky Planet List: {}".format(rocky_planets))
print(list_of_tuples)
