
def measurement_converter():
    while True:
     print('Measurement Converter')
     print("1. Millimeters to Centimeter")
     print('2. Feet to Meters')
     print('3. Inches to Centimeters')
     print("4. Kilograms to Pounds")
     print('5. Celsius to Fahrenheit')

     choice = int(input("Enter your choice (1-5): "))
     if choice == 1:
        mm = float(input("Enter millimeters:"))
        cm = mm/10
        print(f"{mm} millimeters is equal to {cm} centimeters")
     elif choice == 2:
        ft = float(input("Enter feet:"))
        m = ft * 0.3048
        print(f'{ft}feet is equal to {m} meters')
     elif choice ==3:
        inch = float(input("Enter inches:"))
        cm = inch * 2.54
        print(f"{inch} inches is equal to {cm} centimeters")
     elif choice ==4:
        kg = float(input("Enter kilograms:"))
        lb = kg * 2.205
        print(f"{kg} kilograms is equal to {lb} pounds")
     elif choice == 5:
        c = float(input("Enter Celsius:"))
        f = (c* 9/5)+ 32
        print(f"{c} Celsius is equal to {f} Fahrenheit")
     else:
        print("Invalid choice. Please try again.")
    
     print("Do you want to try again? (yes/no)")
     response = input().lower()
     if response != 'yes':
        break
     
measurement_converter()