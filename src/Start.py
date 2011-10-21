'''
Created on Sep 24, 2011

@author: sambit
'''

from EulerProblem.EulerProblemTo10 import *

if __name__ == '__main__':
    problem = input("Which Project Euler Problem you want to run? ")
    solver = "problem" + str(problem)
    args = []
    
    if (problem <= 10):
        EulerProblemTo10(solver, args)