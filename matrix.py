import math
from copy import deepcopy

def bubble_sort_column_desc(matrix, col):
    n = len(matrix)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if matrix[j][col] < matrix[j + 1][col]:
                matrix[j][col], matrix[j + 1][col] = matrix[j + 1][col], matrix[j][col]

def sort_columns_desc(matrix):
    sorted_matrix = deepcopy(matrix)
    cols = len(sorted_matrix[0])
    for col in range(cols):
        bubble_sort_column_desc(sorted_matrix, col)
    return sorted_matrix

def calculate_f(matrix):
    n = len(matrix)
    fi_values = []
    for i in range(n):
        product = 1
        count = 0
        for j in range(i + 1, n):
            if matrix[i][j] > 0:
                product *= matrix[i][j]
                count += 1
        if count > 0:
            fi = product ** (1 / count)
        else:
            fi = 0
        fi_values.append(fi)
    return fi_values, sum(fi_values)

def main():
    A = [
        [0, 2, -2, 89, 21],
        [-1, -4, 36, 41, 71],
        [56, 93, 51, -2, -51],
        [1, 3, -8, 0, 9],
        [23, 41, 5, 8, -2],
    ]

    print("Початкова матриця:")
    for row in A:
        print(row)

    sorted_A = sort_columns_desc(A)

    print("\nВідсортована матриця:")
    for row in sorted_A:
        print(row)

    fi, F = calculate_f(sorted_A)

    print("\nfi(aij):")
    for value in fi:
        print(round(value, 3))

    print("\nF(fi(aij)) =", round(F, 3))

if __name__ == "__main__":
    main()
