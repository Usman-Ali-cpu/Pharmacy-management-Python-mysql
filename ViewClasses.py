class Medicine:
    def __init__(self) -> None:
        self.name = ""
        self.formula = ""
        self.description = ""
        self.price = 0
        self.quantity = 0

    def __init__(self, mname, mformula, mprice, mdes, mqty) -> None:
        self.name = mname
        self.formula = mformula
        self.description = mdes
        self.price = mprice
        self.quantity = mqty


class Customer:
    def __init__(self, email, pwd):
        self.email = email
        self.password = pwd


class Admin:
    def __init__(self, email, pwd):
        self.email = email
        self.password = pwd
