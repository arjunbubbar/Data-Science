import numpy as np 

import matplotlib.pyplot as plt

while True: 
    print("1. Linear Equation \n2. Quadratic Equation \n3. Cubic Equation")
    choice = int(input("Which type of expression do you want to evaluate? "))

    x = np.arange(0, 51)

    if choice == 1:
        print("ax + b")
        a = int(input("Enter value for a: "))
        b = int(input("Enter value for b: "))
        linear = a * x + b
        label = f"y = {a}x + {b}"
        print(f"The figure {label} for x = 0 to 50:")
        plt.figure(figsize=(8, 6))
        plt.plot(x, linear, 'r-', linewidth=2, label=label)
        plt.title("Linear Equation")
        plt.legend()
        plt.show()

    elif choice == 2:
        print("ax^2 + bx + c")
        a = int(input("Enter value for a: "))
        b = int(input("Enter value for b: "))
        c = int(input("Enter value for c: "))
        quad = a * x**2 + b * x + c 
        label = f"y = {a}x^2 + {b}x + {c}"
        print(f"The figure {label} for x = 0 to 50:")
        plt.figure(figsize=(8, 6))
        plt.plot(x, quad, 'r-', linewidth=2, label=label)
        plt.title("Quadratic Equation")
        plt.legend()
        plt.show()

    elif choice == 3:
        print("Expression format: ax³ + bx² + cx + d")
        a = int(input("Enter value for a: "))
        b = int(input("Enter value for b: "))
        c = int(input("Enter value for c: "))
        d = int(input("Enter value for d: "))
        cub = a * x**3 + b * x**2 + c * x + d
        label = f"y = {a}x^3 + {b}x^2 + {c}x + {d}"
        print(f"The figure {label} for x = 0 to 50:")
        plt.figure(figsize=(8, 6))
        plt.plot(x, cub, 'r-', linewidth=2, label=label)
        plt.title("Cubic Equation")
        plt.legend()
        plt.show()

    else:
        print("Invalid choice! Please enter 1, 2 or 3.")
        continue 

    loop = input("Would you like to continue? (yes/no): ").strip().lower()
    if loop != "yes":
        break
