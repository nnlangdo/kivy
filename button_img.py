from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('button_img.kv')

class MyLayout(Widget):
    def hello_on(self):
        
        self.ids.my_image.source = "/home/narendra/Pictures/login2.jpg"

    def hello_off(self):
        self.ids.my_image.source = "/home/narendra/Pictures/login1.jpg"
        self.ids.my_label.text = "You pressed me!"


class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__=='__main__':
    AwesomeApp().run()