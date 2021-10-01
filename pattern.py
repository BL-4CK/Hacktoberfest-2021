# DEVELOPER --- SHAMBO CHOWDHURY
# this program is made to print 2 types of pyramid pattern based on user's input
def pattern():
    num = int(input("Enter the number of rows :  "))

    type = int(input("""
    ------Choices------
    press 1 for type 0
    press 2 for type 1 
    """))
    if type == 1:
        for i in range (0,num):
            for j in range (0,i+1):
                print("*", end=" ")
            print()
        print("\n")
    elif type == 2:
        for c in range (num,0,-1):
            for x in range(0, c):
                print("*", end=' ')
            print()
    else:
        print("Invalid choice input !!")
        pattern()
    def again():
        a = input("Do you want to run again the program [Y/N]  :  ")
        if a == 'y':
            pattern()
        elif a== 'n':
            print("See you next time")

        else:
            again()
    again()
pattern()