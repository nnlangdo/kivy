from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('calc1.kv')
# Set window size
Window.size = (500,600)

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

    # create a button pressing function
    def button_press(self, button):
        # create a variable that contains whatever was in the text box
        prior = self.ids.calc_input.text
        # Test the error first
        if "Not Defined" in prior:
            prior = ''
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text= f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'
    # Create remove function
    def remove(self):
        prior = self.ids.calc_input.text
        # remove the last item in the textbox
        prior = prior[:-1]
        # output back to the textbox
        prior = self.ids.calc_input.text = prior
    # Create function to make text box positive or negative
    def pos_neg(self):
        prior = self.ids.calc_input.text
        # test to see if there is a - sign
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'
    # Create decimal function
    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split("+")
        if "+" in prior and "." not in num_list[-1]:
            # add a decimal to the end
            prior = f'{prior}.'
            # output back to the text box
            self.ids.calc_input.text = prior
        elif "." in prior:
            pass
        else:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior
    # Create addition function
    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}{sign}'

    def equals(self):
        prior = self.ids.calc_input.text
        # Error handling
        try:
            # Evaluate the math from the text box
            answer = eval(prior)
            # output the answer
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Not Defined"
    
    '''
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0.0
            # loop through our list
            for number in num_list:
                answer = answer + float(number)

            # print the answer in the text box
            self.ids.calc_input.text = str(answer)       
    '''

class CalculatorApp(App):
    def build(self):
        return MyLayout()

if __name__=='__main__':
    CalculatorApp().run()