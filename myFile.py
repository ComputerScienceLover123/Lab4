# Dillon Anabi Code Day 1
'''Thursday, 12/17/20 Start time: 9:04 PM Finish time: 10:35 PM Total Time: 1:31 For my first day work day, I mainly prioritized the Project Euler math problems. It took me about 40 minutes to solve the first problem. I was extremely confused with the methods and how to solve it. What helped me a lot is looking online and in the Project Euler site to see some of the starting steps of other people. After I completed the problem, I began looking at the code associated with the math problem. Some of the code contained in the solution involved setting an initial variable to 0 and a target variable to 999. They also used the remainder operation to find all possible multiples of 3 and 5.'''
#Problem 1 Project Euler Code 
target=999
sum=0
for i=1 to target do
if (i mod 3=0) or (i mod 5)=0 then sum:=sum+i
output sum
