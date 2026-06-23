#Python_projectclear
def add():
    a=int(input("\nPlease enter the first number :"))
    b=int(input("Please enter the second number :"))
    c=a+b
    print("\nAddition of the numbers :",c)

def sub():
    a=int(input("\nPlease enter the first number :"))
    b=int(input("Please enter the second number :"))
    c=a-b
    print("\nSubtraction of the numbers :",c)

def mul():
    a=int(input("\nPlease enter the first number :"))
    b=int(input("Please enter the second number :"))
    c=a*b
    print("\nMultiplication of the numbers :",c)

def div():
    a=int(input("\nPlease enter the first number :"))
    b=int(input("Please enter the second number :"))
    c=a//b
    print("\nDivision of the numbers :",c)

def menu():
    while(True):
        print("======================================================")
        print("............Welcome to the calculator............")
        print("======================================================\n")
        print("Type 1 for the addition of the two numbers :")
        print("Type 2 for the subtraction of the two numbers :")
        print("Type 3 for the multiplication of the two numbers :")
        print("Type 4 for the division of the two numbers :")
        k=int(input())
        print("\n----------------------------------------------------")
        if(k==1):
            add()
        elif(k==2):
            sub()
        elif(k==3):
            mul()
        elif(k==4):
            div()
        else:
            print("\n----------------------------------------------------")
            print("You've entered invalid input !")
            print("Please TRY AGAIN !")
            exit()
        print("\n----------------------------------------------------")
        print("\nType 'y' for reusing the calculator :")
        print("Type 'n' for ending the program :")
        p=input()
        if(p=='y' or p=='Y'):
            continue
        else:
            print("\n----------------------------------------------------")
            print("\nThank you so much for using our calculator !")
            print("Take care :)")

            print("\nProgram ended savely ....")
            print("\n-------------------------X---------------------------")
            exit()
menu()