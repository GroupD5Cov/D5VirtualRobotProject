# Read in a file from disk and put it in an array.
file = open("car.txt")
 
name_list = []
for line in file:
    line = line.strip()
    name_list.append(line)
 
file.close()

# --- Linear search
key = "land rover new petrol"
 
i = 0
while i < len(name_list) and name_list[i] != key:
    i += 1
 
if i < len(name_list):
    print( "The car is at position", i)
else:
    print( "The name was not in the list." )
