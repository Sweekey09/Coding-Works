#Introduction

print()
print("Welcome to My Introduction!")
print()

while 1:
    print("Get to know me! Select one choice below!")
    print()
    print("1. Name")
    print("2. Age")
    print("3. Birthday")
    print("4. Current School")
    print("5. What I want to achieve in the future")
    print("6. Hoobies")
    print("7. Exit")
    print()
  
    choice= int(input("Enter your choice: "))

    print()


    if choice== 1:
        print("------------------------------")
        print("Hello!, my name is Noor Safina")
        print("------------------------------")
        print()
    elif choice== 2:
        print("---------------------------------")
        print("I am 18 years old this year, 2022")
        print("---------------------------------")
        print()
    elif choice==3:
        print("-------------------------------------------------------------------------")
        print("My birthday is on the 9th of August 2004! I am a Nationals' Day Baby >.<!")
        print("-------------------------------------------------------------------------")
        print()
    elif choice== 4:
        print("-------------------------------------------------------------------------")
        print("I am currently studying Nitec in Security Technology at ITE College West!")
        print("-------------------------------------------------------------------------")
        print()
    elif choice== 5:
        print("----------------------------------------------------------------------------------------------------")
        print("I want to acheive my dream, working in the Security Industry and is eager to learn more everyday :>!")
        print("----------------------------------------------------------------------------------------------------")
        print()
    elif choice== 6:
        print("---------------------------------------------------------------------------------------------------------------------------------------------------")
        print("My hobbies are mainly sports such as, Badminton, Football and Running but I find Coding really interesting therefore, Coding might be my new hobby!")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------")
        print()   
    elif choice== 7:
        print("-----------------------------------------------")
        print("Thank you for your interest, have a nice day! :>")
        print("-----------------------------------------------")
        print()
        break
    else:
        print("-------------------------------")
        print("Please Re-enter your choice :<!")
        print("-------------------------------")
        print()
