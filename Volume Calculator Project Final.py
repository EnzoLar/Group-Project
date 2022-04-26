print("This is a Volume Calculator by Enzo, Rocio and Cade!")


if __name__ == '__main__':


    while True:
        print("\nMAIN MENU: Please select one of the following shapes (1.Triangular Prism, 2. Sphere, 3. Cube, 4. Cylinder, 5. Rectangular Prism, 6. 3D Parallelogram, 7. Rhombus, 8. Trapezium)")
        print("1. Triangular Prism")
        print("2. Sphere")
        print("3. Cube")
        print("4. Cylinder")
        print("5. Rectangular Prism")
        print("6. 3D Parallelogram")
        print("7. Rhombus")
        print("8. Trapezium")
        print("0. Exit Calculator\n")

        choice = input("Your choice: ")

        if choice == "1":

                
                length= float(input('Please Enter the length of a triangle: '))
                Base= float(input('Please Enter the base of a triangle: '))
                Height= float(input('Please Enter the height of a triangle: '))
                Volume = (0.5 * length * Base * Height )
                print("\n The Volume of a triangular prism is %.2f" %Volume)
                
                while True:
                    choice = input('\nType M to return to Main Menu, or R to repeat: ')
                    if choice == "M":
                        break
                    elif choice == "R":
                        pass
                    else:
                        print("Invalid input.  Please try again!\n")
                        continue

                    length= float(input('Please Enter the length of a triangle: '))
                    Base= float(input('Please Enter the base of a triangle: '))
                    Height= float(input('Please Enter the height of a triangle: '))
                    Volume = (0.5 * length * Base * Height )
                    print("\n The Volume of a triangular prism is %.2f" %Volume)
                    print("\n")

        elif choice == "2":

                PI = 3.14
                radius = float(input('Please Enter the Radius of a Sphere: '))
                Volume = (4 / 3) * PI * radius * radius * radius
                print("\n The Volume of a Sphere is %.2f" %Volume)
                
                while True:
                    choice = input('\nType M to return to Main Menu, or R to repeat: ')
                    if choice == "M":
                        break
                    elif choice == "R":
                        pass
                    else:
                        print("Invalid input.  Please try again!\n")
                        continue

                    PI = 3.14
                    radius = float(input('Please Enter the Radius of a Sphere: '))
                    Volume = (4 / 3) * PI * radius * radius * radius
                    print("\n The Volume of a Sphere is %.2f" %Volume)
                    print("\n")
                    
        elif choice == "3":

            length = float(input('\nPlease Enter the length of a cube: '))
            Volume = length * length * length
            print("\n The Volume of a cube is %.2f" % Volume)

            while True:
                choice = input('\nType M to return to Main Menu, or R to repeat: ')
                if choice == "M":
                    break
                elif choice == "R":
                    pass                   
                else:
                    print("Invalid input.  Please try again!\n")
                    continue

                length= float(input('\nPlease Enter the length of a cube: '))
                Volume = length * length * length
                print("\nThe Volume of a cube is %.2f" %Volume)
                print("\n")
                    
        elif choice == "4":

                
                PI = 3.14
                radius = float(input('Please Enter the Radius of a Cylinder: '))
                height = float(input('Please Enter the Height of a Cylinder: '))
                Volume = PI * radius * radius * height
                print("\n The Volume of a cylinder is %.2f" %Volume)
                
                while True:
                    choice = input('\nType M to return to Main Menu, or R to repeat: ')
                    if choice == "M":
                        break
                    elif choice == "R":
                        pass
                    else:
                        print("Invalid input.  Please try again!\n")
                        continue

                    PI = 3.14
                    radius = float(input('Please Enter the Radius of a Cylinder: '))
                    height = float(input('Please Enter the Height of a Cylinder: '))
                    Volume = PI * radius * radius * height
                    print("\n The Volume of a cylinder is %.2f" %Volume)
                    print('\n')
                    
        elif choice == "5":
                
                l = float(input('Enter the length: '))
                w = float(input('Enter the width: '))
                h = float(input('Enter the height: '))

                def find_volume_of_Rectangular_prism(l, w, h):
                    return ( (l * w * h)) # It is a formula which finds the value of volume.

                print("The volume of this rectangular prism is:", find_volume_of_Rectangular_prism(l, w, h))
                
                while True:
                    choice = input('\nType M to return to Main Menu, or R to repeat: ')
                    if choice == "M":
                        break
                    elif choice == "R":
                        pass
                    else:
                        print("Invalid input.  Please try again!\n")
                        continue

                    l = float(input('Enter the length: '))
                    w = float(input('Enter the width: '))
                    h = float(input('Enter the height: '))

                    def find_volume_of_Rectangular_prism(l, w, h):
                        return ( (l * w * h))
                    print("\n The Volume of a rectangular prism is %.2f", find_volume_of_Rectangular_prism(l, w, h))
                    print('\n')
                    
        elif choice == "6":

                base = float(input('Enter the length of base: '))
                height = float(input('Enter the height: '))
                area = base * height
                volume = area * height
                print("The volume of this 3D parallelogram is:", volume)
                
                while True:
                    choice = input('\nType M to return to Main Menu, or R to repeat: ')
                    if choice == "M":
                        break
                    elif choice == "R":
                        pass
                    else:
                        print("Invalid input.  Please try again!\n")
                        continue

                    base = float(input('Enter the length of base: '))
                    height = float(input('Enter the height: '))
                    area = base * height
                    volume = area * height
                    print("The volume of this 3D parallelogram is:", volume)
                    print('\n')
                    
        elif choice == "7":

                d1 = float(input('Enter 1st diagonal: '))
                d2 = float(input('Enter 2nd diagonal: '))
                l = float(input('Enter the length: '))
                def findVolumeofrhombus(d1, d2):
                    return ( ( d1 * d2 ) / 2) * l

                print("The volume of this rhombus is:", findVolumeofrhombus(d1,d2))
                
                while True:
                    choice = input('\nType M to return to Main Menu, or R to repeat: ')
                    if choice == "M":
                        break
                    elif choice == "R":
                        pass
                    else:
                        print("Invalid input.  Please try again!\n")
                        continue

                    d1 = float(input('Enter 1st diagonal: '))
                    d2 = float(input('Enter 2nd diagonal: '))
                    l = float(input('Enter the length: '))
                    def findVolumeofrhombus(d1, d2):
                        return ( ( d1 * d2 ) / 2) * l
                    print("The volume of this rhombus is:", findVolumeofrhombus(d1,d2))
                    print('\n')
                    
        elif choice == "8":

                height = float(input("Height of trapezoid: "))
                base_1 = float(input('Base one value: '))
                base_2 = float(input('Base two value: '))
                area = ((base_1 + base_2) / 2) * height
                volume = area * height
                print("The volume of this trapezium is:", volume)
                
                while True:
                    choice = input('\nType M to return to Main Menu, or R to repeat: ')
                    if choice == "M":
                        break
                    elif choice == "R":
                        pass
                    else:
                        print("Invalid input.  Please try again!\n")
                        continue

                    height = float(input("Height of trapezoid: "))
                    base_1 = float(input('Base one value: '))
                    base_2 = float(input('Base two value: '))
                    area = ((base_1 + base_2) / 2) * height
                    volume = area * height
                    print("The volume of this trapezium is:", volume)
                    print('\n')

        elif choice == "0":
            break

        else:
            print("Invalid input.  Please try again!\n")



    print("Thank you for using our Calculator.  Have fun!")

