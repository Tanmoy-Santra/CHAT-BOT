import numpy as np 
import pandas as pd
import os
file_path = 'try2024salary.csv'
def show_table():    
    df = pd.read_csv(file_path)
    print('-------------------------------DATA TABLE 2024--------------------------')
    print()
    print()
    print(df)
    print()
    print()
def add_payment():
    df = pd.read_csv(file_path, index_col='name')
    df=df.fillna(0)
    print('ENTER THE STUDENT NAME : ')
    STUDENT_ID =str(input())
    print('ENTER THE MONTH:')
    MONTH = str(input())
    print('ENTER THE STATEMENT WITH DATE : ')
    STATEMENT = str(input())
    df.loc[STUDENT_ID, MONTH] = STATEMENT
    df.to_csv(file_path) 
    print()
    print("Payment added successfully......")
    print('---------------------------------------------------------------------')
def check_payment():
    df = pd.read_csv(file_path,index_col='name')
    df=df.fillna(0)
    print('ENTER STUDENT NAME : ')
    STUDENT_ID=str(input())
    fdf=df.loc[[STUDENT_ID],:]
    print(fdf)
    df.to_csv(file_path) 
    print()    
    print('---------------------------------------------------------------------')    
def remove_data():
    df = pd.read_csv(file_path,index_col='name')
    print('ENTER THE STUDENT NAME : ')
    STUDENT_ID =str(input())
    print('ENTER THE MONTH:')
    MONTH = str(input())
    df.at[STUDENT_ID, MONTH] = pd.NA
    df=df.fillna(0)
    df.to_csv(file_path) 
    print()
    print('data removed successfully......')
    print('---------------------------------------------------------------------')
   


