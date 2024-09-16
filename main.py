
from calculator import Calculator

def main():
    
    calc = Calculator()
    
    print( calc.calculate(10, 5, '+'))  
    print( calc.calculate(10, 5, '-'))  
    print( calc.calculate(10, 5, '*'))  
    print(calc.calculate(10, 5, '/'))  
    

if __name__ == "__main__":
    main()
