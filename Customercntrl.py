from MedicineModel import MedicineModel
from ViewClasses import Customer, Medicine


class CustomerControler:
    def __init__(self) -> None:
        self.model = MedicineModel("localhost", "root", "", "medicine")

    def list_alternates(self, formula, name):
        self.model.display_alternates(formula, name)

    def purchase(self):
        choice = "Y"
        while choice == "Y" or choice == "y":
            self.model.list_for_customer()
            name = input("\nEnter name of medicine from list : ")
            medexist = self.model.check_medicine_name(name)
            if(medexist == True):
                amount = int(input("Enter quantity you want to purchase : "))
                while(amount > self.model.getQuantity(name)):
                    print("Not much quantity is available")
                    formulachoice = input(
                        "Do you want to find medicine with same formula ? Y/N: ")
                    if formulachoice == 'Y' or formulachoice == 'y':
                        formulaa = self.model.getformula(name)
                        self.list_alternates(formulaa, name)
                        name = input("Enter name of medicine : ")
                        amount = int(
                            input("Enter quantity you want to purchase : "))
                    else:
                        amount = int(
                            input("Enter quantity you want to purchase : "))
                if(amount <= self.model.getQuantity(name)):
                    print("------------ Receipt -------------")
                    print("You have purchased " + name)
                    print("Quantity : " + str(amount))
                    price = self.model.getprice(name)
                    print("Total :  " + str(price*amount))
                    print("------------ ------ -------------")
                    updateamount = self.model.getQuantity(name) - amount
                    self.model.update_inventory(name, updateamount)
            else:
                print("Sorry, Don't have medicine with this name!")
            choice = input("Do you want to purchase more ? Y/N: ")
