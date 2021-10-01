def calculator():
    print("---------------CALCULATOR---------------")
    a = int(input("Enter 1st number : "))
    b = int(input("Enter 2nd number : "))

    print("""
-----------------CHOICES---------------
    press 1 to ADD
    press 2 to SUBSTRACT
    press 3 to MULTIPLY
    press 4 to DIVIDE
    
    """)
    print("=======================================")
    c = int(input("Enter Your choice :  "))
    print("\n")
    if c==1:
        sum = (a+b)
        print("Result : "+"{0} + {1} = {2}".format(a,b,sum))
    elif c==2:

        res = (int(a) - int(b))
        print("Result : "+"{0} - {1} = {2}".format(a,b,res))

    elif c==3:

        print("Result : "+"{0} * {1} = {2}".format(a,b,a*b))
    elif c==4:
        print("Result : "+"{0} / {1} = {2}".format(a,b,a/b))
    else:
        print("Invalid choice input")

    again()

def again():
    cal_again = input("\nDo you want to calculate again? [Y/N]  : ")

    if cal_again == 'y':
        calculator()
    elif cal_again == 'n':
        print("See You Later")
    else:
        again()


calculator()
