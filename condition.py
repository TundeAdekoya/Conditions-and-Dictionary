# if "ada" == "ada":
#     print("Correct")
# else:
#     print("Incorrect")


# user_data = {"adekoyatunde.com":"Adekoya Tunde"}
# choice = input("Enter email:\n>")
# if choice in user_data.keys():
#     print("Account Already Exist")    
# else :
#     print("Account does not exist")



# user_data = {"adekoyatunde.com":"adekoya tunde"}

# user_email = input("Enter your email\n>").lower()

#print(user_email in user_data.keys())

# if user_email in user_data.keys():
#     print("Account alreay exist")

# else:
#     choice = input("Do you want to subscribe? (Y/y or N/n)\n>").lower()

#     if choice == 'y':
#         name = input("Enter your Full name:\n>")
#         user_data[user_email] = name
#         print("Successfully subscibed")

#     elif choice =='n':
#         print("Goodbye!")

#     else:
#         print("Invalid Input")



#TO CHECK WITHOUT LEAVING EMPTY SPACE
# if user_email.isspace() or user_email == "":

#     print("No Entry")

# else:
#     if user_email in user_data.keys():
#         print("Account alreay exist")

#     else:
#         choice = input("Do you want to subscribe? (Y/y or N/n)\n>").lower()

#         if choice == 'y':
#             name = input("Enter your Full name:\n>")
#             user_data[user_email] = name
#             print("Successfully subscibed")

#         elif choice =='n':
#             print("Goodbye!")

#         else:
#             print("Invalid Input")

#------------------CLASS WORK-----------------------
# data = {
#     "3947758475" : {
#         "name" : "Desmond",
#         "dob" : "09 - 09 - 89",
#         "bvn" : "123456789",
#         "pin" : "1234",
#         "bal":0
#     }
# }

# print('Welcome to the AstroBank App')
# print('Enter s to signup or l to login:')
# choice = input(">").lower()

# if choice == "l":
#     acc_num = input("Enter your account num:\n>")
#     pin = input("Enter your pin\n>")

#     print(acc_num, " ", pin)

#     user = data.get(acc_num)  #Out is either NONE or the Value

#     if user and user['pin'] == pin:
#         print(f"Welcome {user['name']}.\nYour account balance is ${user['bal']}")

#     else:
#         print("Invalid Login")

#------------ASSIGNMENT---------------------
data = {
    "3947758475" : {
        "name" : "Desmond",
        "dob" : "09 - 09 - 89",
        "bvn" : "123456789",
        "pin" : "1234",
        "bal":12000
    },
}

print('Welcome to the AstroBank App')
print('Enter s to signup or l to login:')
choice = input(">").lower()

if choice == "l":
    acc_num = input("Enter your account num:\n>")
    pin = input("Enter your pin\n>")

    print(acc_num, " ", pin)

    user = data.get(acc_num)  #Out is either NONE or the Value

    if user and user['pin'] == pin:
        print(f"Welcome {user['name']}.\nYour account balance is ${user['bal']}")

        print("Enter d to Deposit, w to Withdrawl, and e to Enquire")
        choice = input(">").lower()

#DEPOSIT
        
        if choice == 'd':
            amount = int(input("Enter the amount to deposit:\n>"))
            user['bal'] += amount
            print(f"Your New Balance ${user['bal']}.\nThanks for banking with Astroverse")

#WITHDRAW

        if choice == 'w':
            amount = int(input("Enter the amount to withdrawl:\n>"))
            if(amount > user['bal']):
                print("Insufficient Funds")

            else:
                user['bal'] -= amount
                print(f"You have ${user['bal']} remaining.\nThanks for banking with Astroverse")

#ENQUIRE

        if choice == 'e':
            print(f"Your balance is ${user['bal']}.\nThanks for banking with Astroverse")

    else:
        print("Invalid Login")

        

#ASSIGNMENT SIGNUP, WITHDRAW, AND DEPOSIT 

#SIGNUP>

if choice == 's':

    new_data = {
            "name":" ",
            "email":" ",
            "D.O.B":" ",
            "bvn":" ",
            "pin":" ",
            "bal":2
    }

    new_data["name"] = input("Enter your name:\n>")
    new_data["email"] = input("Enter your email:\n>")
    new_data["D.O.B"] = input("Enter your date of birth:\n>")
    new_data["bvn"]= input("Enter your BVN:\n>")
    new_data["pin"]= input ("Enter your pin:\n>")

    print(new_data)

    user = new_data.get("bvn")

    if user in new_data.values():
        import random   
        account_number = random.randint(1000000, 2000000)

        print (f"Congrats {new_data['name']}.\nYou have successfully created your account.\nYour account number is {account_number}.")

        print("Enter d to Deposit, w to Withdrawl, and e to Enquire")
        choice = input(">").lower()

#DEPOSIT
        
        if choice == 'd':
            amount = int(input("Enter the amount to deposit:\n>"))
            new_data['bal'] += amount
            print(f"Your New Balance ${new_data['bal']}.\nThanks for banking with Astroverse")

#WITHDRAW

        if choice == 'w':
            amount = int(input("Enter the amount to withdrawl:\n>"))
            if(amount > new_data['bal']):
                print("Insufficient Funds\n")

            else:
                new_data['bal'] -= amount
                print(f"You have ${new_data['bal']} remaining.\nThanks for banking with Astroverse")

#ENQUIRE

        if choice == 'e':
            print(f"Your balance is ${new_data['bal']}.\nThanks for banking with Astroverse")

    else:
        print("Invalid Details")


