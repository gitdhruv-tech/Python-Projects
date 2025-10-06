# ATM Simulation
startBalance = 5000
ATMpin = "1234"
name = "Dhruv"
attempt = 3
while attempt > 0:
    x = input("Enter ATM Pin:\n")
    if x == ATMpin:
        choice = input("Main Menu \n 1->Deposit \n 2->Withdraw \n 3->Change PIN \n 4->Update Profile \n 5->Check Balance \n 6->Check Details \n 7->Exit \n")
        if choice == "Deposit" or choice == "1":
             a = int(input("Enter amount to deposit:\n"))
             startBalance += a
             print("Deposit success!")
        elif choice == "Withdraw" or choice == "2":
            b = int(input("Enter amount to withdraw:\n"))
            if(b>startBalance):
                print("Insufficent Balance!\nPlease enter correct amount.")
            else:
                startBalance -= b
                print("Withdrawal Success!")
        elif choice == "3":
            y = input("Enter new ATM Pin.\n")
            ATMpin = y
            print("Your pin is successfully changed.")
        elif choice == "4":
            newName= input("Enter new name:")
            name = newName
            print("Your Profile updated successfully.")
        elif choice == "Check Balance" or choice == "5":
            print("Your balance is:", startBalance)
        elif choice == "6":
            print("Account holder name is:",name)
            print("Account balance:",startBalance)
            print("Account number: 0261000275761")
        elif choice == "Exit" or choice == "7":
            print("Thank you for visiting.")
            break;
        else:
            print("Invaild choice.\nPlease select option from Main Menu.")
    else:
        attempt -= 1
        print("You have",attempt,"attempt left only.")
        print("Wrong ATM pin!!,Please enter correct pin.")
if attempt == 0:
    print("Too many attempts your account is locked.")

        
    
   