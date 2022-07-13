#Calculator

print("Welcome to Calculator")
print()
print("Please press 'Enter Key'")
print()

import math
print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("8.Exit")

output_list=[]
        
print()

def Add(number1,number2):
    return number1+number2

def Subtract(number1,number2):
    return number1-number2

def Multiply(number1, number2):
    return number1*number2

def Divide(number1,number2):
    return number1/number2

choice= -1
while (choice!=0):
    choice = int(input("Enter your choice:"))
    if (choice == 1):
        print()
        print("Your choice is Addition")
        print()
        number1 = float(int(input("Enter your first number:")))
        number2 = float(int(input("Enter your second number:")))
        print()
        output1 = Add(number1,number2)
        print(number1, "+" ,number2, "=", (output1))
        print()
        
        

        
    elif (choice == 2):
        print()
        print("Your choice is Subtraction")
        print()
        number1 = float(int(input("Enter your first number:")))
        number2 = float(int(input("Enter your second number:")))
        print()
        output2 =Subtract(number1,number2)
        print(number1, "-", number2, "=", (output2))
        print()
        
        
        
    elif (choice ==3):
        print()
        print("Your choice is Multiply")
        print()
        number1 = float(int(input("Enter your first number:")))
        number2 = float(int(input("Enter your second number:")))
        print()
        output3 = Multiply(number1,number2)
        print(number1, "*", number2, "=", (output3))
        print()
                

  
    elif (choice == 4):
        print()
        print("Your choice is Divide")
        print()
        number1 = float(int(input("Enter your first number:")))
        number2 = float(int(input("Enter your second number:")))
        print()
        output4 = Divide(number1,number2)
        print(number1, "/", number2, "=", (output4))
        print()
        
      


    elif (choice==7):
           for i in range (1):
            output_list.append(i)
            print(number1, "+" ,number2, "=", (output1))
            print()

            output_list.append(i)
            print(number1, "-", number2, "=", (output2))
            print()

            output_list.append(i)
            print(number1, "*", number2, "=", (output3))
            print()

            output_list.append(i)
            print(number1, "/", number2, "=", (output4))
            print()

    elif (choice==8):
      print()
      print("Thank you for playing!")
      break

    else:
      print("Please Re-Enter your choice")
