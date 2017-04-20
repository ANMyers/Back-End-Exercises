songs = {
    ('Nickelback', 'How You Remind Me'), 
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals')
} # 1. Define a set that contains tuples. Each tuple should contain two strings:

songs_not_nickelback = set()
 # 2. Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.
for each in songs:
	if 'Nickelback' not in each:
		songs_not_nickelback.add(each)

print("\n----Not Nickelback Songs----\n")
for each in songs_not_nickelback:
	print("Artist: {} \nSong: {}\n".format(each[0], each[1]))