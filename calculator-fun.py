# Quit Function
def quit():
    print("~ Thankyou for visiting in Calculator System ~")

# Again Function
def again():
    d = int(input("Press (1) for again using calculator and Press (2) for quit : "))
    if(d==1):
        calc()
    elif(d==2):
        quit()
    else:
        print("You Enter Wrong Input !!")
        again()

# Starting Point
print("======================================\n      CALCULATOR SYSTEM\n======================================")
def calc():
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    c = int(input("Enter choice \n \n Addition(1)          Subtraction(2)         Multiplication(3)         Division(4)         ALL(5)  \n\n ----------------->  "))
    if(c==1):
        print("Addition is : ",a+b)
        again()
    elif(c==2):
        print("Subtraction is : ",a-b)
        again()
    elif(c==3):
        print("Multiplication is : ",a*b)
        again()
    elif(c==4):
        print("Division is : ",a/b)
        again()
    elif(c==5):
        print("Addition is : ",a+b)
        print("Subtraction is : ",a-b)
        print("Multiplication is : ",a*b)
        print("Division is : ",a/b)
        again()
    else:
        print("You Enter Wrong Input !!")
        again()

calc()









