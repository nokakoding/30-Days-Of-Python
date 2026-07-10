age = int(18)
height = float(5.5)
weight = complex(60kg)

area = 0.5 * Base * Height

base = float(input('Base: '))
height = float(input('Height: '))

area = 0.5 * base * height 

print(f'The area of the triangle is {int(area)}')

side_a = float(input('Side A: '))
side_b = float(input('Side B: '))
side_c = float(input('Side C: '))

perimeter = side_a + side_b + side_c

print(f'The perimeter of the triangle is {int(perimeter)}')

length = float(input('Length: '))
width = float(input('Width: '))

area = length * width 
perimeter = 2 * length * width 

print(f'''The area of the rectangle is {int(area)}. The perimeter of the rectangle is {int(perimeter)}.''')

radius = float(input('Radius of the circle: ')) 

area = 3.14 * radius * radius
circumference = 2 * 3.14 * radius 

print(f'The area of the circle is {float(area)} and its circumference is {float(circumference)}.')

len_python = len('python')
len_dragon = len('dragon')

print(f"The length of 'python': {len_python}")
print(f"The length of 'dragon': {len_dragon}")

is_not_equal = len_python != len_dragon

print(f"is the length of 'python' and 'dragon' the same? {is_not_equal}")

check_on = ('on' in 'python' and 'on' in 'dragon') 

print(f"Is 'on' present in both 'python' and 'dragon'? {check_on}")





