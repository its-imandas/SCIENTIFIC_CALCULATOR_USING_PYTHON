import sympy as sp
import math
import statistics
from scipy.stats import norm, binom

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def sine(x):
    return sp.sin(sp.rad(x))

def cosine(x):
    return sp.cos(sp.rad(x))

def tangent(x):
    return sp.tan(sp.rad(x))

def cotangent(x):
    return 1 / sp.tan(sp.rad(x))

def secant(x):
    return 1 / sp.cos(sp.rad(x))

def cosecant(x):
    return 1 / sp.sin(sp.rad(x))

def exponential(x):
    return sp.exp(x)

def logarithm(x, base):
    return sp.log(x, base)

def lcm(x, y):
    return x * y // sp.gcd(x, y)

def hcf(x, y):
    return sp.gcd(x, y)

def indefinite_integral(expression):
    integral_expr = sp.integrate(expression, sp.Symbol('x'))
    return integral_expr

def definite_integral(expression, a, b):
    integral_expr = sp.integrate(expression, (sp.Symbol('x'), a, b))
    return integral_expr

def derivative(expression):
    derivative_expr = sp.diff(expression, sp.Symbol('x'))
    return derivative_expr

def definite_derivative(expression, a, b):
    derivative_expr = sp.diff(expression, sp.Symbol('x'))
    result = derivative_expr.subs(sp.Symbol('x'), b) - derivative_expr.subs(sp.Symbol('x'), a)
    return result

def decimal_to_binary(n):
    return bin(n)[2:]

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def binary_to_octal(binary_str):
    decimal_num = binary_to_decimal(binary_str)
    return oct(decimal_num)[2:]

def binary_to_hexadecimal(binary_str):
    decimal_num = binary_to_decimal(binary_str)
    return hex(decimal_num)[2:]

def octal_to_binary(octal_str):
    decimal_num = int(octal_str, 8)
    return bin(decimal_num)[2:]

def hexadecimal_to_binary(hexadecimal_str):
    decimal_num = int(hexadecimal_str, 16)
    return bin(decimal_num)[2:]

def octal_to_hexadecimal(octal_str):
    decimal_num = int(octal_str, 8)
    return hex(decimal_num)[2:]

def hexadecimal_to_octal(hexadecimal_str):
    decimal_num = int(hexadecimal_str, 16)
    return oct(decimal_num)[2:]

def calculate_median(data):
    return statistics.median(data)

def calculate_mode(data):
    return statistics.mode(data)

def calculate_correlation(data1, data2):
    return statistics.correlation(data1, data2)

def calculate_mean(data):
    return statistics.mean(data)

def calculate_variance(data):
    return statistics.variance(data)

def calculate_standard_deviation(data):
    return statistics.stdev(data)

def calculate_summation(data):
    return sum(data)

def calculate_permutation(n, r):
    return math.perm(n, r)

def calculate_combination(n, r):
    return math.comb(n, r)

def calculate_probability_normal(x, mean, std_dev):
    return norm.pdf(x, mean, std_dev)

def calculate_probability_binomial(x, n, p):
    return binom.pmf(x, n, p)

def main():
    while True:
        print("Scientific Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Sine")
        print("6. Cosine")
        print("7. Tangent")
        print("8. Cotangent")
        print("9. Secant")
        print("10. Cosecant")
        print("11. Exponential")
        print("12. Logarithm")
        print("13. LCM")
        print("14. HCF")
        print("15. Indefinite Integral")
        print("16. Definite Integral")
        print("17. Derivative")
        print("18. Definite Derivative")
        print("19. Decimal to Binary")
        print("20. Binary to Decimal")
        print("21. Binary to Octal")
        print("22. Binary to Hexadecimal")
        print("23. Octal to Binary")
        print("24. Hexadecimal to Binary")
        print("25. Octal to Hexadecimal")
        print("26. Hexadecimal to Octal")
        print("27. Calculate Median")
        print("28. Calculate Mode")
        print("29. Calculate Correlations")
        print("30. Calculate Mean")
        print("31. Calculate Variance")
        print("32. Calculate Standard Deviation")
        print("33. Calculate Summation")
        print("34. Calculate Permutation")
        print("35. Calculate Combination")
        print("36. Calculate Probability (Normal Distribution)")
        print("37. Calculate Probability (Binomial Distribution)")
        print("38. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 38:
            break

        if choice >= 1 and choice <= 12:
            x_value = float(input("Enter first operand: "))
            if choice != 11 and choice != 12:
                y_value = float(input("Enter second operand: "))
        
        if choice == 1:
            print("Result:", add(x_value, y_value))
        elif choice == 2:
            print("Result:", subtract(x_value, y_value))
        elif choice == 3:
            print("Result:", multiply(x_value, y_value))
        elif choice == 4:
            print("Result:", divide(x_value, y_value))
        elif choice == 5:
            print("Result:", sine(x_value))
        elif choice == 6:
            print("Result:", cosine(x_value))
        elif choice == 7:
            print("Result:", tangent(x_value))
        elif choice == 8:
            print("Result:", cotangent(x_value))
        elif choice == 9:
            print("Result:", secant(x_value))
        elif choice == 10:
            print("Result:", cosecant(x_value))
        elif choice == 11:
            print("Result:", exponential(x_value))
        elif choice == 12:
            base = float(input("Enter the base for logarithm: "))
            print("Result:", logarithm(x_value, base))
        elif choice == 13:
            y_value = int(input("Enter second operand: "))
            print("Result:", lcm(x_value, y_value))
        elif choice == 14:
            y_value = int(input("Enter second operand: "))
            print("Result:", hcf(x_value, y_value))
        elif choice == 15:
            expression = sp.sympify(input("Enter the expression for indefinite integral: "))
            result = indefinite_integral(expression)
            print("Indefinite Integral:", result)
        elif choice == 16:
            expression = sp.sympify(input("Enter the expression for integral: "))
            a = float(input("Enter the lower limit: "))
            b = float(input("Enter the upper limit: "))
            result = definite_integral(expression, a, b)
            print("Definite Integral:", result)
        elif choice == 17:
            expression = sp.sympify(input("Enter the expression for derivative: "))
            result = derivative(expression)
            print("Derivative:", result)
        elif choice == 18:
            expression = sp.sympify(input("Enter the expression for derivative: "))
            a = float(input("Enter the lower limit: "))
            b = float(input("Enter the upper limit: "))
            result = definite_derivative(expression, a, b)
            print("Definite Derivative:", result)
        elif choice == 19:
            decimal_num = int(input("Enter a decimal number: "))
            binary_result = decimal_to_binary(decimal_num)
            print("Binary:", binary_result)
        elif choice == 20:
            binary_str = input("Enter a binary number: ")
            decimal_result = binary_to_decimal(binary_str)
            print("Decimal:", decimal_result)
        elif choice == 21:
            binary_str = input("Enter a binary number: ")
            octal_result = binary_to_octal(binary_str)
            print("Octal:", octal_result)
        elif choice == 22:
            binary_str = input("Enter a binary number: ")
            hexadecimal_result = binary_to_hexadecimal(binary_str)
            print("Hexadecimal:", hexadecimal_result)
        elif choice == 23:
            octal_str = input("Enter an octal number: ")
            binary_result = octal_to_binary(octal_str)
            print("Binary:", binary_result)
        elif choice == 24:
            hexadecimal_str = input("Enter a hexadecimal number: ")
            binary_result = hexadecimal_to_binary(hexadecimal_str)
            print("Binary:", binary_result)
        elif choice == 25:
            octal_str = input("Enter an octal number: ")
            hexadecimal_result = octal_to_hexadecimal(octal_str)
            print("Hexadecimal:", hexadecimal_result)
        elif choice == 26:
            hexadecimal_str = input("Enter a hexadecimal number: ")
            octal_result = hexadecimal_to_octal(hexadecimal_str)
            print("Octal:", octal_result)
        elif choice == 27:
            data = input("Enter data values separated by spaces: ").split()
            data = [float(x) for x in data]
            result = calculate_median(data)
            print("Median:", result)
        elif choice == 28:
            data = input("Enter data values separated by spaces: ").split()
            data = [float(x) for x in data]
            result = calculate_mode(data)
            print("Mode:", result)
        elif choice == 29:
            data1 = input("Enter data values for the first variable separated by spaces: ").split()
            data1 = [float(x) for x in data1]
            data2 = input("Enter data values for the second variable separated by spaces: ").split()
            data2 = [float(x) for x in data2]
            result = calculate_correlation(data1, data2)
            print("Correlation:", result)
        elif choice == 30:
            data = input("Enter data values separated by spaces: ").split()
            data = [float(x) for x in data]
            result = calculate_mean(data)
            print("Mean:", result)
        elif choice == 31:
            data = input("Enter data values separated by spaces: ").split()
            data = [float(x) for x in data]
            result = calculate_variance(data)
            print("Variance:", result)
        elif choice == 32:
            data = input("Enter data values separated by spaces: ").split()
            data = [float(x) for x in data]
            result = calculate_standard_deviation(data)
            print("Standard Deviation:", result)
        elif choice == 33:
            data = input("Enter data values separated by spaces: ").split()
            data = [float(x) for x in data]
            result = calculate_summation(data)
            print("Summation:", result)
        elif choice == 34:
            n = int(input("Enter the value of n: "))
            r = int(input("Enter the value of r: "))
            result = calculate_permutation(n, r)
            print("Permutation:", result)
        elif choice == 35:
            n = int(input("Enter the value of n: "))
            r = int(input("Enter the value of r: "))
            result = calculate_combination(n, r)
            print("Combination:", result)
        elif choice == 36:
            x_value = float(input("Enter x value: "))
            mean = float(input("Enter mean: "))
            std_dev = float(input("Enter standard deviation: "))
            result = calculate_probability_normal(x_value, mean, std_dev)
            print("Probability:", result)
        elif choice == 37:
            x_value = int(input("Enter x value: "))
            n = int(input("Enter n: "))
            p = float(input("Enter probability of success (p): "))
            result = calculate_probability_binomial(x_value, n, p)
            print("Probability:", result)
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()




