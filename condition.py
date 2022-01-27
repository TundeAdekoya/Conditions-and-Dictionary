# if "ada" == "ada":
#     print("Correct")
# else:
#     print("Incorrect")


user_data = {"adekoyatunde.com":"Adekoya Tunde"}
choice = input("Enter email:\n>")
if choice in user_data.keys():
    print("Account Already Exist")    
else :
    print("Account does not exist")



# user_data = {"adekoyatunde.com":"adekoya tunde"}

# user_email = input("Enter your email\n>").lower()

# ##print(user_email in user_data.keys())

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

#     #print(acc_num, " ", pin)

#     user = data.get(acc_num)  #Out is either NONE or the Value

#     if user and user['pin'] == pin:
#         print(f"Welcomme {user['name']}.\nYour account balance is ${user['bal']}")
#     else:
#         print("Invalid Login")