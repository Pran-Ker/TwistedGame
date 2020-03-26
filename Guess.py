import random as rd 

ch = 'y'
amount = 100

while ch.upper()=="Y":
    
    
    print("______________________________________________________________________")
    print("                      You have {} $ to bet                   ".format(amount))
    print("_______________________________________________________________________")
    print("")
    print("")
    spend = 101
    
    while spend>amount:
        spend = int(input("How much do you want to spend?"))
    
    print(spend)
    
    inp = 100
    while inp>10 or inp<0:
        inp = int(input("Guess the number (0 to 10) :"))

    print("Number is {}".format(inp))

    x=inp

    while x==inp:
        x = rd.randint(0,10)
    
    print("Random number is {}".format(x))

    if x!=inp:
        print("Too bad, you lose the round!")
        amount-=spend
        
    
    else:
        print("Wow! You know that is impossible though")
        amount+=spend    
        
    print("Balance amount is {}".format(amount))
    
    if amount>=200:
        print("FLAG{ U_12_TH3_W11\\11\\13R_0F_TH3_G4M3 }")
        ch = "n"
    elif amount<=0:
        print("You have lost the game! That really sucks... :(")
        ch = "n"
    else:    
        ch = input("Do you want to start again?")
    
    
