# ================= ATM SIMULATION SYSTEM =================

# ---------- Global Variables ----------

account_pin = "1234"
account_balance = 25000
account_holder_name = "Anish"
trasaction_count = 0

# ---------- Functions ----------

def verify_pin():
    entered_pin = input("Enter your ATM Pin: ")
    if entered_pin == account_pin:
        print("PIN verified successfully.")
        return True
    else:
        print("Invalid PIN.")
        return False

def check_balance():
    print(f"\nAccount Holder: {account_holder_name}")
    print(f"Available Balance: {account_balance}")

def deposit_money():
    global account_balance, trasaction_count

    deposit_amount = float(input("Enter money: "))
    if deposit_amount >= 0:
        account_balance = account_balance + deposit_amount
        trasaction_count = trasaction_count + 1
        print("\nDeposit successful.")
        print(f"Updated balance: Rs. {account_balance}")
    else:
        print("\nInvalid deposit amount!")

def withdraw_money():
    global account_balance, transaction_count

    withdraw_amount = float(input("Enter amount to withdraw: ₹"))

    if withdraw_amount <= 0:
        print("Invalid withdrawal amount!")
    elif withdraw_amount > account_balance:
        print("Insufficient balance!")
    else:
        account_balance = account_balance - withdraw_amount
        transaction_count = transaction_count + 1
        print("Please collect your cash.")
        print("Remaining Balance: ₹", account_balance)


def change_pin():
    global account_pin

    old_pin = int(input("Enter current PIN: "))
    if old_pin == account_pin:
        new_pin = int(input("Enter new PIN: "))
        confirm_pin = int(input("Confirm new PIN: "))

        if new_pin == confirm_pin:
            account_pin = new_pin
            print("PIN changed successfully.")
        else:
            print("PIN mismatch! PIN not changed.")
    else:
        print("Incorrect current PIN!")


def show_transaction_count():
    print("Total transactions performed:", transaction_count)


# ---------- Main ATM Menu ----------
print("=============== Welcome to ATM =================")

if verify_pin():
    while True:
        print("\n========== ATM MENU ==========")
        print("1. Balance Inquiry")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Transaction Count")
        print("6. Exit")

        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            check_balance()
        elif user_choice == "2":
            deposit_money()
        elif user_choice == "3":
            withdraw_money()
        elif user_choice == "4":
            change_pin()
        elif user_choice == "5":
            show_transaction_count()
        elif user_choice == "6":
            print("Thank you for using ATM.")
            break
        else:
            print("Invalid choice! Please try again: ")
else:
    print("ATM card blocked due to incorrect PIN.")