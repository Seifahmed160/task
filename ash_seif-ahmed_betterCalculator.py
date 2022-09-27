import math

num1= input("Enter The First Number: ")
num2= input("Enter The Second Number: ")
op= input("Enter The Operator: ")

sum= float(num1)+float(num2)
sub= float(num1)-float(num2)
mul= float(num1)*float(num2)
div= float(num1)/float(num2)
mod= float(num1)%float(num2)

if op == "+":
    print("sum ="+str(sum))
elif op == "-":
    print("sub = "+str(sub))
elif op == "*":
    print("mul = "+str(mul))
elif op == "/":
    print("div = "+str(div))
elif op == "%":
    print("mod = "+str(mod))
else:
    print("Invalid Operator")

key=input("Do you Wanna Calculate Factorial of number (Y/N): ")
if key == "Y":
    num= int(input("Enter The Number To Calculate its Factorial: "))
    fac=math.factorial(num)
    print("Factorial= {}".format(fac))
else:
    print("GoodBye")