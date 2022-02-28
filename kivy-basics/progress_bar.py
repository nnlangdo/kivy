from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('progress_bar.kv')

class MyLayout(Widget):
    def press_it(self):
        current = self.ids.my_progressbar.value
        if current ==1:
            current = 0
        current += .05
        self.ids.my_progressbar.value = current
        # update the label
        self.ids.my_label.text = f'{int(current*100)} progress'

class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__=='__main__':
    AwesomeApp().run()