from kivymd.uix.card import MDCard
from kivymd.uix.textfield import MDTextField
from kivymd.app import MDApp
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from matplotlib import pyplot as plt

CENTER = 0.5
DEFAULT_FILTER_PANEL_SIZE_X = 0.3
FILTER_PANEL_RANGE_SIZE_X = 0.5

class MD3Card(MDCard, RectangularElevationBehavior):
    '''Implements a material design v3 card.'''
    pass


class GraphPeer(MDCard, RectangularElevationBehavior):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # kivy built-in function to handle operations after UI is rendered

    def on_kv_post(self, base_widget):
        
        x  = y = []
       

        self.display_filter_setup()
        # making graph background transparent
        plt.rcParams.update({
            "figure.facecolor":  (0, 0, 0, 0),
            "axes.facecolor":    (0, 0, 0, 0),
            "savefig.facecolor": (0, 0, 0, 0),
        })
        plt.plot(x, y)

        self.graph = self.ids.graph
        self.graph.add_widget(FigureCanvasKivyAgg(plt.gcf()))

    def display_filter_setup(self):
        # handles case when user has not activated the segment bar, but the segment bar has price highlighted
        # kivy has no current way to have segment bar start with no segment highlighted
        try:
            active_filter = self.ids.filter_type.current_active_segment.text.lower()
            self.ids.filter_panel.size_hint_x = DEFAULT_FILTER_PANEL_SIZE_X
            self.ids.filter_panel.clear_widgets()
        except(AttributeError):
            active_filter = "cost"

        if active_filter == "cost":
            filter_input = MDTextField(
                hint_text='Filter: Amount', icon_right='cash')
            filter_input.pos_hint = {"center_x": CENTER, }
            self.ids.filter_panel.add_widget(filter_input)
            
        elif active_filter == "cost(range)":
            filter_low = MDTextField(
                hint_text='Filter: Amount Low', icon_right='cash')
            filter_low.pos_hint = {"center_x": CENTER, }
            
            filter_high = MDTextField(
                hint_text='Filter: Amount High', icon_right='cash')
            filter_high.pos_hint = {"center_x": CENTER, }
        
            self.ids.filter_panel.size_hint_x = FILTER_PANEL_RANGE_SIZE_X
            self.ids.filter_panel.add_widget(filter_low)
            self.ids.filter_panel.add_widget(filter_high)
        
        elif active_filter == "date":
            filter_input = MDTextField(
                hint_text='Filter: MM/DD/YYYY', icon_right='calendar-today')
            self.ids.filter_panel.add_widget(filter_input)
            
        elif active_filter == "date(range)":
            filter_start = MDTextField(
                hint_text='Filter: Start Date', icon_right='calendar-today')
            filter_start.pos_hint = {"center_x": CENTER, }
            
            filter_end = MDTextField(
                hint_text='Filter: End Date', icon_right='calendar-today')
            filter_end.pos_hint = {"center_x": CENTER, }
            
            self.ids.filter_panel.size_hint_x = FILTER_PANEL_RANGE_SIZE_X
            self.ids.filter_panel.add_widget(filter_start)
            self.ids.filter_panel.add_widget(filter_end)
        
        elif active_filter == "category":
            filter_input = MDTextField(hint_text='Filter: #<category_name>')
            filter_input.pos_hint = {"center_x": CENTER, }
            self.ids.filter_panel.add_widget(filter_input) 
            
        else:
            filter_input = MDTextField(hint_text='Filter: Charge/Deposit')
            filter_input.pos_hint = {"center_x": CENTER, }
            self.ids.filter_panel.add_widget(filter_input)
       
    