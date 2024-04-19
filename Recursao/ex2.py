def recursiveMethod(n):
    if n<1:
        print("i is less than 1")
    else: 
        print(n)
        recursiveMethod(n-1)
        
recursiveMethod(4)