import math
import numpy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
"""
Bu kütüphane beni aşar
"""
PI = numpy.pi
E = numpy.e
class Calculator():
    history = []
    @staticmethod
    def Radyan(a):
        return numpy.radians(a)
    @staticmethod
    def Add(a,b):
        result =  numpy.add(a,b)
        Calculator.history.append(f"{a} + {b} = {result}")
        return result
    @staticmethod
    def Subtract(a,b):
        result =  numpy.subtract(a,b)
        Calculator.history.append(f"{a} - {b} = {result}")
        return result
    @staticmethod
    def Multiply(a,b):
        result =  numpy.multiply(a,b)
        Calculator.history.append(f"{a} * {b} = {result}")
        return result
    @staticmethod
    def Divide(a,b):
        result =  numpy.divide(a,b)
        Calculator.history.append(f"{a} / {b} = {result}")
        return result
    @staticmethod
    def Square(a):
        result =  numpy.sqrt(a)
        Calculator.history.append(f"{a}^2 = {result}")
        return result
    @staticmethod
    def Power(a,b): 
        result =  numpy.power(a,b)
        Calculator.history.append(f"{a}^{b} = {result}")
        return result
    @staticmethod
    def Log(a,b):
        result =  numpy.log(a) /numpy.log(b)

        return result
    @staticmethod
    def Sin(a):
        result =  numpy.sin(Calculator.Radyan(a))
        Calculator.history.append(f"sin({a}) = {result}")
        return result
    @staticmethod
    def Cos(a):
        result =  numpy.cos(Calculator.Radyan(a))
        Calculator.history.append(f"cos({a}) = {result}")
        return result
    @staticmethod
    def Tan(a):
        result =  numpy.tan(Calculator.Radyan(a))
        Calculator.history.append(f"tan({a}) = {result}")
        return result
    @staticmethod
    def Cot(a):
        result =  1/ numpy.tan(Calculator.Radyan(a)) 
        Calculator.history.append(f"cot({a}) = {result}")
        return result
    @staticmethod
    def Factorial(a):
        try :
            result =  math.factorial(a)
            Calculator.history.append(f"({a}!) = {result}")
            return result
        except Exception as  e:
            print(f"Hata {e}")
            return None
    
class Application(App):
    def build(self): 
        self.result = ""
        button_texts = [
            "0","1","2","3","4","5","6","7","8","9"
            ,"=","*","sin","cos","tan","cot","fact","log","pwr","sqr"
            ,"-","+","/","."
        ]
        layout = GridLayout(cols=6,spacing = [10,10])
        self.label = Label(text = f"Sonuç: {self.result}",font_size = 20)        
        for button_name in button_texts:
            self.button = Button(text = f"{button_name}",font_size = 40,)
            self.button.bind(on_press = self.button_bind)
            layout.add_widget(self.button)
        layout.add_widget(self.label)
        
        return layout
        
    def button_bind(self,instance):
        key = instance.text 
        if key == "=":
            self.calculate_results()
        else:
             if key in ["-","+","/","*"]:
                self.result += f" {key} "
             elif key in ["sin","cos","tan","cot","fact","log","pwr","sqr"]:
                self.result = f"{key}({self.result})"
                self.label.text = f"Result: {key}({self.result})"
             else:
                self.result += key

            
            
             self.label.text = f"Result: {self.result}"
    def calculate_results(self):
        try:
            result = eval((self.result),{"__builtins__":None},{"sin": Calculator.Sin, "cos":Calculator.Cos ,
                 "tan":Calculator.Tan , "sqrt":Calculator.Square ,"cot":Calculator.Cot ,"fact":Calculator.Factorial 
                 ,"log":Calculator.Log ,"pwr":Calculator.Power,"sqr":Calculator.Square})
            self.label.text = f"Result: {result}"
            self.result = str(result)
        except Exception as e:
            print(f"Eror: {e}")
            self.result = ""
            self.label.text = "Error"
if __name__ == "__main__":
    Application().run()

