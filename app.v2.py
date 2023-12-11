# square.py

def calculate_square(number):
    return number ** 2


if __name__ == "__main__":

    num = float(input("Enter a number: "))
    
    result = calculate_square(num)
    print(f"The square of {num} is {result}")
