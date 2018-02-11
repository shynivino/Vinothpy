#Concept of finding N largest/smallest numbers
from collections import Counter
 
arr = [1, 3, 4, 1, 2, 1, 1, 3, 4, 3, 5, 1, 2, 5, 3, 4, 5]
counter = Counter(arr)
top_three = counter.most_common(5)
print(top_three)

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
 
zipped_2 = zip(stocks.keys(), stocks.values())
print(sorted(zipped_2))
#sorting according to keys

# Python code to apply a function on a list
income = [10, 30, 75]
 
def double_money(dollars):
    return dollars * 2
 
new_income = list(map(double_money, income))
print(new_income)
