# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 12:31:47 2022

@author: LJMCA
"""
from scipy.stats import chi2_contingency
# defining the table
data = [[10,0,0], [82,9,23],[271,40,109], [214,54,120],[22,15,31]]
stat, p, dof, expected = chi2_contingency(data)
#print(expected)
print(stat)
# interpret p-value
alpha = 0.01
print("p value is " + str(p))
if p <= alpha:
	print('Dependent (reject H0)')
else:
	print('Independent (H0 holds true)')
