import math

C = 50
H = 30

def calculate_Q(D):
    return math.sqrt((2 * C * D) / H)

input_values = input("Enter a comma-separated sequence of D values: ")

D_values = input_values.split(',')

result = []
for D in D_values:
    D = float(D.strip()) 
    Q = calculate_Q(D)
    result.append(Q)

print(','.join(map(str, result)))
