# -*- coding: utf-8 -*-
class Service:
    pass

class User:
    #genrator
    #static variable
    f = None
    
    #static function
    def account_id_gen():
        account_id = 100
        while True:
            yield account_id
            account_id += 1
    
    #Before creating any account holder or admin  
    #static function      
    def callOnce():
        User.f = User.account_id_gen()
    
    def __init__(self, name, age=20, address="abc", aadhar_id="aad", pan="alhp", account_type="savings", phone="NA"):
        self.name = name
        self.age = age
        self.phone = phone
        self.account_type = account_type
        self.pan = pan
        self.aadhar_id = aadhar_id
        self.account_id = next(User.f)
        
    

class AccountHolder(User):
    def __init__(self, name, init_amount, branch, min_balance = 5000):
        super().__init__(name)
        self.balance = init_amount
        self.min_balance = min_balance
        branch.addAccountHolderToBranch(self)
        
    def add_money(self,amount):
        self.balance += amount
        
    def withdraw_money(self,amount):
        if (self.balance - self.min_balance) >= amount:
            self.balance -= amount
            
    def __repr__(self):
        return self.name + ' ' + str(self.balance)


class Admin(User):
    pass
