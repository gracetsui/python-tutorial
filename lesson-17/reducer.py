from functools import reduce

numbers = [10,2,5]

total = reduce(lambda acc, curr: acc + curr, numbers, 0)
print('Total: ', total)


minimum = reduce(lambda min, curr: curr if curr < min else min, numbers, 999)
print('min: ', minimum)
