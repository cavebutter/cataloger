import os

with os.scandir('/Path/to//Movies') as entries:
    movies = [entry for entry in entries]

with os.scandir('/Path/to/TV Shows') as entries:
    TV_Shows = [entry for entry in entries]
        
with os.scandir('Path/to/Other') as entries:
    other = [entry for entry in entries]

with open('/Path/to/Desktop/Media_Inventory.txt', 'w') as inventory:
    inventory.write("[Movies] \n")
    for item in movies:
        inventory.write(item + '\n')
    inventory.write("\n\n\n\n[TV Shows]\n")
    for item in TV_Shows:
        inventory.write(item + '\n')
    inventory.write("\n\n\n\n[Other]\n")
    for item in other_stuff:
        inventory.write(item + '\n')
