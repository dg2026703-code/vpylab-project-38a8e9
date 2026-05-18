from vpython import *
sphere(pos=vector(0,0,0))

box(pos=vector(0,0,0.9),size=vector(17,10,0.5))

box(pos=vector(0,0,1.2),size=vector(16,9,0.2),color=color.red)

box(pos=vector(0,-5,0),size=vector(1,10,1))

box(pos=vector(0,-10,0),size=vector(5,0.1,5))

box(pos=vector(8,-10,5),size=vector(3,1,5))

box(pos=vector(8,-9.5,4),size=vector(0.5,0.1,3),color=color.black)

b = box(make_trail = True)

while True : 
    rate(700)
    k=keysdown()
    if ' ' in k:
        b.color = color.blue
        
        
        
        
        
        
    



