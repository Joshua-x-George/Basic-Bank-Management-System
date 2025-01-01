import random
from graphT import plotgraph

#constants
domains = ('gmail.com','yahoo.com','hotmail.com','icloud.com','yahoo.in','ymail.com','outlook.com','@email.com')
is_running = True
#format for user-> users = {user:{password:<str>,email:<str>,name:<str>,phone:<str>,balance:<int>,creditscore:<list>}...etc}
users = {'Tuser': {'password': 'pass', 'email': '@gmail.com', 'name': 'Tuser', 'phone': '0000000000', 'creditscore': [525,600,725,500,525,550,600,525,575,625,500,750,525,550,650], 'balance': 5000}}

print("*****************BANKING PROGRAM*****************")
#print("***********************************************")
while is_running:
    #Home Page
    print('\n*************************************************')
    print('''
            ┌────────────────┐
            │1.User Login    │
            │2.Register User │
            │3.Exit          │
            └────────────────┘''')
    print('\n*************************************************')
    Hopt = input("Enter choice 1-3: ")
    print('*************************************************')
    if len(Hopt) != 1 or Hopt not in '123' :#checks if option is within range
        print("\n'",Hopt,"'","is not valid!\nPlease Enter Again!",sep='')
        
    elif Hopt == '1':
        #login page
        loginpage = True
        while loginpage:
            if len(users) == 0:
                print("There are no registered USERS currently!\nPlease Register!")
                input("(Press <Enter> to continue)")
                break
            user = input("Enter the username: ")
            #Checks if user is in dictionary of users
            if user not in users: 
                #Runs if user is not found and returns to Home
                print('\n*************************************************')
                print("\nUser ","'",user,"'"," does not exist!",sep = '')
                input("(Press Enter to return Home)")
                break
            else:
                #Runs if user is found
                print('*************************************************\n')
                passw = input("Enter password for " + user + ": ")
                #Checks password
                if passw == users[user]['password']:
                    #Runs if Password is correct
                    print('''
*************************************************
┌───────────────────────────────────────────────┐
│                 WELCOME!                      │
└───────────────────────────────────────────────┘''')
                    userpage = True
                    while userpage:#Userpage
                        print('*************************************************\n')
                        print('''
             ┌──────────────────────┐
             │1.Show Balance        │
             │2.deposit Money       │
             │3.withdraw Money      │
             │4.Money Transfer      │
             │5.Show Credit score   │
             │6.User details        │
             │7.Lottery             │
             │8.Home                │
             └──────────────────────┘
                              ''')
                        print('\n************************************************* ')
                        
                        opt = input("Enter choice 1-8: ")
                        if len(opt) != 1 or  opt not in '12345678':
                            print("\n'",opt,"'","is not valid!\nPlease Enter Again!",sep='')
                            
                        elif opt == '1':
                            #To check balance
                            print("Your Balance is ₹",users[user]['balance'],sep = '')
                            input("(Press <Enter> to continue)")
                            
                        elif opt == '2':
                            #To deposit money
                            while True:
                                balc = input("Enter the amount to deposit: ₹")
                                if not balc.isdigit():
                                    print("\nEnter again as ","'",balc,"'"," is not valid!",sep = '')
                                elif int(balc) < 0:
                                    print("\nEnter again as ","'",balc,"'"," is not valid!",sep = '')
                                else:
                                    if int(balc) > users[user]['balance']*0.1:
                                        if users[user]['creditscore'][-1] <= 725:
                                            users[user]['creditscore'].append(users[user]['creditscore'][-1]+25)
                                            if len(users[user]['creditscore']) > 15:
                                                del users[user]['creditscore'][0]
                                        
                                    users[user]['balance']+=int(balc)
                                    
                                    print("\nDeposited ₹",balc," to the account\nRemaining balance: ₹",users[user]['balance'],sep='')
                                    input("(Press <Enter> to continue)")
                                    break
                                    
                            
                        elif opt == '3':
                            #To withdraw money
                            while True:
                                if users[user]['balance'] <= 0:
                                    print("\nYou have insufficient funds!")
                                    break
                                balc = input("Enter the amount to Withdraw: ₹")
                                if not balc.isdigit():
                                    print("\nEnter again as ","'",balc,"'"," is not valid!",sep = '')
                                elif int(balc) < 0:
                                    print("\nEnter again as ","'",balc,"'"," is not valid!(as it is negative)",sep = '')
                                elif int(balc) > users[user]['balance']:
                                    print("\nInsufficient Funds as you only have ₹",users[user]['balance'],sep='')
                                    
                                else:
                                    if int(balc) > users[user]['balance']*0.5:
                                        if int(balc) > users[user]['balance']*0.75:
                                            if users[user]['creditscore'][-1] >= 375:
                                                users[user]['creditscore'].append(users[user]['creditscore'][-1]-75)
                                                if len(users[user]['creditscore']) > 15:
                                                    del users[user]['creditscore'][0]
                                        else:
                                            if users[user]['creditscore'][-1] >= 350:
                                                users[user]['creditscore'].append(users[user]['creditscore'][-1]-50)
                                                if len(users[user]['creditscore']) > 15:
                                                    del users[user]['creditscore'][0]
                                    users[user]['balance'] -= int(balc)
                                    print("\nWithdrawn ₹",balc," from the account\nRemaining balance: ₹",users[user]['balance'],sep='')
                                    input("(Press <Enter> to continue)")
                                    break
                        elif opt == '4':
                            #Money transfer
                            transferpage = True
                            while transferpage:
                                if users[user]['balance'] <= 0:
                                    print("\nYou have insufficient funds!\n you cannot transfer with ₹0 balance!")
                                    transferpage = False
                                    break
                                transuser = input("Enter the username of the transee: ").lower()
                                if transuser not in users:
                                    print(transuser,"does not EXIST!\nGoing Home!")
                                    input("(Press <Enter> to continue)")
                                    while True:
                                        topt = input("\nEnter again? (y/n): ").lower()
                                        if topt not in 'yn' or len(opt) != 1:
                                            print("\nEnter a valid output!\nPlease Enter your choice again!")
                                        elif topt == 'y':
                                            break
                                        else:
                                            transferpage = False
                                            break
                                elif transuser == user:
                                    print("\nYou cannot transfer to yourself!\nGoing Home!")
                                    input("(Press <Enter> to continue)")
                                    transferpage = False
                                else:
                                    while True:
                                        balc = input("Enter the money to transfer: ")
                                        if not balc.isdigit():
                                            print("Enter again as ","'",balc,"'"," is not valid!",sep = '')
                                        elif int(balc) < 0:
                                            print("Enter again as ","'",balc,"'"," is not valid!(as it is negative)",sep = '')
                                        elif int(balc) > users[user]['balance']:
                                            print("Insufficient Funds as you only have ₹",users[user]['balance'],sep='')
                                            transferpage = False
                                            break
                                        else:
                                            if int(balc) > users[user]['balance']*0.5:
                                                if int(balc) > users[user]['balance']*0.75:
                                                    if users[user]['creditscore'][-1] >= 350:
                                                        users[user]['creditscore'].append(users[user]['creditscore'][-1]-50)
                                                        if len(users[user]['creditscore']) > 15:
                                                            del users[user]['creditscore'][0]
                                                    
                                                else:
                                                    if users[user]['creditscore'][-1] >= 325:
                                                        users[user]['creditscore'].append(users[user]['creditscore'][-1]-25)
                                                        if len(users[user]['creditscore']) > 15:
                                                            del users[user]['creditscore'][0]
                                            if int(balc) > users[transuser]['balance']*0.25:
                                                if int(balc) > users[transuser]['balance']*0.5:
                                                    if users[user]['creditscore'][-1] <= 700:
                                                        users[user]['creditscore'].append(users[user]['creditscore'][-1]+50)
                                                        if len(users[user]['creditscore']) > 15:
                                                            del users[user]['creditscore'][0]
                                                else:
                                                    if users[user]['creditscore'][-1] <= 725:
                                                        users[user]['creditscore'].append(users[user]['creditscore'][-1]+25)
                                                        if len(users[user]['creditscore']) > 15:
                                                            del users[user]['creditscore'][0]
                                            users[user]['balance'] -= int(balc)
                                            users[transuser]['balance'] += int(balc)
                                            transferpage = False
                                            print("You have transferred ₹",balc," to the account ",transuser,"\nRemaining balance: ₹",users[user]['balance'],sep='')
                                            input("(Press <Enter> to continue)")
                                            break
                        
                        elif opt == '5':#prints credit score graph and to see if its good or bad
                            while True:
                                print('''
            ┌──────────────────────┐
            │1.Show credit Score   │
            │2.Show credit graph   │
            └──────────────────────┘
                                      ''')
                                copt = input("Enter option 1-2: ")
                                if len(copt) != 1 or copt not in '12':
                                    print("Invalid Input!")
                                    input("(Press <Enter> to continue)")
                                elif copt == '1':
                                    print("your credit score is:",users[user]['creditscore'][-1])
                                    if users[user]['creditscore'][-1] > 600:
                                        print("You have a GOOD Credit Score!    ദ്ദി(｡•̀ ,<)~✩‧₊")
                                    elif users[user]['creditscore'][-1] < 400:
                                        print("You have a VERY BAD Credit Score!     ദ്ദി ༎ຶ‿༎ຶ )")
                                    elif users[user]['creditscore'][-1] < 500:
                                        print("You have a BAD Credit Score!     .·°՞(¯□¯)՞°·.")
                                    else:
                                        print("You have an OK Credt Score   (^▽^)")
                                    input("(Press <Enter> to continue)")
                                    
                                    break
                                    
                                    
                                elif copt == '2':
                                    plotgraph(users[user]['creditscore'],scaley=25)
                                    input(('\t'*6)+"(Press <Enter> to continue)")
                                    break
                        elif opt == '6':
                            #uSER DETAILS
                            print('Name     :',users[user]['name'])
                            print('Username :',user)
                            print('email    :',users[user]['email'])
                            print('phone    : +91',users[user]['phone'])
                            print('credit sc:',users[user]['creditscore'][-1])
                            input("(Press <Enter> to continue)")
                            
                            
                        elif opt == '7':
                            if users[user]['balance'] == 0:
                                print("Insufficient funds!")
                                input("(Press <Enter> to continue)")
                            while users[user]['balance'] > 0:
                                
                                gambled_money = input("Enter the amount of Money you are betting on: ₹")
                                if not gambled_money.isdigit():
                                    print("Invalid!\nEnter a valid number!")
                                else:
                                    gambled_money = int(gambled_money)
                                    if gambled_money <= users[user]['balance']:
                                        
                                        
                                        lottery_guess = []
                                        print("Please enter 5 choices of numbers that are two digit numbers.")
                                        for i in ('one','two','three','four','five'):
                                            while True:
                                                user_input = input("Enter choice " + i + " : ")
                                                if len(user_input) != 2 or not user_input.isdigit() or user_input[0] == '0':
                                                    print("You have entered an invalid choice\nPlease Enter Again!")
                                                else:
                                                    lottery_guess.append(int(user_input))
                                                    break
                                        winnos = []
                                        numbers_guessed = 0
                                        for i in range(5):
                                            winnos.append(random.randint(10,99))
                                        print("The Winning numbers were:",winnos)
                                        print("Your correct guesses: ",end = '')
                                        for i in lottery_guess:
                                            if i in winnos:
                                                numbers_guessed +=1
                                                print(winnos.pop(winnos.index(i)),end = ' ')
                                        print()
                                        if numbers_guessed == 0:
                                            winnings = 0
                                        else:
                                            winnings = pow(gambled_money,numbers_guessed+1)
                                        users[user]['balance'] -= gambled_money
                                        users[user]['balance'] += winnings
                                        print("Your winnings: ₹",winnings,"     (˶ᵔ ᵕ ᵔ˶)",sep='',)
                                        print("Your current balance is ₹",users[user]['balance'],sep='')
                                        input("(Press <Enter> to continue)")
                                        break
                                    else:
                                        print("You have insufficient funds!\nRemaining funds: ₹",users[user]['balance'],sep='')
                                        input("(Press <Enter> to continue)")
                                        break

                        elif opt == '8':
                            #HOME
                            userpage = loginpage = False
                            
                else:
                    #Runs if password is incorrect and returns home
                    print("Your password is incorrect!")
                    forgotpassword = True
                    while forgotpassword:
                        lopt = input("Forgot password? (y/n): ").lower()
                        if len(lopt) != 1 or lopt not in 'yn':
                            print("Enter a valid output!\nPlease Enter your choice again!")
                        elif lopt == 'y':
                            print("PLEASE VERIFY YOUR IDENTITY")
                            femail = input("Enter the email address of the user "+ user +" : ")
                            fname = input("Enter your full name: ").upper()
                            fphone = input("Enter your phone number: ")
                            if femail == users[user]['email'] and fname == users[user]['name'] and fphone == users[user]['phone']:
                                fpasswcreate = True
                                while fpasswcreate:
                                    passw = input("Enter your new password for "+ user + ": ")
                                    if len(passw) < 5:
                                        print("Password musn't contain less than 5 characters!\nPlease Enter Again!")
                                    else:
                                        passwc = input("Confirm password: ")
                                        if passw != passwc:
                                            print("Incorrect Password\nPlease enter again")
                                        else:
                                            users[user]['password'] = passw
                                            fpasswcreate = forgotpassword = False
                                        print("\n********LOGIN PAGE********")
                            else:
                                print("Unable to verify identity")
                                input("(Press Enter to Return Home)")
                                loginpage = forgotpassword = False    
                        else:
                            forgotpassword = False    
                    
    
    elif Hopt == '2':
        #Goes to register user
        #username password email name phone balance = 0
        registerpage = True
        print("""
            |Rules for creating username--------------> 
            |           |#1->Username cant be any shorter than 3 CHARACTERS long
            |           |#2->Username cant contain any SPACES
            |           |#3->Username must be unique
            |           |#4-Username must be in all LOWERCASE
                  """)
        input("OK?\npress <enter> to continue")
        while registerpage:

            user = input("Enter a new username: ")
            if user in users:
                print("'",user,"'"," Already exists\nPlease enter a new username!",sep= '')
            elif len(user) < 3:
                print("Username cant be shorter than 3 characters long\nPlease enter again!")
            elif not user.isalpha():
                print("Username can't have any spaces\n And can only contain lower case alphabets (a to z)\nPlease enter again!")
            elif not user.islower():
                print("Username can only contain in lowercase characters\nPlease Enter again!")
            else:
                users[user] = {}
                passwcreate = True
                print("Password must contain minimum 5 Characters!")
                while passwcreate:
                    passw = input("Enter password for "+ user + ": ")
                    if len(passw) < 5:
                        print("Password musn't contain less than 5 characters!\nPlease Enter Again!")
                    else:
                        passwc = input("Confirm password: ")
                        if passw != passwc:
                            print("Incorrect Password\nPlease enter again")
                        else:
                            users[user]['password'] = passw
                            break
                emailcreate = True
                while emailcreate:
                    users[user]['email'] = None
                    email = input("Enter email id: ")
                    #example@gmail.com
                    emailcheckflag = False
                    for i in users.values():
                        if i['email'] == email:
                            emailcheckflag = True
                    if "@" not in email:
                        print("'",email,"'"," Is Not Valid\nvalid emails are in the form 'example@domain'\nPlease enter again",sep = '' )
                    elif email.count('@') != 1:
                        print("'",email,"'"," Is Not Valid\nvalid emails are in the form 'example@domain'\nPlease enter again",sep = '' )
                    elif email.split('@')[-1] not in domains:
                        print("'",email,"'"," domain is Not Supported!\nPlease enter again",sep = '' )
                    elif emailcheckflag:
                        print("'",email,"'"," already exists please enter again",sep = '' )
                    else:
                        emailc = input("Confirm email: ")
                        if email != emailc:
                            print("Incorrect Email\nPlease enter again")
                        else:
                            users[user]['email'] = email
                            break
                namecreate = True
                while namecreate:
                    name = input("Enter your full name (IN FULL CAPS): ")
                    if not name.isupper():
                        print("is not upper case")
                    else:
                        users[user]['name'] = name
                        namecreate = False
                phonecreate = True
                while phonecreate:
                    phone = input("Enter your phone number (eg: 9447712123): ")
                    if not phone.isdigit():
                        print("Your entered phone number is not valid!\nPlease Enter Again!")
                    elif len(phone) !=10:
                        print("Your phone number is not valid as it can only contain exactly 10 digits\nPlease Enter Again!")
                    else:
                        users[user]['phone'] = phone
                        phonecreate = False
                
                
                users[user]['creditscore'] = [525]
                users[user]['balance'] = 5000
                print("\nYOU HAVE SUCCESSFULLY REGISTERED YOUR USER\nPlease login through the user portal!")
                print("You have been credited ₹5000 for choosing our bank!\nTHANK YOU!")
                input("(Press Enter to Return Home)")                            
                
                    
                registerpage = False
    
    elif Hopt == '3':
        #Exits the program
        is_running = False
print("THANK YOU!")

    
