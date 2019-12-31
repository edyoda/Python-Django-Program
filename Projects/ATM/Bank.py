# -*- coding: utf-8 -*-
class Bank:
    def __init__(self, name):
        self.name = name
        self.branches = []
        self.bank_atms = []
        
    def addBranchToBank(self,branch):
        self.branches.append(branch)
        
    def showAllBranchesAndAccountHolders(self):
        for branch in self.branches:
            print (branch.branch_id, branch.address)
            for account in branch.accounts:
                print (account)
                
    def addATMMachineToBank(self,atm_machine):
        self.bank_atms.append(atm_machine)

class BankBranch:
    def __init__(self,branch_id,address,bank):
        self.branch_id = branch_id
        self.bank = bank
        self.address = address
        self.accounts = []
        self.managed_atm = []
        #adding new branch to the bank
        bank.addBranchToBank(self)
        
    def addAccountHolderToBranch(self,accountHolder):
        self.accounts.append(accountHolder)
        
    def addATMMachineToBranch(self,atm_machine):
        self.managed_atm.append(atm_machine)

class AtmMachine:
    def __init__(self, address, machine_id, bank, managed_branch, initial_amount=0):
        self.address = address
        self.machine_id = machine_id
        self.bank = bank
        self.managed_branch = managed_branch 
        bank.addATMMachineToBank(self)
        managed_branch.addATMMachineToBranch(self)

class AtmCard:
    pass

class Transaction:
    pass