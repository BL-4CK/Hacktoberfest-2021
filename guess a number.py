print("----------Guess a number---------- ")
n = 18
chance = 5
while(chance <= 6):

    chance = chance - 1
    num1 = int(input("\nEnter your guess number :   "))
    if n > num1:
        print("\nYour number is less than the N")
        print("\nNumber to chances you have : {0}".format(chance))

    elif n < num1:
        print("\nYour number is greater than N")
        print("\nNumber to chances you have : {0}".format(chance))
    elif num1==18:
        print("\nSuccess")
        break
    if chance == 0:
        print("GAME OVER !")
        break
