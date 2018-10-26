num1= int(input("Enter The Number1: "))
num2= int(input("Enter The Number2: "))
num3= int(input("Enter The Number3: "))

if (num1>num2) & (num1>num3):
    print ("The Number1 is Greater",num1)
elif (num2>num1) & (num2>num3):
    print ("The Number2 is Greater",num2)
else:
    print ("The Number3 is Greater",num3)
