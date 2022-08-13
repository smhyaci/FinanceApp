from kivy.config import Config
Config.set('graphics', 'window_state', 'maximized')

from kivy.uix.floatlayout import FloatLayout
from data_entry_panel.DataEntryPeer import DataEntryPeer
from graph_panel.GraphPeer import GraphPeer
from kivymd.app import MDApp

# creates the main window view
class PurchasePeerApp(MDApp):
    def build(self):
        #set color scheme for app
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Teal"
        return PurchasePeer()  

class PurchasePeer(FloatLayout):
    pass

if __name__ == "__main__":
    PurchasePeerApp().run()