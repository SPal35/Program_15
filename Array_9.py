def generate_2d_array(X, Y):

    array = [[i * j for j in range(Y)] for i in range(X)]
    return array

X = int(input("Enter the number of rows (X): "))
Y = int(input("Enter the number of columns (Y): "))

result_array = generate_2d_array(X, Y)

for row in result_array:
    print(row)
