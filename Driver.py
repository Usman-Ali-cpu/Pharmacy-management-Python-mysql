from Customercntrl import CustomerControler
from MedicineCntrl import MedicineControler
from os import system

controller = MedicineControler()
controller2 = CustomerControler()
while True:
    print("\t**************************")
    print("\tEnter 1. FOR CUSTOMER LOGIN")
    print("\tEnter 2. FOR ADMIN LOGIN")
    print("\tEnter 3. Exit")
    print("\t**************************\n")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        customerlogin = controller.sign_in()
        if customerlogin:
            print("\t************ WELLCOME TO STORE ***************")
            while True:
                print("\t**************************")
                print("\tEnter 1. TO LIST MEDICINE")
                print("\tEnter 2. TO BUY MEDICINE")
                print("\tEnter 3. TO SIGN OUT")
                print("\t**************************\n")
                customerchoice = int(input("Enter your choice: "))
                if customerchoice == 1:
                    controller.listing_medicine_customer()
                if customerchoice == 2:
                    controller2.purchase()
                if customerchoice == 3:
                    system("cls")
                    break

    if choice == 2:
        adminlogin = controller.admin_sign_in()
        if adminlogin:
            print("\t************* YOU ARE ADMIN *****************")
            while True:
                print("\t**************************")
                print("\tEnter 1. TO LIST MEDICINE")
                print("\tEnter 2. TO ADD MEDICINE")
                print("\tEnter 3. TO DELETE MEDICINE")
                print("\tEnter 4. TO SIGN OUT")
                print("\t**************************\n")
                adminchoice = int(input("Enter your choice: "))
                if adminchoice == 1:
                    controller.listing_medicine()
                if adminchoice == 2:
                    controller.add_medicine()
                if adminchoice == 3:
                    controller.remove_medicine()
                if adminchoice == 4:
                    system("cls")
                    break

    if choice == 3:
        exit(0)

    # controller.sign_in()
    # controller.add_medicine()
    # controller.add_medicine()
    # controller.add_medicine()
    # controller.listing_medicine()
    # controller.list_alternates("2x456", "disprin")
    # # controller.remove_medicine()
    # # controller.listing_medicine()
    # con = CustomerControler()
    # con.purchase()
