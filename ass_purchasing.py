"""
Purchasing optimization: Provider product purchasing
====================================================
Another use case of optimization is in the purchase of goods. Providers offer certain products under some conditions (costs, availability restrictions) and optimization is performed according to several criteria. 

In this case we need to fulfill some good needs by minimizing the cost of the purchasing of the goods.

More specifically,

Given:
- A set of products (goods) g1, g2, g3, ...
- A set of providers p1, p2, p3, ...
- An stock catalog, in which there is the stock availability of each good for each provider:
		gx	gy	gz
	pa	10	20	10
	pb	20	40	10
	pc	30	30	30
- A margin catalog, in which there is the (calculated) margin per unit of each good for each provider:
		gx	gy	gz
	pa	1	2	1
	pb	1	3	1
	pc	2	3	1
- A product demand

The goal is
- Minimize the cost of the product purchases.

Restrictions are:
- Fulfill the product demand.
- For each good and provider not to overlap the max stock availability.

Code snippet with data
- See ass_purchasing.py

Additional exercise
Consider the additional restriction and reforumulate the problem:
- We can only buy products from at most three different providers.
"""

# Import PuLP modeler functions
from pulp import *

# Create the 'prob' variable to contain the problem data
prob = LpProblem("A Purchasing Problem",LpMinimize)

# List of goods (products)
lgood = ['g1','g2','g3','g4','g5','g6','g7','g8','g9']
# List of providers
lprov = ['p1','p2','p3','p4','p5']

# Demand per good
demand = {
	'g1': 1000,
	'g2': 500,
	'g3': 700,
	'g4': 300,
	'g5': 200,
	'g6': 1500,
	'g7': 750,
	'g8': 250,
	'g9': 1000
}

# Stock catalog
# catalog_stock['p1']['g1']: Stock of good g1 for the provider p1
catalog_stock = {
	'p1': {'g1':1000,'g2':1000,'g3':0   ,'g4':500 ,'g5':300 ,'g6':200 ,'g7':800 ,'g8':1000,'g9':1000},
	'p2': {'g1':0   ,'g2':0   ,'g3':20  ,'g4':0   ,'g5':3000,'g6':1000,'g7':100 ,'g8':100 ,'g9':100 },
	'p3': {'g1':0   ,'g2':300 ,'g3':100 ,'g4':400 ,'g5':1000,'g6':500 ,'g7':50  ,'g8':8000,'g9':4000},
	'p4': {'g1':500 ,'g2':500 ,'g3':800 ,'g4':1000,'g5':100 ,'g6':1000,'g7':700 ,'g8':300 ,'g9':5000},
	'p5': {'g1':5000,'g2':250 ,'g3':200 ,'g4':2000,'g5':100 ,'g6':1000,'g7':500 ,'g8':200 ,'g9':100 },
}

# Cost catalog
# catalog_cost['p1']['g1']: Cost per unot of good g1 for the provider p1
catalog_cost = {
	'p1': {'g1':10  ,'g2':10  ,'g3':0   ,'g4':5   ,'g5':20  ,'g6':15  ,'g7':10  ,'g8':5   ,'g9':10  },
	'p2': {'g1':0   ,'g2':0   ,'g3':4   ,'g4':4   ,'g5':19  ,'g6':14  ,'g7':10  ,'g8':6   ,'g9':10  },
	'p3': {'g1':0   ,'g2':8   ,'g3':4   ,'g4':5   ,'g5':19  ,'g6':13  ,'g7':10  ,'g8':5   ,'g9':10  },
	'p4': {'g1':9   ,'g2':10  ,'g3':4   ,'g4':5   ,'g5':18  ,'g6':15  ,'g7':10  ,'g8':5   ,'g9':11  },
	'p5': {'g1':10  ,'g2':9   ,'g3':5   ,'g4':6   ,'g5':20  ,'g6':15  ,'g7':10  ,'g8':4   ,'g9':10  },
}


# Variables

# Optimization function
prob += 0 # To be filled

# Restrictions

# Fill the current demand

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# The optimised objective function value is printed to the screen
print("Total Cost of Purchasing = ", value(prob.objective))
