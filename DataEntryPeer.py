from datetime import datetime
from kivymd.uix.card import MDCard
from kivymd.uix.segmentedcontrol.segmentedcontrol  import MDSegmentedControl, MDSegmentedControlItem
from kivymd.uix.behaviors import RectangularElevationBehavior
import re
import datetime


class MD3Card(MDCard, RectangularElevationBehavior):
    '''Implements a material design v3 card.'''
    pass

class DataEntryPeer(MDCard, RectangularElevationBehavior):
    def is_valid_date_format(self, date):
        try:
            datetime.datetime.strptime(date, '%d/%m/%Y')
            self.ids.date_field.helper_text = "Valid date"
        except ValueError:
            self.ids.date_field.helper_text = "Invalid MM/DD/YYYY format"
            
    def is_valid_category_format(self, category):
        valid_category_format = re.compile(r'#\w+\b')
        user_input_results = valid_category_format.findall(category)
        print(user_input_results)
        if user_input_results is None:
            self.ids.category_field.helper_text = "Invalid category format"
        elif len(user_input_results) == 0:
            self.ids.category_field.helper_text = "Use #<category name>"
        else:
            self.ids.category_field.helper_text = "Valid category"
            
    def is_valid_amount(self, amount):
        valid_price_format = re.compile(r'\d*\.?\d{0,2}?')
        user_input_results = valid_price_format.fullmatch(amount)
        print(user_input_results)
        if user_input_results is None or not user_input_results.string:
            self.ids.amount_field.helper_text = "Invalid amount"
        else:
            self.ids.amount_field.helper_text = "Valid Amount"
        
    def is_valid_transaction_type(self, type):
        type = type.lower()
        if type == "charge":
            self.ids.transaction_field.helper_text = "Valid Transaction Type"
        elif type == "deposit":
            self.ids.transaction_field.helper_text = "Valid Transaction Type"
        else:
            self.ids.transaction_field.helper_text = "options: charge or deposit"    
        
    def test(self):
        print("Functioning Button")
