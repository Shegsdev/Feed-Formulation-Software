'''
	Objective function: Maximize 10x1 + 6x2 + 4x3
		Subject to   x1 + x2 + x3 <= 100
			     10x1 + 4x2 + 5x3 <= 600
			     2x1 + 2x2 + 6x3 <= 300
			     x1 >= 0, x2 >= 0, x3 >= 0

'''

from optlang import Model, Variable, Constraint, Objective

# All the (symbolic) variables are declared, with a name and optionally a lower and/or upper bound.

x1 = Variable('x1', lb=0)
x2 = Variable('x2', lb=0)
x3 = Variable('x3', lb=0)

# A constraint is constructed from an expression of variables and a lower and/or upper bound (lb and ub).

c1 = Constraint(x1 + x2 + x3, ub=100)
c2 = Constraint(10 * x1 + 4 * x2 + 5 * x3, ub=600)
c3 = Constraint(2 * x1 + 2 * x2 + 6 * x3, ub=300)

# An objective can be formulated
obj = Objective(10 * x1 + 6 * x2 + 4 * x3, direction='max')

# Variables, constraints and objectives are combined in a Model object, which can subsequently be optimized.
model = Model(name='Simple model')
model.objective = obj
model.add([c1, c2, c3])
status = model.optimize()

print("status:", model.status)
print("objective value:", model.objective.value)
print("-------------")
for var_name,  var in model.variables.items():
    print(var_name, "=", var.primal)


# Installation
# | Install optlang using pip:

# pip install optlang
