from kivy.lang import Builder
from kivymd.app import MDApp
from matplotlib.pyplot import cla

class MainApp(MDApp):
    some_text = "Hello World!"
    our_list = ["John", "Marry", "Tina"]
    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('code.kv')

MainApp().run()