from unittest import result
from kivymd.uix.card import MDCard
import re


class DataEntryPeer(MDCard):
    def is_valid_amount(self, amount):
        valid_price_format = re.compile(r'\d*\.?\d{0,2}?')
        user_input_results = valid_price_format.fullmatch(amount)
        print(user_input_results)
        if user_input_results is None or not user_input_results.string:
            self.ids.amount_field.helper_text = "Please enter a valid amount"
        else:
            self.ids.amount_field.helper_text = "Good"
            
