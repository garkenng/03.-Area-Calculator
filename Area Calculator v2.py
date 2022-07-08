"""
Area calculator v2.
Added to accept upper and lowercase input
Added measure for program to exit if invalid entry reaches 3
"""

print('Area Calculator has started!')
name = input('What\'s your name? ')

incorrect_response = 0

while incorrect_response < 3:
    option = input('Enter C for circle or T for triangle: ')
    if option == 'c' or option == 'C':
        radius = float(input('Enter radius: '))
        area = 3.14159 * radius ** 2
        print(f'Area of cirlce is: {area}')
        break
    elif option == 't' or option == 'T':
        base = float(input('Enter base: '))
        height = float(input('Enter height: '))
        area = 0.5 * base * height
        print(f'Area of triangle is: {area}')
        break
    else:
        print('Entered too many invalid choices!')
        incorrect_response += 1
    
   
print('Program has ended, have a nice day!')