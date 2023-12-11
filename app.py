# square.py

def calculate_square(number):
    return number * number

def add(a,b):
    return a+b

if __name__ == "__main__":

    num = float(input("Enter a number: "))
    
    result = calculate_square(num)
    print(f"The square of {num} is {result}")
