# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 12:31:47 2022

@author: LJMCA
"""

from scipy.stats import chi2_contingency

# defining the table
data = [[6,2,13], [49,26,14],[170,134,112], [132,159,128],[12,19,24]]
stat, p, dof, expected = chi2_contingency(data)
#print(expected)
print("Chi-Square Value is :",stat)
# interpret p-value
alpha = 0.01
print("p value is " + str(p))
if p <= alpha:
	print('Dependent (reject H0)')
else:
	print('Independent (H0 holds true)')
