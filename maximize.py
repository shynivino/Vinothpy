""" oBJ fUN => MAXIMIXE X+10Y
Sub to 
x+7*y <= 17.5
x <= 3.5
x,y >=0"""

x=0;y=0
for i in range(1,1000):
    
    
    if x+7*y <= 17.5 and x <= 3.5 and x >= 0:
        x=x+1
x=x-1
for i in range(1,100):
    if x+7*y <= 17.5 and x <= 3.5 and y >= 0:
        y=y+1            
    
y=y-1       
print(x)
print(y)
print(x+10*y)
