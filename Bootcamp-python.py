#!/usr/bin/env python3
# gentle intro to python
# written by Katherine Duncan 12/09/21
# based on tutorial developed by Mike Mack

#%% python as a calculator 
2+2
(103-3*5)/4
7/3
4+3
sqrt(48)

# need to add the math library to do some arithmetic!
import math
math.sqrt(9)

4**2
math.pow(4,2)


#%% beyond arithmetic 
25 > 5
25 < 5
5 < 15 < 25
4 >= 4
4 == 4

(4<5) and (6<10)
(4<3) or (6<10)
not (4<3) and not (6<5)

#%% try it yourself
'''
Use python to calculate:
83 multiplied by 76
5 to the power of 3
'''


'''
Use python to determine 
if 81 multiplied by 12 is greater than 2000
if 435 divided by 5 is less than 90
if at least one of the above inequalities is false
'''


#%% variables
a = 5
b = 4
a + b
c = a + b
c/3

a = 12
a + b

#%% data types
type(1)
type(1.8)
lion= 1.
type(lion)

type('zebra')
type("tiger")
type('lion')

'zebra'/x
#%% variables names
twox2 = 4
2xtwo = 4

a = 5
A = 2
a + A

return = 5
class = "nope"

#%% try it yourself
'''
Using snake case names, create one integer and two string variables

try using the "+" operator to combine the two string variables; what happens

try using the "+" operator to combine a string and a integer variable; what happens 
'''


#%% lists
a = [1,2,3]
b = ['y','e','p']
c = [1,'hi', a, b]
d = [3, 4., 'e', a

#%% indexing

x = 'PYTHON'
x[0]
x[4]
x[-1]

y = ['PYTHON', 2, 55, [4, 6]]
y[0]
y[3]

Lst = [50, 70, 30, 20, 90, 10, 50]
Lst[0:2]
Lst[0:4:2]
Lst[:3]
Lst[2:]
Lst[::-1]

#%% assigning elements

a = [587,443,862,901]
587 in a
999 in a
999 not in a
z = 'zebra'
'b' in z

data = [[456,875,549,490],[876,1092,763,889],[1119,568,688,13]]
[456,875,549,490] in data

fridge = ['apples','milk', 'bacon']
'apples' in fridge


#%% try it yourself
'''
use indexing to find the second value stored in list a

use slicing to get the first and last values stored in list a

replace the final element in list data with list a

*Advanced* use indexing to find the second value stored in the first element of list data 
'''
