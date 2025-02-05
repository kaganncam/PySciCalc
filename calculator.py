import math
import numpy
from kivy.app import App
from kivy.uix.label import Label
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
          return  Label(text = "Hello  World")
Myapp = Aplication()
Myapp.run()