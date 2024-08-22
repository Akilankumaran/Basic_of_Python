def add():
   a =(int(input("Enter a value :")))
   b =(int(input("Enter b value : ")))
   return (a + b)
result = add()
print("The Sum is :", result)


def findevenorodd():
    num = int(input("Enter a number :"))
    if (num%2== 0):
        result = "Even"
    else:
       result = "Odd"
    return result
result = findevenorodd()
print("The entered number is :",result)

def rangeoffunction():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    for i in range(a,b):
        print(i)
    return i 
result = rangeoffunction()
print("The range from a to b:", result)



# learning how to commit(git) when the code is modified.