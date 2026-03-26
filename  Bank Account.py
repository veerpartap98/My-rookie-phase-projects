import csv 
import os 
import datetime as d

heading = 'BANK ACCOUNT'
def design(): 
    print(f'{'='*35}\n{heading.center(25)}\n{'='*35}')
    
def opening_bank_account():
    try:
        name= input('Enter your name : ').strip().lower()
        father_name = input('Enter your father name : ').strip().lower()
        phone_number = input('Enter your phone number : ').strip().lower()
        dob = input('Enter your date of birth (YYY-MM-DD) : ')
        fiel =f'{name} S-o {father_name}.csv'
        DOB = d.date.fromisoformat(dob)
        today = d.date.today()
        age = today.year - DOB.year - ((today.month, today.day) < (DOB.month, DOB.day))
        if age<18:
            print('Sorry you are underage for opening a bank account')
            return
        
        with open(fiel,'w', newline='') as f :
            field_names = ['Name','Phone Number','DOB','Balance','Date','Time']
            account = csv.DictWriter(f,fieldnames=field_names)
            account.writeheader()
            account.writerow({
                'Name' : name,
                'Phone Number' : phone_number,
                'DOB' : dob,
                'Balance' : 0,
                'Date' : d.date.today()
            })
            
        print(f'{name} your account is opened in our bank')
        
    except Exception as e :
        print(f'Something went wrong {e}')
        

def deposit():
    try:
        name = input('Enter your name : ').strip().lower()
        father_name = input('Enter your father name : ').strip().lower()
        amount = int(input('Enter the amount you want to deposit : ')) 
        
        fiel_name= f'{name} S-o {father_name}.csv'
        if not os.path.exists(fiel_name):
            print('You dont have an account')
            return
        
        with open(f'{name} S-o {father_name}.csv','r') as f :
            account = csv.DictReader(f)
            reader = list(account)
            balnce = 0
            for row in reader:
                balnce = int(row['Balance']) + amount
                        
        with open(f'{name} S-o {father_name}.csv','a') as f :
            field_names = ['Name','Phone Number','DOB','Balance','Date','Time']
            account2 = csv.DictWriter(f,fieldnames=field_names)
            account2.writerow({
                'Name' : name,
                'Phone Number' : 'xxxx',
                'DOB' : 'YYYY-MM-DD',
                'Balance' : balnce,
                'Date' : d.date.today() 
            })
            
            print(f'{name}, your transaction is completed successfully!')
            print(f'Amount deposited: {amount}')
            
    except Exception as e :
        print(f'Something went wrong {e}')
            
def sending_money():
    try :
        name = input('Enter your name : ').strip().lower()
        father_name = input('Enter your father name : ').strip().lower()
        amount = int(input('Enter the amount you want to send : ')) 
        reciver_name = input('Enter money reciver name : ').strip().lower()
        reciver_father_name = input('Enter money reciver father name : ').strip().lower()
        
        fiel_name= f'{name} S-o {father_name}.csv'
        fiel_name2 = f'{reciver_name} S-o {reciver_father_name}.csv'
        if not os.path.exists(fiel_name):
            print('You do not have an account')
            return
        if not os.path.exists(fiel_name2):
            print('Reciver do not have an account')
            return
        
        with open(fiel_name,'r') as f :
            account = csv.DictReader(f)
            reader = list(account)
            balance = 0
            for row in reader:
                balance = int(row['Balance']) - amount
                
        with open(fiel_name2,'r') as f :
            account2 = csv.DictReader(f)
            reader = list(account2)
            balnce = 0
            for row in reader:
                balnce = int(row['Balance']) + amount
                
        with open(fiel_name,'a') as f :
            field_names = ['Name','Phone Number','DOB','Balance','Date','Time']
            account3 = csv.DictWriter(f,fieldnames=field_names)
            account3.writerow({
                'Name' : name,
                'Phone Number' : 'xxxx',
                'DOB' : 'YYYY-MM-DD',
                'Balance' : balance,
                'Date' : d.date.today(),
                'Time' : d.datetime.now()
            })
            
        with open(fiel_name2,'a') as f :
                field_names = ['Name','Phone Number','DOB','Balance','Date','Time']
                account4 = csv.DictWriter(f,fieldnames=field_names)
                account4.writerow({
                    'Name' : name,
                    'Phone Number' : 'xxxx',
                    'DOB' : 'YYYY-MM-DD',
                    'Balance' : balnce,
                    'Date' : d.date.today(),
                    'Time' : d.time.now()
                })
        
        print(f'{name}, your transaction is completed successfully!')
    except Exception as e :
        print(f'Something went wrong {e}')
        
        
def main():
    design()
    print('WElCOME TO OUR BANK, HOW WE CAN HELP YOU?\n1: Open an account \n2: Deposit money \n3: Send money ')
    print()
    purpose = input('Enter the number of the service you wana procced with : ').strip()
    
    if purpose == '1':
        opening_bank_account()
    if purpose =='2':
        deposit()
    if purpose== '3':
        sending_money()
    if purpose == '':
        print('Select a service number')
        
main()