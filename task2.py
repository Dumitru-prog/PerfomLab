f = open('file1.txt') 
coords = f.readline().split() 
radius = float(f.readline()) 
x = float(coords[0]) 
y = float(coords[1])
print(f"x = {x} y = {y} radius = {radius}")
f = open('file2.txt') 
dots = f.readlines() 
for dot in dots: 
    dot = dot.split() 
    xd = float(dot[0]) 
    yd = float(dot[1])
    if (x - xd)**2 + (y - yd)**2 < radius**2: 
        print(1) 
    elif (x - xd)**2 + (y - yd)**2 > radius**2:
        print(2) 
    else:
        print(0) 