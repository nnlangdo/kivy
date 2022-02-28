from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib import FigureCanvasKivyAgg 
import matplotlib.pyplot as plt 


x = [1, 2, 3, 4, 5]
y = [7, 12, 6, 15, 9]

plt.plot(x, y)
plt.ylabel("Y Axis")
plt.xlabel("X Axis")

class matty(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        box = self.ids.box
        box.add_widget(plt.gcf())

    def save_it(self):
        pass
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        Builder.load_file('mat_plotlib.kv')
        return matty()

MainApp().run()