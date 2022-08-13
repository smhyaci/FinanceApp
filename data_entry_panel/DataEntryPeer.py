import re
import datetime
from kivymd.toast import toast
from database.DataLayer import DataLayer
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import RectangularElevationBehavior



class MD3Card(MDCard, RectangularElevationBehavior):
    '''Implements a material design v3 card.'''
    pass

class DataEntryPeer(MDCard, RectangularElevationBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db_connection = DataLayer()
    
    def is_valid_date_format(self, date):
        try:
            datetime.datetime.strptime(date.strip(), '%m/%d/%Y')
            self.ids.date_field.helper_text = "Valid date"
            return True
        except ValueError:
            self.ids.date_field.helper_text = "If blank/invalid defaults to today"
            return False
        
    def is_valid_category_format(self, category):
        valid_category_format = re.compile(r'#\w+\b')
        user_input_results = valid_category_format.findall(category)
        if user_input_results is None:
            self.ids.category_field.helper_text = "Invalid category format"
        elif len(user_input_results) == 0:
            self.ids.category_field.helper_text = "Use #<category name>"
        else:
            self.ids.category_field.helper_text = "Valid category"
            return True
        return False
            
    def is_valid_amount(self, amount):
        valid_price_format = re.compile(r'\d*\.?\d{0,2}?')
        user_input_results = valid_price_format.fullmatch(amount.strip())
        if user_input_results is None or not user_input_results.string:
            self.ids.amount_field.helper_text = "Invalid amount"
            return False
        else:
            self.ids.amount_field.helper_text = "Valid Amount"
            return True
        
    def is_valid_transaction_type(self, type):
        type = type.strip().lower()
        if type == "charge":
            self.ids.transaction_field.helper_text = "Valid Transaction Type"
        elif type == "deposit":
            self.ids.transaction_field.helper_text = "Valid Transaction Type"
        else:
            self.ids.transaction_field.helper_text = "options: charge or deposit" 
            return False
        return True           
        
    def submit_new_transaction(self):     
        #adds transaction to transactions table in purchasepeer_db
        insert_statement = (
            "INSERT INTO transactions (date, category, amount, description, type)"
            "VALUES (?, ?, ?, ?, ?)"
            )
        try:
            data = (
                datetime.datetime.strptime(self.get_date_field(),'%m/%d/%Y').strftime('%Y/%m/%d'),
                self.get_category_field(),
                self.get_amount_field(),
                self.get_description_field(),
                self.get_transaction_field()
            )       
            self.db_connection.execute(insert_statement, data)
            toast("Transaction added!")
        except BaseException as exception:
            print(exception)
            toast("Invalid data entry. Transaction not added.")
        
        self.clear_all_fields()
        

    def get_date_field(self):
        #defaulting date to date during time of entry
        if not self.ids.date_field.text.strip():
            return datetime.datetime.now().strftime("%m/%d/%Y")
        else:
            return self.ids.date_field.text.strip()
    
    def get_category_field(self):
        if not self.ids.category_field.text:
            return None
        return self.ids.category_field.text.replace("#","").strip()
    
    def get_amount_field(self):
        if not self.is_valid_amount(self.ids.amount_field.text):
            raise Exception("No amount detected")
        elif self.get_transaction_field() == "charge":
            return "-" + self.ids.amount_field.text.strip()
        else:
            return self.ids.amount_field.text.strip()
        
    def get_description_field(self):
        if not self.ids.description_field.text:
            return None
        return self.ids.description_field.text.strip()
    
    def get_transaction_field(self):
        if not self.is_valid_transaction_type(self.ids.transaction_field.text):
            raise Exception("No transaction type detected")
        return self.ids.transaction_field.text.strip()
    
    def clear_date_field(self):
        self.ids.date_field.text = ""
    
    def clear_category_field(self):
        self.ids.category_field.text = ""
    
    def clear_amount_field(self):
        self.ids.amount_field.text = ""
    
    def clear_transaction_field(self):
        self.ids.transaction_field.text = ""
        
    def clear_description_field(self):
        self.ids.description_field.text = ""
        
    def clear_all_fields(self):
        self.clear_date_field()
        self.clear_category_field()
        self.clear_amount_field()
        self.clear_description_field()
        self.clear_transaction_field()
        
        