from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen


# Define our different screens

class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('multiscreen.kv')

class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (1, 0, 1, 1)
        return kv 

if __name__=='__main__':
    AwesomeApp().run()