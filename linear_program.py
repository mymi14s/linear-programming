"""
Title: Linear Programming Problem Solver
Author: Anthony Chiemeka Emmanuel
Date: 16-10-2016
Email: mymi14s@gmail.com
Version: 1.0
"""

from __future__ import print_function
import sys
from ortools.linear_solver import linear_solver_pb2
from ortools.linear_solver import pywraplp


def RunLinearExampleNaturalLanguageAPI(optimization_problem_type):
  """Example of simple linear program with natural language API."""
  solver = pywraplp.Solver('RunLinearExampleNaturalLanguageAPI',
                           optimization_problem_type)
  infinity = solver.infinity()
  # x1, x2 and x3 are continuous non-negative variables.
  x1 = solver.NumVar(0.0, infinity, 'x1')
  x2 = solver.NumVar(0.0, infinity, 'x2')
  x3 = solver.NumVar(0.0, infinity, 'x3')

  solver.Maximize(10 * x1 + 6 * x2 + 4 * x3)
  c0 = solver.Add(10 * x1 + 4 * x2 + 5 * x3 <= 600, 'ConstraintName0')
  c1 = solver.Add(2 * x1 + 2 * x2 + 6 * x3 <= 300)
  sum_of_vars = sum([x1, x2, x3])
  c2 = solver.Add(sum_of_vars <= 100.0, 'OtherConstraintName')

  MSolveAndPrint(solver, [x1, x2, x3], [c0, c1, c2])
  # Print a linear expression's solution value.
  print(('Sum of vars: %s = %s' % (sum_of_vars, sum_of_vars.solution_value())))


def MRunLinearExampleCppStyleAPI(optimization_problem_type):
  """Example of simple linear program with the C++ style API."""
  solver = pywraplp.Solver('RunLinearExampleCppStyle', optimization_problem_type)
  
  infinity = solver.infinity()
  solver_lists = ['x1','x2','x3','x4','x5','x6','x7','x8','x9','x10','x11','x12','x13','x14','x15','x16',\
	'x17','x18','x19','x20','x21','x22','x23','x24','x25','x26','x27','x28','x29','x30','x31','x32','x33',\
	'x34','x35','x36','x37','x38','x39','x40','x41','x42','x43','x44','x45','x46','x47','x48','x49','x50',\
	'x51','x52','x53','x54','x55','x56','x57','x58','x59','x60','x61','x62','x63','x64','x65','x66','x67']
	

  c0=0; x0=0
  c1=0; x1=0
  c2=0; x2=0
  c3=0; x3=0
  c4=0; x4=0
  c5=0; x5=0
  c6=0; x6=0
  c7=0; x7=0
  c8=0; x8=0
  c9=0; x9=0
  c10=0; x10=0
  c11=0; x11=0
  c12=0; x12=0
  c13=0; x13=0
  c14=0; x14=0
  c15=0; x15=0
  c16=0; x16=0
  c17=0; x17=0
  c18=0; x18=0
  c19=0; x19=0
  c20=0; x20=0
  c21=0; x21=0
  c22=0; x22=0
  c23=0; x23=0
  c24=0; x24=0
  c25=0; x25=0
  c26=0; x26=0
  c27=0; x27=0
  c28=0; x28=0
  c29=0; x29=0
  c30=0; x30=0
  c31=0; x31=0
  c32=0; x32=0
  c33=0; x33=0
  c34=0; x34=0
  c35=0; x35=0
  c36=0; x36=0
  c37=0; x37=0
  c38=0; x38=0
  c39=0; x39=0
  c40=0; x40=0
  c41=0; x41=0
  c42=0; x42=0
  c43=0; x43=0
  c44=0; x44=0
  c45=0; x45=0
  c46=0; x46=0
  c47=0; x47=0
  c48=0; x48=0
  c49=0; x49=0
  c50=0; x50=0
  c51=0; x51=0
  c52=0; x52=0
  c53=0; x53=0
  c54=0; x54=0
  c55=0; x55=0
  c56=0; x56=0
  c57=0; x57=0
  c58=0; x58=0
  c59=0; x59=0
  c60=0; x60=0
  c61=0; x61=0
  c62=0; x62=0
  c63=0; x63=0
  c64=0; x64=0
  c65=0; x65=0
  c66=0; x66=0
  c67=0; x67=0
  c68=0; x68=0
  c69=0; x69=0
  c70=0; x70=0
  c71=0; x71=0
  c72=0; x72=0
  c73=0; x73=0
  c74=0; x74=0
  c75=0; x75=0
  c76=0; x76=0
  c77=0; x77=0
  c78=0; x78=0
  c79=0; x79=0
  c80=0; x80=0
  c81=0; x81=0
  c82=0; x82=0
  c83=0; x83=0
  c84=0; x84=0
  c85=0; x85=0
  c86=0; x86=0
  c87=0; x87=0
  c88=0; x88=0
  c89=0; x89=0
  c90=0; x90=0
  c91=0; x91=0
  c92=0; x92=0
  c93=0; x93=0
  c94=0; x94=0
  c95=0; x95=0
  c96=0; x96=0
  c97=0; x97=0
  c98=0; x98=0
  c99=0; x99=0
  xlist= [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22\
    ,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34,x35,x36,x37,x38,x39,x40,x41,x42,x43\
    ,x44,x45,x46,x47,x48,x49,x50,x51,x52,x53,x54,x55,x56,x57,x58,x59,x60,x61,x62,x63,x64\
    ,x65,x66,x67,x68,x69,x70,x71,x72,x73,x74,x75,x76,x77,x78,x79,x80,x81,x82,x83,x84,x85\
    ,x86,x87,x88,x89,x90,x91,x92,x93,x94,x95,x96,x97,x98,x99]
  clist = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24\
	,c25,c26,c27,c28,c29,c30,c31,c32,c33,c34,c35,c36,c37,c38,c39,c40,c41,c42,c43,c44,c45,c46,c47\
	,c48,c49,c50,c51,c52,c53,c54,c55,c56,c57,c58,c59,c60,c61,c62,c63,c64,c65,c66,c67,c68,c69,c70\
	,c71,c72,c73,c74,c75,c76,c77,c78,c79,c80,c81,c82,c83,c84,c85,c86,c87,c88,c89,c90,c91,c92,c93\
	,c94,c95,c96,c97,c98,c99]

  print("Maximization Case:")
  number_of_variables = int(input("Enter number of variable: "))
  number_of_constraints = int(input("Enter number of constraint: "))
  
  xnlist = []
  xclist = []  
  for number_of_variable in range(number_of_variables):
	  xlist[number_of_variable] = solver.NumVar(0.0, infinity, solver_lists[number_of_variable])
	  xnlist.append( xlist[number_of_variable])   
  # x1, x2 and x3 are continuous non-negative variables.
  
  # Minimize x1 + 2 * x2.
  objective = solver.Objective()
  print("Enter Objective function: ")
  for x in range(number_of_variables):
	  print("x"+str(x+1));n = float(input())
	  objective.SetCoefficient( xnlist[x], n)
  objective.SetMaximization()

  # 2 * x2 + 3 * x1 >= 17.
  for x in range(number_of_constraints):
	  print("Constraint "+ str(x+1) +":")
	  n = float(input("bi: "));xlist[x] = solver.Constraint(-infinity, n, str(xlist[x]))
          xclist.append(xlist[x])
	  for y in range(number_of_variables):
		  print("x"+str(y+1))
		  n = float(input())
		  xlist[x].SetCoefficient(xnlist[y], n)
 


  MSolveAndPrint(solver, xnlist, xclist)


def MSolveAndPrint(solver, variable_list, constraint_list):
  """Solve the problem and print the solution."""
  print(('Number of variables = %d' % solver.NumVariables()))
  print(('Number of constraints = %d' % solver.NumConstraints()))

  result_status = solver.Solve()

  # The problem has an optimal solution.
  assert result_status == pywraplp.Solver.OPTIMAL

  # The solution looks legit (when using solvers others than
  # GLOP_LINEAR_PROGRAMMING, verifying the solution is highly recommended!).
  assert solver.VerifySolution(1e-7, True)

  #print(('Problem solved in %f milliseconds' % solver.wall_time()))

  # The objective value of the solution.
  print(('Optimal objective value = %f' % solver.Objective().Value()))

  # The value of each variable in the solution.
  for variable in variable_list:
    print(('%s = %f' % (variable.name(), variable.solution_value())))

  """print('Advanced usage:')
  print(('Problem solved in %d iterations' % solver.iterations()))
  for variable in variable_list:
    print(('%s: reduced cost = %f' % (variable.name(), variable.reduced_cost())))
  activities = solver.ComputeConstraintActivities()
  for i, constraint in enumerate(constraint_list):
    print(('constraint %d: dual value = %f\n'
          '               activity = %f' %
          (i, constraint.dual_value(), activities[constraint.index()])))
  """

def RunIntegerExampleCppStyleAPI(optimization_problem_type):
  """Example of simple integer program with the C++ style API."""
  solver = pywraplp.Solver('RunIntegerExampleCppStyleAPI',
                           optimization_problem_type)
  infinity = solver.infinity()
  
  solver_lists = ['x1','x2','x3','x4','x5','x6','x7','x8','x9','x10','x11','x12','x13','x14','x15','x16',\
	'x17','x18','x19','x20','x21','x22','x23','x24','x25','x26','x27','x28','x29','x30','x31','x32','x33',\
	'x34','x35','x36','x37','x38','x39','x40','x41','x42','x43','x44','x45','x46','x47','x48','x49','x50',\
	'x51','x52','x53','x54','x55','x56','x57','x58','x59','x60','x61','x62','x63','x64','x65','x66','x67']
	
  
  c0=0; x0=0
  c1=0; x1=0
  c2=0; x2=0
  c3=0; x3=0
  c4=0; x4=0
  c5=0; x5=0
  c6=0; x6=0
  c7=0; x7=0
  c8=0; x8=0
  c9=0; x9=0
  c10=0; x10=0
  c11=0; x11=0
  c12=0; x12=0
  c13=0; x13=0
  c14=0; x14=0
  c15=0; x15=0
  c16=0; x16=0
  c17=0; x17=0
  c18=0; x18=0
  c19=0; x19=0
  c20=0; x20=0
  c21=0; x21=0
  c22=0; x22=0
  c23=0; x23=0
  c24=0; x24=0
  c25=0; x25=0
  c26=0; x26=0
  c27=0; x27=0
  c28=0; x28=0
  c29=0; x29=0
  c30=0; x30=0
  c31=0; x31=0
  c32=0; x32=0
  c33=0; x33=0
  c34=0; x34=0
  c35=0; x35=0
  c36=0; x36=0
  c37=0; x37=0
  c38=0; x38=0
  c39=0; x39=0
  c40=0; x40=0
  c41=0; x41=0
  c42=0; x42=0
  c43=0; x43=0
  c44=0; x44=0
  c45=0; x45=0
  c46=0; x46=0
  c47=0; x47=0
  c48=0; x48=0
  c49=0; x49=0
  c50=0; x50=0
  c51=0; x51=0
  c52=0; x52=0
  c53=0; x53=0
  c54=0; x54=0
  c55=0; x55=0
  c56=0; x56=0
  c57=0; x57=0
  c58=0; x58=0
  c59=0; x59=0
  c60=0; x60=0
  c61=0; x61=0
  c62=0; x62=0
  c63=0; x63=0
  c64=0; x64=0
  c65=0; x65=0
  c66=0; x66=0
  c67=0; x67=0
  c68=0; x68=0
  c69=0; x69=0
  c70=0; x70=0
  c71=0; x71=0
  c72=0; x72=0
  c73=0; x73=0
  c74=0; x74=0
  c75=0; x75=0
  c76=0; x76=0
  c77=0; x77=0
  c78=0; x78=0
  c79=0; x79=0
  c80=0; x80=0
  c81=0; x81=0
  c82=0; x82=0
  c83=0; x83=0
  c84=0; x84=0
  c85=0; x85=0
  c86=0; x86=0
  c87=0; x87=0
  c88=0; x88=0
  c89=0; x89=0
  c90=0; x90=0
  c91=0; x91=0
  c92=0; x92=0
  c93=0; x93=0
  c94=0; x94=0
  c95=0; x95=0
  c96=0; x96=0
  c97=0; x97=0
  c98=0; x98=0
  c99=0; x99=0
  xlist= [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22\
    ,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34,x35,x36,x37,x38,x39,x40,x41,x42,x43\
    ,x44,x45,x46,x47,x48,x49,x50,x51,x52,x53,x54,x55,x56,x57,x58,x59,x60,x61,x62,x63,x64\
    ,x65,x66,x67,x68,x69,x70,x71,x72,x73,x74,x75,x76,x77,x78,x79,x80,x81,x82,x83,x84,x85\
    ,x86,x87,x88,x89,x90,x91,x92,x93,x94,x95,x96,x97,x98,x99]
  clist = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24\
	,c25,c26,c27,c28,c29,c30,c31,c32,c33,c34,c35,c36,c37,c38,c39,c40,c41,c42,c43,c44,c45,c46,c47\
	,c48,c49,c50,c51,c52,c53,c54,c55,c56,c57,c58,c59,c60,c61,c62,c63,c64,c65,c66,c67,c68,c69,c70\
	,c71,c72,c73,c74,c75,c76,c77,c78,c79,c80,c81,c82,c83,c84,c85,c86,c87,c88,c89,c90,c91,c92,c93\
	,c94,c95,c96,c97,c98,c99]
	
	
  # x1 and x2 are integer non-negative variables.
  print("\nMinimization case:\n")
  number_of_variables = int(input("Enter number of variable: "))
  number_of_constraints = int(input("Enter number of constraint: "))
  
  xnlist = []  
  for number_of_variable in range(number_of_variables):
	  xlist[number_of_variable] = solver.IntVar(0.0, infinity, solver_lists[number_of_variable])
	  xnlist.append( xlist[number_of_variable])
  #x2 = solver.IntVar(0.0, infinity, 'x2')

  # Minimize x1 + 2 * x2.
  objective = solver.Objective()
  print("Enter Objective function: ")
  for x in range(number_of_variables):
	  print("x"+str(x+1));n = float(input())
	  objective.SetCoefficient( xnlist[x], n)
  #objective.Minimization()
  
  
  
  # 2 * x2 + 3 * x1 >= 17.
  for x in range(number_of_constraints):
	  print("Constraint "+ str(x+1) +":")
	  n = float(input("bi: "));ct = solver.Constraint(n,infinity)
	  for y in range(number_of_variables):
		  print("x"+str(y+1))
		  n = float(input())
		  ct.SetCoefficient(xnlist[y], n)
 

  SolveAndPrint(solver, xnlist)


def SolveAndPrint(solver, variable_list):
  """Solve the problem and print the solution."""
  print(('Number of variables = %d' % solver.NumVariables()))
  print(('Number of constraints = %d' % solver.NumConstraints()))

  result_status = solver.Solve()

  # The problem has an optimal solution.
  assert result_status == pywraplp.Solver.OPTIMAL

  # The solution looks legit (when using solvers others than
  # GLOP_LINEAR_PROGRAMMING, verifying the solution is highly recommended!).
  assert solver.VerifySolution(1e-7, True)

  #print(('Problem solved in %f milliseconds' % solver.wall_time()))

  # The objective value of the solution.
  print(('Optimal objective value = %f' % solver.Objective().Value()))

  # The value of each variable in the solution.
  for variable in variable_list:
    print(('%s = %f' % (variable.name(), variable.solution_value())))

  #print('Advanced usage:')
  #print(('Problem solved in %d branch-and-bound nodes' % solver.nodes()))


def Announce(solver, api_type):
  #print(('---- Integer programming example with ' + solver + ' (' +
   #      api_type + ') -----'))


	def RunAllIntegerExampleNaturalLanguageAPI():
	  if hasattr(pywraplp.Solver, 'GLPK_MIXED_INTEGER_PROGRAMMING'):
		Announce('GLPK', 'natural language API')
		RunIntegerExampleNaturalLanguageAPI(
			pywraplp.Solver.GLPK_MIXED_INTEGER_PROGRAMMING)
	  if hasattr(pywraplp.Solver, 'CBC_MIXED_INTEGER_PROGRAMMING'):
		Announce('CBC', 'natural language API')
		RunIntegerExampleNaturalLanguageAPI(
			pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
	  if hasattr(pywraplp.Solver, 'SCIP_MIXED_INTEGER_PROGRAMMING'):
		Announce('SCIP', 'natural language API')
		RunIntegerExampleNaturalLanguageAPI(
			pywraplp.Solver.SCIP_MIXED_INTEGER_PROGRAMMING)


def RunAllIntegerExampleCppStyleAPI():
	  if hasattr(pywraplp.Solver, 'GLPK_MIXED_INTEGER_PROGRAMMING'):
		Announce('GLPK', 'C++ style API')
		RunIntegerExampleCppStyleAPI(pywraplp.Solver.GLPK_MIXED_INTEGER_PROGRAMMING)
	  if hasattr(pywraplp.Solver, 'CBC_MIXED_INTEGER_PROGRAMMING'):
		Announce('CBC', 'C++ style API')
		RunIntegerExampleCppStyleAPI(pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
	  if hasattr(pywraplp.Solver, 'SCIP_MIXED_INTEGER_PROGRAMMING'):
		Announce('SCIP', 'C++ style API')
		RunIntegerExampleCppStyleAPI(
			pywraplp.Solver.SCIP_MIXED_INTEGER_PROGRAMMING)


#def main():
  #RunAllIntegerExampleNaturalLanguageAPI()
  #RunAllIntegerExampleCppStyleAPI()


#if __name__ == '__main__':
 # main()
def main():
  print("Title: Linear Programming Problem Solver\nAuthor: Anthony Chiemeka Emmanuel\nDate: 16-10-2016\nEmail: mymi14s@gmail.com\nVersion: 1.0")
  print("Instruction: m for Minimization, M for Maximization\n");minMax = raw_input("Enter m or M: ")
  while True:
	  if minMax == 'M':
		  all_names_and_problem_types = (
			  list(linear_solver_pb2.MPModelRequest.SolverType.items()))
		  for name, problem_type in all_names_and_problem_types:
			# Skip non-LP problem types.
			if not name.endswith('LINEAR_PROGRAMMING'):
			  continue
			# Skip problem types that aren't supported by the current binary.
			if not pywraplp.Solver.SupportsProblemType(problem_type):
			  continue
			#print(('\n------ Linear programming example with %s ------' % name))
			#print('\n*** Natural language API ***')
			#RunLinearExampleNaturalLanguageAPI(problem_type)
			#print('\n*** C++ style API ***')
			MRunLinearExampleCppStyleAPI(problem_type);print("Instruction: m for Minimization, M for Maximization\n");minMax = raw_input("Enter m or M: ")
	  elif minMax == 'm':
		  RunAllIntegerExampleCppStyleAPI();print("Instruction: m for Minimization, M for Maximization\n");minMax = raw_input("Enter m or M: ")
	  
	  else:
		  print("Wrong input")
		  print("Instruction: m for Minimization, M for Maximization\n")
		  minMax = raw_input("Enter m or M: ")

if __name__ == '__main__':
  main()
