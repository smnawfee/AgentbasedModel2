import random

y0=50
x0=50

if random.random() < 0.5:
    y0 +=1
else:
    y0 -=1
    
if random.random() < 0.5:
    x0 +=1
else:
    x0 -=1
    
print (y0,x0)
    
y1=51
x1=51

if random.random() < 0.5:
    y1 +=1
else:
    y1 -=1
    
if random.random() < 0.5:
    x1 +=1
else:
    x1 -=1
    
print (y1,x1) 

answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
print(answer)