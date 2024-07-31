def matrix_input(prompt): 

    print(prompt) 

    r = int(input("Enter no of rows: ")) 

    c = int(input("Enter no of columns: ")) 

    matrix = [] 

    print("Enter the matrix row by row:") 

    for i in range(r): 

        row = list(map(int, input().split())) 

        if len(row) != c: 

            print("Invalid row length. Please re-enter the row.") 

            row = list(map(int, input().split())) 

        matrix.append(row) 

    return matrix  

def matrix_multiply(A, B): 

    r_A, c_A = len(A), len(A[0]) 

    r_B, c_B = len(B), len(B[0])     

    if c_A != r_B: 

        return "Error: Matrices are not multiplicable."         

    result = [[0 for _ in range(c_B)] for _ in range(r_A)]  

    for i in range(r_A): 

        for j in range(c_B): 

            for k in range(c_A): 

                result[i][j] += A[i][k] * B[k][j] 

    return result  

def main(): 

    A = matrix_input("Enter matrix A:") 

    B = matrix_input("Enter matrix B:")  

    result = matrix_multiply(A, B)  

    if isinstance(result, str): 

        print(result) 

    else: 

        print("The product of matrices A and B is:") 

        for row in result: 

            print(" ".join(map(str, row))) 

if __name__ == "__main__": 

    main() 