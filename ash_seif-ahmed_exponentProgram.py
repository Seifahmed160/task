def exponent(base,powNum):
    result =1
    for i in range(powNum):
        result= result*base
        result = pow(base,powNum) # using built in function
    return result


base= int(input("Enter The Base Number: "))
powNum= int(input("Enter The Power: "))
result =exponent(base,powNum)
print("The Result="+ str(result))

