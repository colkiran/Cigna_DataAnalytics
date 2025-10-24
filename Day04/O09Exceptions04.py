"""
Requirement

Withdraw money from bank:
  a. balance in bank should not be less than 1000
  b. user account will be blocked for an hour of the user enters wrong pin for 3 times

"""

import time

class BalanceExceptionError(Exception):
    pass

class AttemptExceptionError(Exception):
    pass

attempt = 0
def withDraw():
    global attempt
    balance = 10000
    saved_pin = 1234
    pin = int(input("Enter the PIN :"))
    if pin == saved_pin:
        try:
            amt = float(input("Enter the amount to be withdrawn :"))
            temp_bal = balance - amt

            if temp_bal < 1000:
                raise BalanceExceptionError("Insufficient funds.......")

            balance = balance - amt
            print("Amount debitted successfully from the account ending #####......")
            print(f"The balance amount in the account is : {balance}")

        except Exception as var:
            print(var)
    else:
        ans = input("Do you want to reenter the pin :")
        if ans.lower() == 'y':
            attempt += 1
            try:
                if attempt == 4:
                    raise AttemptExceptionError("Too many attempts, you account is blocked for an hour....")

            except Exception as var:
                print(var)
                time.sleep(3600)
            else:
                withDraw()
            finally:
                print("Thank you for using #### bank.......")
                return



withDraw()