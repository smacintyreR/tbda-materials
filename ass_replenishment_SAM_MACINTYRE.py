"""
Logistics management: store replenishment - Sam MacIntyre Assignment - Topic in Big Data 1
=========================================
Logistics is about getting the right product, to the right customer, in the right quantity, in the right condition, at the right place, at the right time, and at the right cost (the seven Rs of Logistics).

In this case we need to calculate the stores assignment of a given product by considering the store demands, the transportation costs, the margin and the total stock of the product in the warehouse.
The goal is to maximize the benefit by considering the demand, the margin and the transportation costs.

More specifically,

Given:
- A list of stores s1, s2, s3, ...
- A product demand for each store
- A transportation cost per product unit for each store
- A margin per product unit for each store
- An initial stock in the warehouse

The goal is:
- Maximize the benefit of sending the units of product to each store.

Restrictions are:
- Not to overlap the maximum amount of stock in the warehouse.

Code snippet with data
- See ass_replenishment.py

Additional exercise
In many real cases the product demand is not well known. Consider now the demand follows a Poisson distribution P(l), where l is the previous value of demand (the expected demand for each store). Reformulate the problem with this new situation.
"""



# Import PuLP modeler functions
from pulp import *
import numpy as np

# Create the 'prob' variable to contain the problem data
prob = LpProblem("Replenishment Problem",LpMaximize)

# List of stores
lstore = ['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10']

# Demand for each store
demand = {
	's1': 100,
	's2': 50,
	's3': 25,
	's4': 60,
	's5': 70,
	's6': 85,
	's7': 90,
	's8': 95,
	's9': 22,
	's10': 30
}
# Per unit transportation cost for each store
transport = {
	's1': 1,
	's2': 1,
	's3': 2,
	's4': 2,
	's5': 3,
	's6': 3,
	's7': 2,
	's8': 1,
	's9': 1,
	's10': 1
}
# Per unit margin for each store
margin = {
	's1': 10,
	's2': 10,
	's3': 9,
	's4': 9,
	's5': 9,
	's6': 8,
	's7': 8,
	's8': 10,
	's9': 10,
	's10': 10
}
# Initial stock in the warehouse
initial_stock = 300

# Variables (Integers)
storeVariables = LpVariable.dicts("Str", lstore, 0, cat = 'Integer')

# Optimization function
prob += lpSum([storeVariables[i]*margin[i] - storeVariables[i]*transport[i] for i in lstore]), "Total Revenue"

# Restrictions

# Add restriction for total available stock
prob += lpSum([storeVariables[i] for i in lstore]) == initial_stock, "StockAvailable"

# Add restrictions to ensure we never exceed demand in a store
for i in lstore:
	prob += storeVariables[i] <= demand[i]


# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# The optimised objective function value is printed to the screen
print("Total Benefit of Replenishment = ", value(prob.objective))


# Print out the final values for each store - the result appears to agree with common sense
for v in prob.variables():
    print(v.name, "=", v.varValue)

# Check everything sums to the inttial stock
lpSum([prob.variables()[i].varValue for i in range(0,len(lstore))])

# Add the poisson demand

# Create a new demand dictionary with the previous demand
demand_pois = {k: np.random.poisson(v) for k, v in demand.items()}

# Check the numbers make sense
demand_pois

# Specify the new problem
prob_pois = LpProblem("Replenishment Problem", LpMaximize)

# Demand for each store
prev_demand = {
	's1': 100,
	's2': 50,
	's3': 25,
	's4': 60,
	's5': 70,
	's6': 85,
	's7': 90,
	's8': 95,
	's9': 22,
	's10': 30
}

demand_pois = {k: np.random.poisson(v) for k, v in prev_demand.items()}
# Per unit transportation cost for each store


store_variables_pois = LpVariable.dicts("StrP", lstore, 0, cat = 'Integer')

# Optimization function
prob_pois += lpSum([store_variables_pois[i]*margin[i] -
					store_variables_pois[i]*transport[i] for i in lstore])
					, "Total Revenue"

# Restrictions

# Add restriction for total available stock
prob_pois += lpSum([store_variables_pois[i] for i in lstore]) == initial_stock
 					,"StockAvailable"

# Add restrictions to ensure we never exceed demand in a store
for i in lstore:
	prob_pois += store_variables_pois[i] <= demand_pois[i]


# The problem is solved using PuLP's choice of Solver
prob_pois.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob_pois.status])

# The optimised objective function value is printed to the screen
print("Total Benefit of Replenishment = ", value(prob_pois.objective))

for v in prob_pois.variables():
    print(v.name, "=", v.varValue)
