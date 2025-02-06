import math
import numpy
import keyboard
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
"""
Bu kütüphane beni aşar
"""
PI = numpy.pi
E = numpy.e

def Add(a,b):
    return numpy.add(a,b)

def Subtrack(a,b):
    return numpy.subtract(a,b)

def Multiply(a,b):
    return numpy.multiply(a,b)

def Divide(a,b):
    return numpy.divide(a,b)

def Square(a):
    return numpy.sqrt(a)

def Power(a,b): 
    return numpy.power(a,b)

def Log(a,b):
    return numpy.log(a) /numpy.log(b)

def Sin(a):
    return numpy.sin(a)

def Cos(a):
    return numpy.cos(a)

def Tan(a):
        return numpy.tan(a)

def Cot(a):
        return numpy.cot(a)

def Factorial(a):
    try :
        return math.factorial(a)
    except Exception as  e:
        print(f"Hata {e}")
        return None

class Aplication(App):
    def build(self): 
        button_texts = ["0","1","2","3","4","5","6","7","8","9","=","x","sin","cos","tan","cot","fact","log","pwr","sqr","-","+","/","."]
        self.label = Label(text="Metin girin ve Butona tıklayın")
        self.text_ınput= TextInput(hint_text = "Buraya bişeyler yaz")
        button = Button(text = "Butona tıkla")
        button.bind(on_press = self.show_text)
        
        layout =  BoxLayout(orientation="vertical")
        layout.add_widget(self.label)
        layout.add_widget(button)
        layout.add_widget(self.text_ınput)
        return layout
    
    def show_text(self,instance):
        input = self.text_ınput.text 
        self.label.text = f"Girilen yazı {input}"
        
     

if __name__ == "__main__":
    Aplication().run()