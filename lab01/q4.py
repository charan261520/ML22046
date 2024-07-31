def matrix_input(prompt): 

    print(prompt) 

    r = int(input("Enter the number of rows: ")) 

    c = int(input("Enter the number of columns: ")) 

    matrix = [] 

    print("Enter the matrix row by row:") 

    for _ in range(r): 

        row = list(map(int, input().split())) 

        if len(row) != c: 

            print(f"Invalid row length. Please enter exactly {cols} integers.") 

            row = list(map(int, input().split())) 

        matrix.append(row) 

    return matrix 

def t_matrix(matrix): 

    r = len(matrix) 

    c = len(matrix[0])  

    transposed = [[0 for _ in range(r)] for _ in range(c)]                        

    for i in range(r): 

        for j in range(c): 

            transposed[j][i] = matrix[i][j]     

    return transposed  

def main():                                                       

    matrix = matrix_input("Enter the matrix:")     

    transposed = t_matrix(matrix)     

    print("The transposed matrix is:") 

    for row in transposed: 

        print(" ".join(map(str, row)))  

if __name__ == "__main__": 

    main() 