#!/usr/bin/env python3.6
import random

from locker import userdata, Credentials

def create_user(user_name, password, email):
  """
  Function that is used to create a new user.
  """
  new_user = userdata(user_name,password, email)
  return new_user

def save_user(user):
  """
  Function to save user.
  """
  user.user_save()
def display_users():
   return userdata.display_users()


def login_user(user_name,password):
  """
  function that checks whether a user exist and then logs the user in

  """
  check_user_exist = Credentials.check_user_exist(user_name,password)
  return check_user_exist

def create_credential(account_name,account_username, account_password):
  """
  Function to create a new credential.
  """
  new_credential = Credentials(account_name,account_username,account_password)
  return new_credential

def save_credential(credential):
  """
  Function to save new  credential.
  """
  credential.save_account()

def delete_account(credential):
  """
  Function to delete a credential.
  """
  credential.delete_account()

def display_accounts():
  """
  Function that returns all the saved credential.
  """
  return Credentials.display_accounts()

def generate_password():
  """
  Function that generates  a random password.
  """
  password_gen = Credentials.generate_password()

  return password_gen

def main():
  print("Welcome to passwordlocker")
  print('\n')
  while True:
    print('.'* 60)
    short_code = input("Use this short codes: su-create/sign up a new user account, ls-to display users, li-to log in (if you are done), ex - exit from password locker \n").lower().strip()
    print('.'* 60)

    if short_code == "ex":
        print("Thank you for choosing us and welcome !!")
        break

    elif short_code == "su":
        print("Sign Up")
        print('-' * 30)
        user_name = input("User_name: ")
        password = input("Password: ")
        email = input("Email: ")

        save_user(create_user(user_name,password,email))
        print('\n')

        print(f"Welcome,{user_name} your account has been created succesfully")
        print('\n')
        print('-' * 30)

    elif short_code == "ls":
        if display_users():
            print("Here is a list of our users")
            print('\n')
            for user in display_users():
                print(f"{user.user_name}")
                print('\n')
        else:
            print("no users available")


    elif short_code == "li":
        print("Please Enter your User name and your Password to log in")
        print('-' * 30)
        user_name = input("User name: ")
        password = input("password: ")
        sign_in = login_user(user_name,password)
        if sign_in == True:
            print(f"Hi,{user_name}, What would you like to do?")
            while True:
                print('.'* 60)
                short_code = input("Codes: cr - create an account, dp- display the list of your accounts, ex- exit the site \n").lower().strip()
                print('.'* 60)
                if short_code == "cr":
                    print("Create new credentials")
                    print('*' * 30)
                    account_name = input("Account name: ")
                    account_username = input("account User Name: ")
                    print('.'* 60)
                    password_option = input("What do you prefer: (ee-enter existing password) or (gr-generate new password) \n").strip()
                    print('.'* 60)
                    while True:
                        if password_option == "ee":
                            account_password = input("Enter your password (minimum 4 characters): ")
                            break
                        elif password_option == "gp":
                            account_password = generate_password()
                            break
                        else:
                            print("Invalid option")
                            break
                    save_credential(create_credential(account_name,account_username,account_password))
                    print('*' * 30)
                    print(f"New created account: \n Account:{account_name}\n User Name:{account_username} \n Password: {account_password}")
                    print('*' * 30)

                elif short_code == "dp":
                    if display_accounts():
                        print("Here is your accounts: ")

                        print('#' * 30)
                        for account in display_accounts():
                            print(f" account:{account.account_name} \n User Name:{account_username}\n Password:{account_password}")
                            print('_'* 30)
                        print('#' * 30)
                    else:
                        print("sorry......you dont have any accounts created")

                elif short_code == "ex":
                    print("Welcome back again")
                    break
                else:
                    print("Invalid Choice")



#                break

        else:
            print("You dont have an account.Please create an account ")

#    break

if __name__ == '__main__':
    
    main()