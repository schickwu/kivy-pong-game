import numpy as np
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import BooleanProperty
import random
#from kivy.uix.canvas import canvas


class MenuWidget(BoxLayout):
    start_enabled = BooleanProperty(False)
    level = random.randint(1, 3)
    print(level)

    def on_text_validate(self,textval):
        self.textinput= textval.text
        print(self.textinput)

    def on_button_click_e(self, clickfune):
        print("clicked"+clickfune.state)
        self.start_enabled = True
        self.level = 1
        print(self.level)

    def on_button_click_m(self, clickfunm):
        print("clicked"+clickfunm.state)
        self.start_enabled = True
        self.level = 2
        print(self.level)

    def on_button_click_d(self, clickfund):
        print("clicked"+clickfund.state)
        self.start_enabled = True
        self.level = 3
    def on_toggle_click(self,togglefun):
        print("activated"+togglefun.state)




