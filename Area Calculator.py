"""
Area calculator
"""

print('Area Calculator has started!')
name = input('What\'s your name? ')
option = input('Enter C for circle or T for triangle: ')

if option == 'c':
    radius = float(input('Enter radius: '))
    area = 3.14159 * radius ** 2
    print(f'Area of cirlce is: {area}')
elif option == 't':
    base = float(input('Enter base: '))
    height = float(input('Enter height: '))
    area = 0.5 * base * height
    print(f'Area of triangle is: {area}')
else:
    print('Entered invalid shape!')

print('Program has ended, have a nice day!')