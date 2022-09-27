import statistics

num1= float(input("Enter The First Number: "))
num2= float(input("Enter The Second Number: "))
num3= float(input("Enter The Third Number: "))

avg= (num1+num2+num3)/3
print("The Average of The 3 Numbers is: %.2f" %avg)

numList=[num1,num2,num3]
avg_builtin= statistics.mean(numList)
print("The Average of The 3 Numbers is: %.2f" %avg_builtin)

