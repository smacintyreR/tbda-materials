# Import PuLP modeler functions
from pulp import *

"""
5 3 x x 7 x x x x
6 x x 1 9 5 x x x
x 9 8 x x x x 6 x
8 x x x 6 x x x 3
4 x x 8 x 3 x x 1
7 x x x 2 x x x 6
x 6 x x x x 2 8 x
x x x 4 1 9 x x 5
x x x x 8 x x 7 9
"""

# Create the 'prob' variable to contain the problem data
prob = LpProblem("Sudoku",LpMinimize)

# Variables
# xijk = value of row i column j is k
x = {}
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            x[(i,j,k)] = LpVariable(
    "Value of row {} column {} is {}".format(i,j,k),
    0, 1, LpInteger)

# Optimization function
prob += 0

# Restrictions
# Rows
for i in range(1,10):
    for k in range(1,10):
        prob += lpSum([x[(i,j,k)] for j in range(1,10)]) == 1

# Columns
for j in range(1,10):
    for k in range(1,10):
        prob += lpSum([x[(i,j,k)] for i in range(1,10)]) == 1

# Squares
for s in [1,4,7]:
    for t in [1,4,7]:
        for k in range(1,10):
            prob += lpSum([x[(i,j,k)] for i in range(s,s+3) for j in range(t,t+3)]) == 1

# One value per cell
for i in range(1,10):
    for j in range(1,10):
        prob += lpSum([x[(i,j,k)] for k in range(1,10)]) == 1

# Fixed values
prob += x[(1,1,5)] == 1
prob += x[(1,2,3)] == 1
prob += x[(1,5,7)] == 1
prob += x[(2,1,6)] == 1
prob += x[(2,4,1)] == 1
prob += x[(2,5,9)] == 1
prob += x[(2,6,5)] == 1
prob += x[(3,2,9)] == 1
prob += x[(3,3,8)] == 1
prob += x[(3,8,6)] == 1
prob += x[(4,1,8)] == 1
prob += x[(4,5,6)] == 1
prob += x[(4,9,3)] == 1
prob += x[(5,1,4)] == 1
prob += x[(5,4,8)] == 1
prob += x[(5,6,3)] == 1
prob += x[(5,9,1)] == 1
prob += x[(6,1,7)] == 1
prob += x[(6,5,2)] == 1
prob += x[(6,9,6)] == 1
prob += x[(7,2,6)] == 1
prob += x[(7,7,2)] == 1
prob += x[(7,8,8)] == 1
prob += x[(8,4,4)] == 1
prob += x[(8,5,1)] == 1
prob += x[(8,6,9)] == 1
prob += x[(9,5,8)] == 1
prob += x[(9,8,7)] == 1
prob += x[(9,9,9)] == 1

#print(prob)

# The problem is solved using PuLP's choice of Solver
prob.solve()

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    if v.varValue != 0:
        print(v.name, "=", v.varValue)

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# The optimised objective function value is printed to the screen
print("Total Cost of Sudoku = ", value(prob.objective))

# Print sudoku solution
c = {}
for v in prob.variables():
    if v.varValue is not None and int(v.varValue) == 1:
        #print(v.name)
        #print(v.name[13],v.name[22],v.name[27])
        i,j,k = int(v.name[13]), int(v.name[22]), int(v.name[27])
        c[(i,j)] = k
for i in range(1,10):
    for j in range(1,10):
        print("{} ".format(c[(i,j)]), end='')
    print("")
