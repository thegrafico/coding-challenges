data = None
filename = "text.txt"

with open(filename, "r+") as f:
    data = f.read().strip().replace("\n", " ")
print(data)    
    