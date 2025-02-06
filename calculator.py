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
        result =  numpy.sin(a)
        Calculator.history.append(f"sin({a}) = {result}")
        return result
    @staticmethod
    def Cos(a):
        result =  numpy.cos(a)
        Calculator.history.append(f"cos({a}) = {result}")
        return result
    @staticmethod
    def Tan(a):
        result =  numpy.tan(a)
        Calculator.history.append(f"tan({a}) = {result}")
        return result
    @staticmethod
    def Cot(a):
        result =  1/ numpy.tan(a) 
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
        self.operation = ""
        self.c = Calculator()
        self.numbers = []
        self.result = ""
        button_texts = ["0","1","2","3","4","5","6","7","8","9","=","x","sin","cos","tan","cot","fact","log","pwr","sqr","-","+","/","."]
        layout = GridLayout(cols=6,spacing = [10,10])
        self.label = Label(text = f"Sonuç: {self.result}",font_size = 20)        
        for button_name in button_texts:
            self.button = Button(text = f"{button_name}",font_size = 40,)
            self.button.bind(on_press = self.button_bind)
            layout.add_widget(self.button)
        layout.add_widget(self.label)
        
        return layout
        
    def button_bind(self,instance):
        
        if instance.text in ["1","2","3","4","5","6","7","8","9","."] and instance not in ["sin","cos","tan","cot","fact","log","pwr","sqr"]:
                                    
            self.result += instance.text 
            self.label.text = f"Sonuç = {self.result}"     
        if instance.text in ["x","+","-","/"] and self.result[-1] not in ["1","2","3","4","5","6","7","8","9",".","sin","cos","tan","cot","fact","log","pwr","sqr"]:
            self.operation = instance.text
            self.numbers.append(float(self.result))
            self.numbers.append(operation)
            self.label.text = f"Sonuç {self.result} {instance.text}" 
            
        
        if self.operation is not "" and instance.text == "=" and len(self.numbers) == 3:
            a = float(self.numbers[0])
            b = float(self.numbers[2])
            self.operation = self.numbers[1]
            if self.operation =="+":
                self.result = str(self.c.Add(a,b))
                self.label.text = f"Sonuç {self.result}"
            elif self.operation == "-":
                self.result = str(self.c.Subtract(a,b))
                self.label.text = f"Sonuç {self.result}"
            elif self.operation == "x":
                self.result = str(self.c.Multiply(a,b))
                self.label.text = f"Sonuç {self.result}"
            elif self.operation == "/":
                self.result = str(self.c.Divide(a,b))
                self.label.text = f"Sonuç {self.result}"

if __name__ == "__main__":
    Application().run()

