import sys

mod = 321411684795998371952705913685813950403 
base = 4116689149

def menu():
    print("============ Menu ============= ")
    choice  = input ("""
                    A : Alice Stage 1
                    B : Bob 
                    C : Addtion 
                    Q : Exit
                    Please enter which modulus type you would like:
                    """)
    if choice == "A" or choice =="a":
        multiplication()
        menu()
    elif choice == "B" or choice == "b":
        power()
        menu()
    elif choice == "C" or choice == "c":
        addtion()
        menu()
    elif choice == "Q" or choice == "q":
        sys.exit
    else:
        print("You can only select items in the menu")
        print("Please try again")
        menu()


#alice's first stage of output 
def hellman(x, y, p):
    res = 1
    x = x % p
    if (x == 0):
        return 0
    while (y > 0 ):
         if ((y & 1) == 1):        
             res = (res * x) % p
         y = y >> 1
         x = (x * x) % p 

    return res

def aliceS1print():
   x = base; y = 288358649145066896504000974356927662371; p = mod
   print('Alice stage 1 =', aliceS1(x, y, p), 'mod', p) 




#bobs first stange of out put 
def bobS1(x, y, p):
    res = 1
    x = x % p
    if (x == 0):
        return 0
    while (y > 0 ):
         if ((y & 1) == 1):
             res = (res * x) % p
         y = y >> 1
         x = (x * x) % p 
    return res

def bobS1print():
    x = base; y = 266372873561836896319324784586721523627; p = mod
     
    print('Bob stage 1 =', bobS1(x, y, p), 'mod', p) 


#Alice second stage 
def aliceS2(x, y, p):
    res = 1
    x = x % p
    if (x == 0):
        return 0
    while (y > 0 ):
         if ((y & 1) == 1):
             res = (res * x) % p
         y = y >> 1
         x = (x * x) % p 

    return res

def aliceS2print():
    x = 38463287078112727244892760917610286014; y = 288358649145066896504000974356927662371; p= mod

    print('Alice Stage 2 =', aliceS2(x, y, p), 'mod', p)

#Alice second stage 
def bobS2(x, y, p):
    res = 1
    x = x % p
    if (x == 0):
        return 0
    while (y > 0 ):
         if ((y & 1) == 1):
             res = (res * x) % p
         y = y >> 1
         x = (x * x) % p 

    return res

def bobS2print():
    x = 24004202547683770419016829657526486559; y = 266372873561836896319324784586721523627; p= mod

    print('Bob Stage 2 =', bobS2(x, y, p), 'mod', p)


aliceS1print()
bobS1print()
aliceS2print()
bobS2print()
