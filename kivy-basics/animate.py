from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.animation import Animation


Builder.load_file('animate.kv')

class MyLayout(Widget):
    def animate_it(self, widget, *args):
        animate = Animation(
            background_color=(0, 0, 1, 1),
            duration=1,           
             )
        # do second animation
        animate += Animation(
        # opacity=0,
        # duration= .5
        size_hint = (1, 1)        
        )

        animate += Animation(
        size_hint = (.5, .5)        
        )

        animate += Animation(
        pos_hint = {'center_x': .1}        
        )
        animate += Animation(
        pos_hint = {'center_x': .5}        
        )
        animate.start(widget)
        
        animate.bind(on_complete = self.my_callback)

    def my_callback(self, *args):
        self.ids.my_label.text = "Wow Look At That!"



        

class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__=='__main__':
    AwesomeApp().run()