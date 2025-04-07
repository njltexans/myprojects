# this is going to be an area calculator for different shapes


Shape = input('What shape do you want to calculate the area for? ')
if Shape == 'circle':
    radius = int(input('Enter the radius of the circle: '))
elif Shape == 'rectangle':
    length = int(input('Enter the length of the shape: '))
    width = int(input('Enter the width of the shape: '))
elif Shape == 'triangle':
    base = int(input('Enter the base of the triangle: '))
    height = int(input('Enter the height of the triangle: '))
elif Shape == 'square':
    side = int(input('Enter the side of the square: '))
else:
    print('Nah, not a real shape')



if Shape == 'rectangle':
    area = length * width
    print(f'The area of the rectangle is {area}')
elif Shape == 'circle': 
    area = 3.14159 * radius**2
    print(f'The area of the circle is {area}')
elif Shape == 'triangle':
    area = 0.5 * base * height
    print(f'The area of the triangle is {area}') 
elif Shape == 'square':
    area = side**2
    print(f'The area of the square is {area}')   