users = ['A','B','C']

data = ['A', 30, True]

emptylist = []

print("A" in emptylist)

print('#1: ', users[0]) # get the first element from list 
print('#2', users[-1]) # get the last element from list

print('#3', users.index('C'))  # add '#3' to help you identify the print() messages

print('#4', users[0:2])
print('#5', users[1:])
print('#6', users[-3:-1])

print('#7', len(data))

users.append("D")
print('#8', users)

users += ['E']
print('#9',users)

users.extend(['F', 'G'])
print('#10', users)

users.extend(data)
print('#11', users)

users.insert(0, 'H')
print('#12',users)

users[2:2] = ['I', 'J']
print('#13', users)

users[1:3] = ['D', 'L']
print('#14', users)

users.remove('G')
print('#15', users)

print('first pop-out value: ', users.pop())
print('second pop-out value: ',users.pop())
print('#16', users)

del users[0]
print('#17 ', users)

#del data
data.clear()
print('#18', data)

users[1:2] = ['a']
users.sort()
print('#19', users)

users.sort(key=str.lower)
print('#20', users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print('#21', nums)

nums.sort(reverse=True)
print('#22', nums)

print('#23', sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
print(mycopy.sort())
print(nums)

print(type(nums))

mylist = list([1, "X", True])
print(mylist)

# Tuples

mytuple = tuple(('N', 42,True))

anothertuple = (1,4,2,8,2,2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('X')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))