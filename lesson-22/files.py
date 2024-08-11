import os

# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

f = open("lesson-22/names.txt")

for line in f:
    print(line)
    
f.close()

try:
    f = open("lesson-22/names_list.txt")
except:
    print("The file you want to read doesn't exist")
finally:
    f.close()
    
f = open("lesson-22/names.txt", "a")
f.write("\nNeil")
f.close()

f = open("lesson-22/names.txt")
print(f.read())
f.close()

f = open("lesson-22/context.txt", "w")
f.write("I deleted all the context")
f.close()

f = open("lesson-22/context.txt")
print(f.read())
f.close()

f = open("lesson-22/name_list.txt", "w")
f.close()

if not os.path.exists("lesson-22/dave.txt"):
    f = open("lesson-22/dave.txt", "x")
    f.close()
    
if os.path.exists("lesson-22/dave.txt"):
    os.remove("lesson-22/dave.txt")
else:
    print("The file you wish to delete does not exist")
    
    
with open("lesson-22/more_names.txt") as f:
    content = f.read()
    
with open("lesson-22/names.txt") as f:
    f.write(content)