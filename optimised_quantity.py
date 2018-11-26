"""
Program to identify optimised no of quantity required from the available length standard
Here Key is lenth and value is quantity required from the materia dict.
but standard length available from the market is 300
"""

material = {150:5,200:3,250:4,100:7}
standard_material = {300:1000}
sum = 0
for key in material.keys():
    sum+=key*material[key]
optimised_quantity = standard_material[300]
print(sum)
if standard_material.keys()[0] * standard_material[300] == sum:
    print("if")
    print(standard_material[300])

elif standard_material.keys()[0] * standard_material[300] > sum:
    print("elseif")
    while((standard_material[300] * standard_material.keys()[0]) > sum):
        optimised_quantity -= 1
        standard_material[300] = optimised_quantity
    print("length*quantity",standard_material.keys()[0],(standard_material[300] + 1),(standard_material[300] + 1)*standard_material.keys()[0])
else:
    print("else")
    while((standard_material[300] * standard_material.keys()[0]) < sum):
        optimised_quantity += 1
        standard_material[300] = optimised_quantity
    print("length*quantity",standard_material.keys()[0],standard_material[300],standard_material[300]*standard_material.keys()[0])
    
        
        