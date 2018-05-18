#Concept of finding N largest/smallest numbers
from collections import Counter
 
arr = [1, 3, 4, 1, 2, 1, 1, 3, 4, 3, 5, 1, 2, 5, 3, 4, 5]
counter = Counter(arr)
top_three = counter.most_common(3)
print(top_three)
##[(1, 5), (3, 4), (4, 3)]

first_attempt = Counter({1: 90, 2: 65, 3: 78, 4: 88})
second_attempt = Counter({1: 88, 2: 84, 3: 95, 4: 92})
final = first_attempt | second_attempt
print(final)# Counter({3: 95, 4: 92, 1: 90, 2: 84}) Prints the keys that having highest value

#Concept of Zipping & Sorting dict
import heapq
 
stocks = {
    'Goog' : 520.54,
    'FB' : 76.45,
    'yhoo' : 39.28,
    'AMZN' : 306.21,
    'APPL' : 99.76
    }
 
zipped_1 = zip(stocks.values(), stocks.keys())
 
# sorting according to values
print(sorted(zipped_1))
#[(39.28, 'yhoo'), (76.45, 'FB'), (99.76, 'APPL'), (306.21, 'AMZN'), (520.54, 'Goog')]
 
#sorting according to keys
zipped_2 = zip(stocks.keys(), stocks.values())
print(sorted(zipped_2))
#[('AMZN', 306.21), ('APPL', 99.76), ('FB', 76.45), ('Goog', 520.54), ('yhoo', 39.28)]

# Python code to apply a function on a list map, reduce and filter
income = [10, 30, 75]
 
def double_money(dollars):
    return dollars * 2
 
new_income = list(map(double_money, income))
print(new_income)#[20, 60, 150]

total=reduce(lambda x,y:x+y,income)
print (total)

filtered=filter(lambda x:x>25,income)
print filtered #[30, 75]

##finding pythogorian triplets
print [(x, y, z) for z in range(1,100) for y in xrange(1, z) for x in range(1, y) if x*x + y*y == z*z]
##output##
"""

[(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20), (15, 20, 25), (7, 24, 25), 
(10, 24, 26), (20, 21, 29), (18, 24, 30), (16, 30, 34), (21, 28, 35), (12, 35, 37), (15, 36, 39), (24, 32, 40), 
(9, 40, 41), (27, 36, 45), (30, 40, 50), (14, 48, 50), (24, 45, 51), (20, 48, 52), (28, 45, 53), (33, 44, 55), 
(40, 42, 58), (36, 48, 60), (11, 60, 61), (39, 52, 65), (33, 56, 65), (25, 60, 65), (16, 63, 65), (32, 60, 68), 
(42, 56, 70), (48, 55, 73), (24, 70, 74), (45, 60, 75), (21, 72, 75), (30, 72, 78), (48, 64, 80), (18, 80, 82), 
(51, 68, 85), (40, 75, 85), (36, 77, 85), (13, 84, 85), (60, 63, 87), (39, 80, 89), (54, 72, 90), (35, 84, 91), 
(57, 76, 95), (65, 72, 97)]

"""


