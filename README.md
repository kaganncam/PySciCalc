# PySciCalc


This is a simple scientific calculator application built using the **Kivy framework** and **Python**. It performs basic arithmetic operations as well as advanced mathematical functions like trigonometric functions, logarithms, factorials, and more.

## Features
- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, division.
- **Advanced Functions**: Sine, cosine, tangent, cotangent, logarithms, power, square root, and factorial.
- **History Tracking**: Keeps track of previous operations and their results.
- **Responsive UI**: Interactive user interface designed with Kivy's GridLayout.

## Prerequisites
- Python 3.x
- Kivy library
- Numpy and math libraries

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/kivy-calculator.git
## Install dependencies
 ```
pip install kivy
pip install numpy
```
## How It Works

- The calculator provides a simple UI with buttons for numbers, operations, and functions.
- When a button is pressed, the corresponding function or operator is added to the input string.
- Pressing = will evaluate the result of the expression and display it.
- Operations are handled via the Calculator class, which includes static methods for performing mathematical operations.
- The results of previous operations are stored in a history list, and you can track the calculation history.
## Example Functions
- Addition: ```2 + 3```
- Sin: ```sin(30)```
- Logarithm: ```log(10, 2)```
- Factorial: ```fact(5)```

