from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

class LoginUI(Screen):
    pass

class RegisterUI(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('multiscreen.kv')

class LoginApp(App):
    def build(self):
        return kv

if __name__=='__main__':
    login = LoginApp()
    Window.size=(397,650)
    login.run()