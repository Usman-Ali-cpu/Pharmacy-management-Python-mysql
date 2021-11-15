from typing import final
import pymysql
from pymysql import connections
from pymysql import cursors


class MedicineModel:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        try:
            self.connection = pymysql.connect(
                host=self.host, user=self.user, password=self.password, database=self.database)
        except Exception as e:
            print("There is error in connection", str(e))

    def __del__(self):

        if self.connection != None:
            self.connection.close()

    def check_user_exist(self, user):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                cursor.execute("select email from customer")
                customers = cursor.fetchall()

                for customer in customers:
                    if customer[0] == user.email:
                        return True
                return False
        except Exception as e:
            print("Exception in checkUserExist", str(e))
        finally:
            if cursor != None:
                cursor.close()

    def insert_customer(self, user):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "insert into customer (email, password) values (%s, %s)"
                args = (user.email, user.password)
                cursor.execute(query, args)
                self.connection.commit()
                return True
            return False
        except Exception as e:
            print("Exception in insert customer ", str(e))
        finally:
            if cursor != None:
                cursor.close()

    def check_admin_exist(self, admin):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                cursor.execute("select email from admin")
                admins = cursor.fetchall()

                for admin in admins:
                    if admin[0] == admin.email:
                        return True
                return False
        except Exception as e:
            print("Exception in checkadminExist", str(e))
        finally:
            if cursor != None:
                cursor.close()

    def insert_admin(self, admin):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "insert into admin (email, password) values (%s, %s)"
                args = (admin.email, admin.password)
                cursor.execute(query, args)
                self.connection.commit()
                return True
            return False
        except Exception as e:
            print("Exception in insert admin ", str(e))
        finally:
            if cursor != None:
                cursor.close()

    def check_medicine_exist(self, medicine):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                cursor.execute("select med_name from medicines")
                medicine_names = cursor.fetchall()
                for name in medicine_names:
                    if name[0] == medicine.name:
                        return True
                return False
        except Exception as e:
            print("Exception in checking medicine ", str(e))
        finally:
            if cursor != None:
                cursor.close()

    def insert_medicine(self, medicine):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "insert into medicines (med_name, med_formula, med_description, med_price, med_quantity) values(%s,%s, %s, %s, %s)"
                args = (medicine.name, medicine.formula,
                        medicine.description, medicine.price, medicine.quantity)
                cursor.execute(query, args)
                self.connection.commit()
        except Exception as e:
            print("Exception in insert Medicine " + str(e))
        finally:
            if cursor != None:
                cursor.close()

    def check_medicine_name(self, name):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select med_name from medicines where med_name = %s"
                args = (name)
                cursor.execute(query, args)
                data = cursor.fetchall()
                for d in data:
                    if d[0] == name:
                        print(d[0])
                        return True
                return False
        except Exception as e:
            print("Exception in checking Medicine " + str(e))
        finally:
            if cursor != None:
                cursor.close()

    def list_medicine(self):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select * from medicines"
                cursor.execute(query)
                data = cursor.fetchall()
                print(
                    "Med_id\t Med_name\t Med_formula\t Med_description\t Med_price\t Med_quantity")
                print(
                    "-----------------------------------------------------------------------------------------------")
                for d in data:
                    print(str(d[0]) + "\t   " + str(d[1]) + "\t   " + str(d[2]) + "\t   " +
                          str(d[3]) + "\t   " + str(d[4]) + "\t\t  " + str(d[5]))
                print(
                    "-----------------------------------------------------------------------------------------------\n")
        except Exception as e:
            print("Exception in Listing Medicines " + str(e))
        finally:
            if cursor != None:
                cursor.close()

    def delete_medicine(self, name):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "DELETE FROM medicines WHERE med_name = %s"
                args = (name)
                cursor.execute(query, args)
                self.connection.commit()
                print("Medicine has been deleted successfully")
        except Exception as e:
            print("Exception in Listing Medicines " + str(e))
        finally:
            if cursor != None:
                cursor.close()

    def display_alternates(self, formula, name):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select `med_name` , `med_description` , `med_price` from medicines WHERE med_formula = %s and med_name != %s"
                args = (formula, name)
                cursor.execute(query, args)
                data = cursor.fetchall()
                print(
                    "Med_name\t Med_description\t Med_price")
                print(
                    "----------------------------------------------------")
                for d in data:
                    print(str(d[0]) + "\t\t " +
                          str(d[1]) + "\t\t" + str(d[2]))
        except Exception as e:
            print("Exception in Listing Alternate Medicines " + str(e))
        finally:
            if cursor != None:
                cursor.close()

    def list_for_customer(self):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select `med_name` , `med_description` , `med_price` from medicines"
                cursor.execute(query)
                data = cursor.fetchall()
                print(
                    "Med_name\t Med_description\t Med_price")
                print(
                    "----------------------------------------------------")
                for d in data:
                    print(str(d[0]) + "\t\t " +
                          str(d[1]) + "\t\t" + str(d[2]))
                print("----------------------------------------------------")
        except Exception as e:
            print("Exception in Listing Medicines " + str(e))
        finally:
            if cursor != None:
                cursor.close()

    def getQuantity(self, name):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select med_quantity from medicines where med_name = %s"
                args = (name)
                cursor.execute(query, args)
                data = cursor.fetchall()
                return int(data[0][0])
        except Exception as e:
            print("Exception in getting quantity of Medicine " + str(e))
        finally:
            if cursor != None:
                cursor.close()

    def getprice(self, name):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select med_price from medicines where med_name = %s"
                args = (name)
                cursor.execute(query, args)
                data = cursor.fetchall()
                return int(data[0][0])
        except Exception as e:
            print("Exception in getting price of Medicine " + str(e))
        finally:
            if cursor != None:
                cursor.close()

    def getformula(self, name):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "select med_formula from medicines where med_name = %s"
                args = (name)
                cursor.execute(query, args)
                data = cursor.fetchall()
                return data[0][0]
        except Exception as e:
            print("Exception in getting formula of Medicine " + str(e))
        finally:
            if cursor != None:
                cursor.close()

    def update_inventory(self, name, amount):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "UPDATE medicines SET med_quantity = %s  WHERE med_name = %s"
                args = (amount, name)
                cursor.execute(query, args)
                self.connection.commit()
        except Exception as e:
            print("Exception in getting price of Medicine " + str(e))
        finally:
            if cursor != None:
                cursor.close()
