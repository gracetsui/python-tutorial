from functools import reduce

# traditional function
def square(num): return num * num # use "square" as a verb
# lambda num : num * num
print('square of x:', square(2))

# lambda function
squareLambda = lambda y: y *y 
print('square of y:',  squareLambda(2))

# doubling list of numbers
numbers = [ 1,2,3,4]
def double(nums: list[int]):
    doubledNums = []
    for n in nums:
        doubledNums.append(n * 2)
        
    return doubledNums

print('doubling with traditional function: ', double([2,3,4]))
mapped = map(lambda x: x * 2, [3,4,5]) # lambda function is "pythonic" style
print('doubling with lambda function:', list(mapped) )


def addTwo(num): return num + 2
# lambda num : num + 2
print(addTwo(12))


def sum_total(a, b): return a + b
# lambda a, b : a + b


print(sum_total(10, 8))


############################

def funcBuilder(x):
    return lambda num : num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

############################

lambda num : num * num # Alex: this line create a lambda function, BUT not using it (nor assigning to any variable)

numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num : num * num, numbers)
print(list(squared_nums))

##########################

odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))

##########################


numbers = [1,2,3,4,5,1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

print(sum(numbers, 10))


names = ['Dave Gray', 'Sara Ito', 'John Jacob Jingleheimerschmidt']

char_count = reduce(lambda acc, curr : acc + len(curr), names, 0)

print(char_count)