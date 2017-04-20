#Instructions
#-------------------------
showroom = set() # 1. Create an empty set name "showroom"

showroom.add("Mustang")
showroom.add("Tiburon")
showroom.add("Sonata")
showroom.add("Derp") # 2. Add four of your favorite car model names to the set

print(len(showroom)) # 3. Print the length of your set

showroom.add("Sonata") # Pick one of your items in your show room and add it to the set again

print(showroom) # Demonstration of a Set not allow duplicates

new_showroom = ["Hydai", "Potato", "Jeffery"]

showroom.update(new_showroom) # 6. Useing "update()", add two more car models to your showroom with another set.

print(showroom) # Demonstration of 6.

showroom.discard("Hydai") # 7. You've sold one of your cares. Remote it from the set with the "discard()" method.

print(showroom) # Demonstration of 7.

# Acquiring more cars
junkyard = set() # 1. Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set

junkyard.add("Desk")
junkyard.add("Table")
junkyard.add("Chair")
junkyard.add("Sonata")

exists_in_both = showroom.intersection(junkyard) # 2. Use the intersection method to see which cars exist in both the showroom and that junkyard.
combined_yard = showroom.union(junkyard) # 3. Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.

print(exists_in_both) # Demonstration of 2.
print(combined_yard) # Demonstration of 3.

