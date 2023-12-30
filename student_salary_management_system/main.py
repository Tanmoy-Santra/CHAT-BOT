import numpy as np
import pandas as pd 
from password import login
from system import*
while(1):
    input_username = input("ENTER USERNAME: ")
    input_password = input("ENTER PASSWORD: ")
    if login(input_username, input_password):
         print("Login successful!")
         for i in range(0,200):
             print(' ')
         break
    else:
         print("INVALID USERNAME OR PASSWORD.....!!")
    
print('==========================SALAY RECORD OF 2024==============================')
print()
print('----------------------------------------------------------------------------')
print()
while(1):    
    print('1.SHOW TABLE')
    print('2.ADD PAYMENT')
    print('3.CHECK PAYMENT')
    print('4.REMOVE DATA')
    print('5.EXIT')
    print('CHOOSE YOUR OPTION :')
    ch=int(input())
    if ch==1:
        show_table()
    elif ch==2:
        add_payment()
    elif ch==3:
        check_payment()
    elif ch==4:
        remove_data()
    else:
        exit()




