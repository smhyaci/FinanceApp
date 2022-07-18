
# TODO: clean up import statements
from kivymd.app import MDApp
from DataEntryPanel import DataEntryPanel



# creates the main window view
class FinanceApp(MDApp):
    def build(self):
        
        #set color scheme for app
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        
        return DataEntryPanel()  
    
    
if __name__ == "__main__":
    FinanceApp().run()