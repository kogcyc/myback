import math

def arctan_approximation(x, n):
    result = 0
    sign = 1
    
    for k in range(n):
        term = (sign * (x ** (2 * k + 1))) / (2 * k + 1)
        result += term
        sign *= -1
    
    return result

# Example usage:
x = 0.5
n = 30  # You can change 'n' to adjust the number of terms used in the approximation
approximation = arctan_approximation(x, n)
print(math.degrees(approximation))
