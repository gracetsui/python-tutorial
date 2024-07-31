value = 1
while value < 10: 
    print(value)
    if value == 5: # if value is 5, terminate the while loop (jump to line #7)
        break
    value += 1

print("vaule at this point: ", value)

value = 1  # reset value back to 1
while value <= 10: 
    value += 1
    print('value in the loop:', value)
    if value == 5:
        continue # jump back to line#12 (skip line#16-17)
    else:
        print("Value is now equal to " + str(value)) # no printing if value is 5

names = ["Dave", "Sara", "John"]
for x in names:
    print(x)
    
for x in "Mississippi":
    print(x)
    
for x in names:
    if x == "Sara":
        break
    print(x)
    
    for x in names:
      if x == "Sara":
        continue
      print(x)
    
for x in range(4):
    print(x)
    
for x in range(2, 4):
    print(x)
    
for x in range(0, 101, 5):
    print(x)
else:
    print("Glad that\'s over!")
    
names = ["Dave", "Sara", "John"]
actions = ["codes", "eats","sleeps"]

for name in names:
    for action in actions:
        print(name + " " + action + ".")
        
for action in actions:
    for name in names:
        print(name + " " + action + ".")
        