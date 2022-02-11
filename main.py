from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase

screen_helper = """
ScreenManager:
    LoadScreen:
    MainScreen:
<LoadScreen>:
    name: 'Load'
    MDRectangleFlatButton:
        text: 'Main'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: root.manager.current = 'Main'
    Image:
        source:"logo.png"
        pos_hint: {'center_x':0.5,'center_y':0.8}


<MainScreen>:
    name: 'Main'
    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title:'Crpytop'
        MDTabs:
            id:tabs
            on_tab_switch: app.on_tab_switch(*args)

<Tab>:
    MDLabel:
        id:label
        text:"test" 
        halign:"center"
"""


class LoadScreen(Screen):
    pass


class MainScreen(Screen):
    pass

class Tab(FloatLayout,MDTabsBase):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(LoadScreen(name='Load'))
sm.add_widget(MainScreen(name='Main'))


class DemoApp(MDApp):

    def build(self):
        screen = Screen()
        self.help_str = Builder.load_string(screen_helper)

        screen.add_widget(self.help_str)
        return screen
    def on_start(self):
        self.help_str.get_screen("Main").ids.tabs.add_widget(Tab(text = "NEWS"))
        self.help_str.get_screen("Main").ids.tabs.add_widget(Tab(text = "PREDICTOR"))
        self.help_str.get_screen("Main").ids.tabs.add_widget(Tab(text = "CRYPTO-DICTIONARY"))

    def on_tab_switch(self,instance_tabs,instance_tab,instance_tab_label,tab_text):
        instance_tab.ids.label.text = 'Main'




if __name__ == '__main__':
    DemoApp().run()