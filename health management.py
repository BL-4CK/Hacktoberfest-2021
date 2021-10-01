def whole_program():
    print("""
    ----------choice----------
    press 1 for shambo
    press 2 for alan 
    press 3 for alexa
    """)
    name = int(input("Enter your choice :  "))

    #=========choice between input or retrieve===========

    print("\npress 1 for input "
          "press 2 for retrieve ")
    choice = int(input("\nEnter your choice  :  "))

    #=========choice between meal or exercise============

    print("\npress 1 for meal "
          "press 2 for exercise")
    choice2 = int(input("\nEnter your choice :    "))

    import datetime

    time = datetime.datetime.now()

    # ======================================================
    if name == 1:
        if choice == 1:
            if choice2 == 1:
                shambo_meal = str(input("Enter your note :  "))
                a = open("Shambo_meal.txt","a")
                b = a.write("\n"+(str('['+(str(time))+']'))+" "+shambo_meal)
                print("\nNote written successfully")
                a.close()
            elif choice2 == 2:
                shambo_ex = str(input("Enter your note  :  "))
                c = open("shambo_ex.txt","a")
                d = c.write("\n"+(str('['+(str(time))+']'))+" "+shambo_ex)
                print("\nNote written successfull")
                c.close()
            else:
                print("invalid choice input")
        elif choice == 2:
            if choice2 == 1:
                num1 = open("Shambo_meal.txt")
                num2 = num1.read()
                print(num2)
                num1.close()
                again()
            elif choice2 == 2:
                num3 = open("shambo_ex.txt")
                num4 = num3.read()
                print(num4)
                num3.close()
                again()
            else:
                print("invalid choice input")
        else:
            print("Invalid choice input")
    elif name == 2:
        if choice == 1:
            if choice2 == 1:
                alan_meal = str(input("Enter your note :  "))
                e = open("alan_meal.txt", "a")
                f = e.write("\n"+(str('['+(str(time))+']'))+" "+alan_meal)
                print("\nNote written successfully")
                e.close()
            elif choice2 == 2:
                alan_ex = str(input("Enter your note  :  "))
                g = open("alan_ex.txt","a")
                h = g.write("\n"+(str('['+(str(time))+']'))+" "+alan_ex)
                print("\nNote written successfull")
                g.close()
            else:
                print("Invalid choice input")
        elif choice == 2:
            if choice2 == 1:
                i = open("alan_meal.txt")
                j = i.read()
                print(j)
                i.close()
                again()
            elif choice2 == 2:
                k = open("alan_ex.txt")
                l = k.read()
                print(l)
                k.close()
                again()
            else:
                print("Invalid choice input")
        else:
            print("invalid choice input")
    elif name == 3:
        if choice==1:
            if choice2 == 1:
                alexa_meal = str(input("Enter your note :  "))
                m = open("alexa_meal.txt","a")
                n = m.write("\n"+(str('['+(str(time))+']'))+" "+alexa_meal)
                print("\nNote written successfully")
                m.close()
            elif choice2 == 2:
                alexa_ex = str(input("Enter your note  :  "))
                o = open("alexa_ex.txt","a")
                p = o.write("\n"+(str('['+(str(time))+']'))+" "+alexa_ex)
                print("\nNote written successfull")
                o.close()
            else:
                print("Invalid choice input")
        elif choice == 2:
            if choice2 == 1:
                q = open("alexa_meal.txt")
                r = q.read()
                print(r)
                q.close()
                again()
            elif choice2 == 2:
                s = open("alexa_ex.txt")
                t = s.read()
                print(t)
                s.close()
                again()
            else:
                print("Invalid choice input")

        else:
            print("Invalid choice input")
    else:
        print("invalid choice input")
    again()

def again():
    run = input("Do you want to again run the program : [Y/N] : ")
    if run == 'y':
        whole_program()
    elif run == 'n':
        print("See you again later ")
    else:
        again()

whole_program()
