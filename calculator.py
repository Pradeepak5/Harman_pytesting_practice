def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

if __name__=="__main__":
    a = int(input("Enter num 1 :"))
    b = int(input("Enter num 2 :"))

    addition = add(a, b)
    print(addition)
    subtraction = sub(a, b)
    print(subtraction)
    multiplication = mul(a, b)
    print(multiplication)
    division = div(a, b)
    print(division)