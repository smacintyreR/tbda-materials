"""
Scheduling problem: resource allocation
=======================================
In a scheduling problem we have to fulfill a set of jobs on a number of resources under certain constraints such as restrictions on the job completion times, priorities between jobs (one job cannot start until another one is finished)...

In this case we need to produce some products. To produce a product we need to perform some jobs, from which resources are allocated.
The goal is to produce the products by minimizing the availability time, i.e., the time in which each product is finished.

More specifically,

Given:
- A list of products p1, p2, p3, ...
- A list of resources r1, r2, r3, ... (resources can be machines, people, ...)
- A max capacity of resources to process jobs at a time c1, c2, c3, ...
- A list of dependencies of a product (product roadmap). To be produced, each product to be produced needs to perform some jobs in order. 
Each job depends on a resource. 
It is not necessary to perform all jobs for a product continuously on time. It is possible to wait some time between jobs of a product.
	p1: 	r1	r2	r3 	   -> Produced! # To be produced, p1 must perform a job from which needs resource r1, then another job from which needs resource r2, and so on
	p2: 	r2	r3	r4	   -> Produced! # To be produced, p2 must perform a job from which needs resource r2, then another job from which needs resource r3, and so on
	p3:		r1	r5	r3	r2 -> Produced! # To be produced, p3 must perform a job from which needs resource r1, then another job from which needs resonrce r5, and so on

The goal is:
- Schedule the resource usage in order to finish the products by minimizing the availability time of the products.

Restrictions are:
- Not to overlap the maximum capacity of a resource at a time.
- Perform the tasks (resource allocation) in the order specified in the product roadmap.

Code snippet with data
- See ass_scheduling.py

Additional exercise
Consider now an additional restriction and reforumulate the problem:
- Maximum deadline time for the production of each product. Products must be produced at most at that time.
"""

# Import PuLP modeler functions
from pulp import *

# Create the 'prob' variable to contain the problem data
prob = LpProblem("Scheduling Problem",LpMinimize)

# List of products
lprod = ['p1','p2','p3','p4','p5','p6','p7','p8','p9']
# List of resources
lres = ['r1','r2','r3','r4','r5','r6','r7','r8','r9']
# Number of simultaneously jobs for a resource at a time
rescap = {
	'r1': 1,
	'r2': 1,
	'r3': 1,
	'r4': 1,
	'r5': 1,
	'r6': 1,
	'r7': 1,
	'r8': 1,
	'r9': 1,
}
# Product roadmaps
roadmap = {
	'p1': ['r1','r2','r3','r4','r5'],
	'p2': ['r1','r3','r5','r7','r9'],
	'p3': ['r1','r3','r4','r5','r8','r9'],
	'p4': ['r2','r3','r4','r5','r7','r8','r9'],
	'p5': ['r3','r2','r1','r4','r7','r9'],
	'p6': ['r3','r2','r1','r5','r8'],
	'p7': ['r4','r7','r9','r1','r2','r5'],
	'p8': ['r6','r5','r4','r3','r2','r1'],
	'p9': ['r1','r2','r3','r4','r5','r6','r7','r8','r9']
}
# For the additonal exercise
# Dealine production time for each product
prodmaxtime = {
	'p1': 10,
	'p2': 10,
	'p3': 10,
	'p4': 10,
	'p5': 15,
	'p6': 15,
	'p7': 15,
	'p8': 15,
	'p9': 15,
}

ntime = 30
nprod = len(lprod)
nres = len(lres)


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
print("Total Time of Scheduling = ", value(prob.objective))
