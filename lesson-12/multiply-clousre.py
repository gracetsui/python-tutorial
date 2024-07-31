# def sum(x : int, y:int):
#     return x + y
# print('sum(2+3) -> ', sum(2, 3))

# play with closure
def multiply(multplier: int):
    def inner(y: int):
        nonlocal multplier
        result = multplier * y
        print(f'result: {multplier} * {y} -> ', result)
        return result
    
    return inner

double = multiply(2)
print(double(5))

triple = multiply(3)
print(triple(6))


        
        