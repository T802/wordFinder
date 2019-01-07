from itertools import chain
from glob import glob 

#reference to full dictionary 
NAME = 'resources/allWords.txt'

print("Opening: " + NAME)

# open dictionary file 
file = open(NAME, 'r')

#read each line as lowercase
lines = [line.lower() for line in file]

# sort and remove duplicate, rewrite to file 
with open(NAME, 'w') as out:
    print("-Writing Lines-")
    out.writelines(sorted(set(lines)))

# close dictionary file 
print("Closing: " + NAME)
file.close()
