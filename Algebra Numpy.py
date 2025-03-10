import numpy as np 

while True: 
    print("1. Linear Equation \n2. Quadratic Equation")
    choice = int(input("Which type of expression do you want to evaluate? "))

    x = np.arange(0, 11)

    if choice == 1:
        print("ax + b")
        a = int(input("Enter value for a: "))
        b = int(input("Enter value for b: "))
        print(f"{a}x + {b} for x=0 to 10 is:")
        linear =a * x + b
        print(linear)

    elif choice == 2:
        print("ax^2 + bx + c")
        a = int(input("Enter value for a: "))
        b = int(input("Enter value for b: "))
        c = int(input("Enter value for c: "))
        print(f"{a}x^2 + {b}x + {c} for x=0 to 10 is:")
        quad =a * x**2 + b * x + c
        print(quad)

    else:
        print("Invalid choice! Please enter 1 or 2.")
        continue 

    loop = input("Would you like to continue? (yes/no): ").strip().lower()
    if loop != "yes":
        break
