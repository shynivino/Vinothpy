"""
Tonnage	400
Tower	150

Indian			
Trailer	Weight,t	Length,m	$/KM
1	       70	       25	       7.5
2	       65	       25	       5.5
3	       65	       27	       5.5
4	       55	       30	       5
5	       50	       30	       5

=SUMPRODUCT(Weight * NoOfTrailer) = > 405  	0.9877	>= 0.75	< 1

=SUMPRODUCT(Length * NoOfTrailer) = > 200	    0.7500	>= 0.5	< 1

"""

import pulp

weight = [70, 65, 65, 55, 50]
lenght = [25, 25, 27, 30, 30]
cost = [7.5, 5.5, 5.5, 5, 5]
tower_weight = 400
tower_length = 150

model = pulp.LpProblem(pulp.LpMinimize)

x1 = pulp.LpVariable('x1', lowBound=0, cat='Integer')
x2 = pulp.LpVariable('x2', lowBound=0, cat='Integer')
x3 = pulp.LpVariable('x3', lowBound=0, cat='Integer')
x4 = pulp.LpVariable('x4', lowBound=0, cat='Integer')
x5 = pulp.LpVariable('x5', lowBound=0, cat='Integer')

def obj_func (x1, x2, x3, x4, x5):
    sum_cost = (cost[0]*x1 + cost[1]*x2 + cost[2]*x3 + cost[3]*x4 + cost[4]*x5) * 100
    return sum_cost

def cons_eqn1 (x1, x2, x3, x4, x5):
    y1 = (weight[0]*x1 + weight[1]*x2 + weight[2]*x3 + weight[3]*x4 + weight[4]*x5) / tower_weight
    return y1

def cons_eqn2 (x1, x2, x3, x4, x5):
    y2 = (lenght[0]*x1 + lenght[1]*x2 + lenght[2]*x3 + lenght[3]*x4 + lenght[4]*x5) / tower_length
    return y2

model += obj_func (x1, x2, x3, x4, x5)

model += cons_eqn1 (x1, x2, x3, x4, x5) <= 1/.75
model += cons_eqn1 (x1, x2, x3, x4, x5) >= 1
model += cons_eqn2 (x1, x2, x3, x4, x5) <= 1/.5
model += cons_eqn2 (x1, x2, x3, x4, x5) >= 1

model.solve()

if pulp.LpStatus[model.status] == "Optimal":
    print ("Trailer 1 {}".format(x1.varValue))
    print ("Trailer 2 {}".format(x2.varValue))
    print ("Trailer 3 {}".format(x3.varValue))
    print ("Trailer 4 {}".format(x4.varValue))
    print ("Trailer 5 {}".format(x5.varValue))
    print ("Cost is {}".format(pulp.value(model.objective)))
else:
    print(pulp.LpStatus[model.status])
    
####################output##################
"""
Trailer 1 0.0
Trailer 2 2.0
Trailer 3 0.0
Trailer 4 5.0
Trailer 5 0.0
Cost is 3600.0
"""
#############################################
