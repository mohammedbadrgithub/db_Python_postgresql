
import os
from functions import signup
from functions import signin

while True :
    os.system('cls')
    print ('welcome in our database')
    choice = input ('what do you want ?  \n1)press 1 to signin  \n2)press 2 signup  \n3)press 3 to exit  \n >>>>       ')
    if choice == '1' :
        signin()
    elif choice == '2':
        os.system('cls')
        print('signup')
        signup()
    elif choice == '3':
        break  
    else :
        os.system('cls') 
        print('out of options ')
        
        