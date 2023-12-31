import sympy as sym

#Defining variables
A, P, i, n = sym.symbols('A P i n')

#Defining equation
Eq3A = P*((i*(1+i)**n)/((1+i)**n-1))-A

#Substituting values
Eq3Asub = Eq3A.subs({A:25500,P:115000,n:6})

#Solving numerically for i
sol = sym.nsolve(Eq3Asub,5)

#Printing solution
print('i =',sol)