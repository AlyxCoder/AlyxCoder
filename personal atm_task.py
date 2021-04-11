name = input("What is your username? \n")
allowedUsers = ['Remi','Quarshie','Yaw']
allowedPassword = ['RemI','QuarshiE','YaW']

if(name in allowedUsers):
    password = input("Your password? \n")
    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):
        print('Welcome %s' % name)


        from datetime import datetime
        now = datetime.now()
        dt_string = now.strftime('%d/%m/%Y %H:%M:%S')
        print('Date and Time:', dt_string)
        
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input('Please select an option: \n'))
    
        if(selectedOption == 1):
            print('you selected %s' % selectedOption)

            withdrawal = input('How much would you like to withdraw? \n')
            print('Take Cash')
            print('Thank you for banking with us!')
            
        elif(selectedOption == 2):
            print('you selected %s' % selectedOption)

            cashDeposit = input('How much would you like to deposit? \n')
            print('Current balance: %s' % cashDeposit)
            
        elif(selectedOption == 3):
            print('you selected %s' % selectedOption)

            complaint = input('What issue will you like to report? \n')
            print('Thank you for contacting us')
            
        else:
            print('Invalid Option selected, please try again')
        
    else:
        print('password Incorrect, please try again')

else:

    print('Name not found, please try again')



