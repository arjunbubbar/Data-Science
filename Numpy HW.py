
import numpy as np

while True: 

    rows = int (input ("How many rows would you like the matrices to have? "))
    cols = int (input ("How many columns would you like the matrices to have? "))

    choice = input ("Would you like to randomise or choose? ").lower()
    if choice == "randomise":
        matrix1 = np.random.randint (1,200,(rows,cols))
        matrix2 = np.random.randint (1,200,(rows,cols))
        print (matrix1) 
        print (matrix2)

    elif choice == "choose":
        matrix1 = []
        print ("Please enter values for Matrix 1 ")
        for i in range (rows):
            row = []
            for j in range (cols):
                value = int (input (f"Enter value for position [{i+1}, {j+1}]: ")) 
                # Had to search this up was confused here, explanation needed
                row.append(value)
            matrix1.append(row)  
        matrix1 = np.array(matrix1)  

        matrix2 = []
        print ("Please enter values for Matrix 2")
        for i in range (rows):
            row = []
            for j in range (cols):
                value = int (input(f"Enter value for position [{i+1}, {j+1}]: "))
                row.append(value)
            matrix2.append(row)  
        matrix2 = np.array(matrix2)

        print (matrix1)
        print (matrix2)        

    else:
        print ("Invalid choice, please enter 'randomise' or 'choose' ")
        continue
        
    operation = input ("Would you like to add or subtract? ").lower()
    if operation == "add": 
        add = matrix1 + matrix2
        print (add)
    elif operation == "subtract": 
        subtract = matrix1 - matrix2
        print (subtract)
    else:
        print ("Invalid operation, please enter 'add' or subtract' ")
        continue

    loop = input ("Would you like to continue? ").lower()
    if loop == "yes":
        continue
    else: 
        print ("Thank you for playing ")
        break




