import math
import matplotlib.pyplot as plt

def exec_calc():
    print("Operations Available: +, -, *, /, pow, sin, cos, tan, graph-curve")
    operator = input(">> ")
    isOperator = operator_check(operator)
    values_list = []
    if isOperator == True:
        if operator == '+':
            add(values_list)
        elif operator == '-':
            sub(values_list)
        elif operator == 'pow':
            pow(values_list)
        elif operator == '/':
            div(values_list)
        elif operator == '*':
            multi(values_list)
        elif operator == 'cos':
            cos(1)
        elif operator == 'sin':
            sin(1)
        elif operator == 'tan':
            tan(1)
        elif operator == 'graph-curve':
            graph_curve(1)
    else:
        print("Try Again")

def operator_check(operator):
    existing_operations = ['+', '-', '*', '/', 'pow', 'sin', 'cos', 'tan', 'graph-curve']
    i = 0
    isExistence = False
    for operation in existing_operations:
        
        if operator == operation:
            isExistence = True
            break
    return isExistence
    
def check_input(input):
    isInput = False
    try:
        value = float(input)
        ##it is an floating point value
        isInput = True
    except ValueError:
        ##its a string
        isInput = False
    return isInput   


def add(values_list):
    print("Selected (+)")
    print("Enter numbers to add!")
    print("To stop adding enter Q")
    exit_char = "Q"
    i = 0
    
    while True:
        num = input(">> ")
        if check_input(num) == False:
            if num.lower() == exit_char.lower():
                if len(values_list) > 1:
                    values_list.append("=")
                    print("You have decided to SUM")
                    break
                print("You have decided to LEAVE")
                break
            else:
                print(values_list)
                print("Try Again, enter a number")
        else:
            values_list.append(num)
            i = i + 1
    sum = 0.0
    for value in values_list:
        if value == "=":
            break
        sum = sum + float(value)
    sum_list = []
    for value in values_list:
        if value == "=":
            sum_list.pop()
            sum_list.append(value)
            break
        sum_list.append(value)
        sum_list.append("+")
        
    sum_list.append(str(sum))
    print(" ".join(sum_list))
    return
        
def sub(values_list):
    print("Selected (-)")
    print("Enter a number!")
    print("To subtracting enter Q")
    exit_str = "Q"
    values_list = []
    i = 0
    while True:
        num = input(">> ")
        check_input(num)
        if check_input(num) == False:
            if exit_str.lower() == num.lower():
                if len(values_list) > 1:

                    values_list.append("=")
                    print("You have decided to SUM")
                    break
                else:
                    print("You have decided to LEAVE")
        else:
            values_list.append(num)
            i = i + 1
    
    init = 0
    diff = 0.0
    for value in values_list:
        if init == 0:
            diff = float(value)
            init = 1
        else:
            if value == '=':
                break
            diff = diff - float(value)
    diff_list = []
    
    for value in values_list:
        if value == '=':
            diff_list.pop()
            diff_list.append(value)
            break
        diff_list.append(value)
        diff_list.append("-")
        
    diff_list.append(str(diff))
    print(" ".join(diff_list))
    return
            
            
            
def multi(values_list):
    print("Selected (*)")
    print("Enter a numbers: ")
    print("To quit enter Q")
    exit_char = "Q"
    values_list = []
    num = 0.0
    while True:
        num = input(">> ")
        if check_input(num) == False:
            if num == "q":
                if len(values_list) > 1:
                    values_list.append("=")
                break
            else:
                print("Try again, enter a number")
        else:
            values_list.append(num)
    
    sum = float(1)
    sum_list = []
    
    for value in values_list:
        if value == '=':
            break
        sum = sum * float(value)
    
    for value in values_list:
        if value == '=':
            sum_list.pop()
            sum_list.append("=")
            break
        sum_list.append(value)
        sum_list.append("*")
    
    sum_list.append(str(sum))
    print(" ".join(sum_list))
    return

def pow(values_list):
    print("Selected (pow)\nTo Quit or Sum press Q\nEnter a base number then exponent: ")
    values_list = []
    exit_char = "Q"
    i = 0
    
    while i < 2:
        num = input(">> ")
        if check_input(num) == False:
            if num.lower() == exit_char.lower():
                break
            else:
                print("Try again")
        else:
            values_list.append(num)
            i = i + 1
    values_list.append("=")
    
    init = 0
    sum = 1.0
    ##print(values_list)
    for value in values_list:
        if value == "=":
            break
        if init == 0:
            init = 1
            sum = float(value)
        else:
            sum = sum ** float(value)
            break
    
    sum_list = []
    for value in values_list:
        if value == "=":
            sum_list.pop()
            sum_list.append("=")
            break
        sum_list.append(value)
        sum_list.append("^")
    
    sum_list.append(str(sum))
    print(" ".join(sum_list))
    pass

def div(values_list):
    print("Selected (/) division\nEnter a number to divide!\nTo exit press Q")
    exit_char = "Q"
    values_list = []
    i = 0
    while i < 2:
        num = input(">> ")
        if check_input(num) == False:
            if num.lower() == exit_char.lower():
                print("You have decided to leave")
                return
        else:
            if float(num) == 0 and i == 1:
                print("Error: DIV WITH 0")
                return
            values_list.append(num)
            i = i + 1
    
    values_list.append("=")
    sum = 0.0
    init = 0
    for value in values_list:
        if value == "=":
            break
        
        if init == 0:
            init = 1
            sum = float(value)
        else:
            sum = sum/float(value)
    
    sum_list = []
    
    for value in values_list:
        if value == "=":
            sum_list.pop()
            sum_list.append("=")
            break
        
        sum_list.append(value)
        sum_list.append("/")
        
    sum_list.append(str(sum))
    print(" ".join(sum_list))    
    pass

def sin(value):
    print("Selected (sin)\nWrite in degrees")
    value = float(input("Sin"))
    radians = math.radians(value)
    sum = math.sin(radians)
    print(f"Sin({value}) = {sum}")
    #pi = 180 degrees, 1 radian = 180deg/pi
    return

def cos(value):
    print("Selected (cos)\nEnter value in degrees")
    value = float(input("Cos"))
    radians = math.radians(value)
    sum = math.cos(radians)
    print(f"Cos({value}) = {sum}")
    return

def tan(value):
    print("Selected (tan)\nEnter any value")
    value = input("Tan")
    radians = math.radians(value)
    sum = math.tan(radians)
    print(f"Tan({value}) = {sum}")
    pass


def graph_curve(linear_curve):
    print("Selected (graph-curve)")
    k_value = float(input("You will have to first choose x value: "))
    m_value = float(input("You will have to now choose y value: "))
    x_list = []
    y_list = []
    i = -10
    #y = kx + m
    x_value = 0.0
    y_value = 0.0
    while i < 10:
         x_value = k_value * i
         x_list.append(x_value)
         y_value = k_value * i + m_value
         y_list.append(y_value)
         i = i + 1
    plt.title("Linear Curve")
    plt.plot(x_list, y_list)
    plt.show()
    return

if __name__ == '__main__':
    print("Welcome to Calculator!\n")
    while True:
        exec_calc()