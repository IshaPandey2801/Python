"""

In a company an employee is paid as under:

If his basic salary is less thab Rs. 1500, then HRA = 10% of basic salary and DA =90% 
of basic salary.If his salary is either equal to or above Rs. 1500, then HRA = Rs. 500
DA = 98% of basic salary. If the employee's salary is input through the keyboard write a 
program to find hiss gross.  

"""

basic_salary= float(input("Enter basic salary : "))

if basic_salary<1500:
    hra = 0.10*basic_salary
    da = 0.90*basic_salary
else:
    hra=500
    da=0.98*basic_salary

#Calculate gross salary
gross_salary = basic_salary+hra+da

print("Gross Salary", gross_salary)