
# TODO: clean up import statements
from kivy.app import App
from TransactionEntryPanel import TransactionEntryPanel


class FinanceApp(App):
    def build(self):
        return TransactionEntryPanel()  
    
    
if __name__ == "__main__":
    FinanceApp().run()