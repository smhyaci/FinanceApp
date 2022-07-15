
# TODO: clean up import statements
from kivy.app import App
from TransactionEntryPanel import TransactionEntryPanel
from kivy.core.window import Window


main_window_bg_color = (190/255, 190/255 , 190/255, 1)

# creates the main window view
class FinanceApp(App):
    def build(self):
        #set color of background window
        Window.clearcolor =  main_window_bg_color
        return TransactionEntryPanel()  
    
    
if __name__ == "__main__":
    FinanceApp().run()