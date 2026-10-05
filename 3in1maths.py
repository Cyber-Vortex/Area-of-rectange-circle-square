while True:
    print("Press 1 to find the Area of rectangle:")
    print("Press 2 to find the Area of square:")
    print("Press 3 to find the Area of circle:")
    print("Press 4 to exit")

    choice = int(input("Enter the number between (1 to 4): "))

    if choice == 1:
        length = float(input("Enter the length: "))
        breadth = float(input("Enter the breadth: "))
        area = length * breadth
        print("Area of the rectangle is:", area)
    elif choice == 2:
        side = float(input("Enter the side: "))
        area = side * side
        print("Area of the square is:", area)
    elif choice == 3:
        pi = 3.14
        radius = float(input("Enter the radius: "))
        area = pi * radius * radius
        print("Area of the circle is:", area)
    elif choice == 4:
        print("Exiting the program.")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 4.")
