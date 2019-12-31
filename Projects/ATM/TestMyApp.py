# -*- coding: utf-8 -*-
from User import User,AccountHolder
from Bank import Bank,BankBranch

#System Initializer
User.callOnce()

#Create Bank & Branches
bank = Bank('Kotak')
bank_branch = BankBranch(101,'Whitefield',bank)

#Create account in branches
a = AccountHolder('jack',10000, bank_branch)
a.add_money(12000)
a.withdraw_money(2000)

a = AccountHolder('jill',20000, bank_branch)
a.add_money(2000)
a.withdraw_money(5000)


bank.showAllBranchesAndAccountHolders()

#Create ATM Machines



#Allocate ATM card to account holders


#Account Holders do transaction