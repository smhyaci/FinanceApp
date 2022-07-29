from abc import ABC, abstractmethod
from doctest import debug_script
from pydoc import describe

class Transaction(ABC):
    
    def __init__(self, date_added, expense_category, amount, description=''):
        self.date_added = date_added
        self.expense_category = expense_category
        self.amount = amount
        self.description = description
        
        
    def get_date_added(self):
        return self.date_added
    
    
    def set_date_added(self, new_date):
        self.date_added = new_date
    
        
    def get_expense_category(self):
        return self.expense_category
    
    
    def set_expense_category(self, new_expense_category):
        self.expense_category = new_expense_category
    
    
    def get_description(self):
        return self.description
    
    
    def set_description(self, new_description):
        self.description = new_description
    
    
    @abstractmethod
    def get_amount(self):
        pass
    
    
    @abstractmethod
    def set_amount(self, new_amount):
        pass
    

class Charge(Transaction):
    
    def __init__(self, date_added, expense_category, amount, description=None):
        super().__init__(date_added, expense_category, amount, description)
        
    
    def get_amount(self):
        return -self.amount
    
    
    def set_amount(self, new_amount):
        self.amount = -new_amount
    

class Deposit(Transaction):
    
    def __init__(self, date_added, expense_category, amount, description=''):
        super().__init__(date_added, expense_category, amount, description)
        
    
    def get_amount(self):
        return self.amount
    
    
    def set_amount(self, new_amount):
        self.amount = new_amount
    