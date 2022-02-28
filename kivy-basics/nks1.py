# coloring background and text
# default attribute modification
# applying builder method for kv file very usefull hack
# overwriting the default attr for a perticular field
# Label color only be used with canvas.before 


import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('my.kv')

class MyLayout(Widget):
    pass

class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__=='__main__':
    AwesomeApp().run()