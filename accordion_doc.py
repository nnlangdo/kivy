from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.app import App

class AccordionApp(App):
    def build(self):
        root = Accordion()

        item1 = AccordionItem(title='First Acc')
        accordion_text = "Kabhi Kabhi Mere dil me khayal atta hai........."
        item1.add_widget(Label(text=accordion_text))
        root.add_widget(item1)

        item2 = AccordionItem(title='Second Acc')
        item2.add_widget(Label(text='Second Accordion Text'))
        root.add_widget(item2)

        return root

if __name__=='__main__':
    AccordionApp().run()