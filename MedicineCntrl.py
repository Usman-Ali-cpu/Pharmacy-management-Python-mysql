from MedicineModel import MedicineModel
from ViewClasses import Admin, Customer, Medicine


class MedicineControler:
    def __init__(self) -> None:
        self.model = MedicineModel("localhost", "root", "", "medicine")

    def signup(self):
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        u = Customer(email, password)
        exist = self.model.check_user_exist(u)
        if exist == False:
            insert = self.model.insert_customer(u)
            if insert:
                print("Signup successful")
                return True
            else:
                print("Error in signup")
                return False
        else:
            print("User already exist")
            return False

    def sign_in(self):
        email = input("Enter email : ")
        password = input("Enter password : ")
        user = Customer(email, password)
        exist = self.model.check_user_exist(user)
        if exist == False:
            print("User doesn't exist!")
            choice = input("Do you want to Sign up ? (Y/N) : ")
            if(choice == "Y" or choice == "y"):
                return self.signup()
        else:
            print("You have been login successfully")
            return True

    def admin_signup(self):
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        u = Admin(email, password)
        exist = self.model.check_admin_exist(u)
        if exist == False:
            insert = self.model.insert_admin(u)
            if insert:
                print("Signup successful")
                return True
            else:
                print("Error in signup")
                return False
        else:
            print("User already exist")
            return False

    def admin_sign_in(self):
        email = input("Enter email : ")
        password = input("Enter password : ")
        admin = Admin(email, password)
        exist = self.model.check_admin_exist(admin)
        if exist == False:
            print("admin doesn't exist!")
            choice = input("Do you want to Sign up ? (Y/N) : ")
            if(choice == "Y" or choice == "y"):
                return self.admin_signup()
        else:
            print("You have been login successfully")
            return True

    def add_medicine(self):
        name = input("Enter name of medicine : ")
        formula = input("Enter formula of medicine : ")
        description = input("Enter description of medicine: ")
        price = int(input("Enter price: "))
        quantity = int(input("Enter available quantity of medicine : "))
        newmedicine = Medicine(name, formula, price, description, quantity)
        checkexist = self.model.check_medicine_exist(newmedicine)
        if checkexist == True:
            print("Medicine with name " + name + " already exist")
        else:
            self.model.insert_medicine(newmedicine)
            print("Medicine has been Added successfully")

    def remove_medicine(self):
        name = input("Enter name of medicine to remove : ")
        checkexist = self.model.check_medicine_name(name)
        if checkexist == False:
            print("Medicine doesn't exist")
            self.model.list_medicine()
            name = input("\nChoice medicine by entering name : ")
            if(self.model.check_medicine_name(name)):
                self.model.delete_medicine(name)
            else:
                print("Name is incorrect! You can't proceed to delete")
        else:
            self.model.delete_medicine(name)

    def listing_medicine(self):
        self.model.list_medicine()

    def listing_medicine_customer(self):
        self.model.list_for_customer()

    def list_alternates(self, formula, name):
        self.model.display_alternates(formula, name)
