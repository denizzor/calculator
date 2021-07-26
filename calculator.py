print("Calculator with python")
print ("Select the specified number for the operation.","\n1-Addition","\n2-Extraction Process","\n3-Multiplication","\n4-Division")

chose= input("Select the operation (1-2-3-4):")

number1=int(input("Number 1:"))
number2=int(input("Number 2:"))

if chose =="1":
   print(number1,"+",number2,"=",number1+number2)
elif chose =="2":
    print(number1,"-",number2,"=",number1-number2)
elif chose =="3":
    print(number1,"x",number2,"=",number1*number2)
elif chose =="4":
    print(number1,"//",number2,"=",number1/number2)
else:
    print ("Incorrect operation.")





