# TODO: put all .kv files into a folder or package and access it that way
from kivymd.app import MDApp
from PurchasePeer import PurchasePeer


# creates the main window view
class PurchasePeerApp(MDApp):
    def build(self):
        #set color scheme for app
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        return PurchasePeer()  
    
    
if __name__ == "__main__":
    PurchasePeerApp().run()