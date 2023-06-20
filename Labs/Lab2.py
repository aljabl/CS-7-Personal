'''
CALCULATING THE SALARY

Problem definition: write a program tht calculates and displays an employee's total wages for the week.
    - the regular hours for the work week are 40
    - any hours worked over 40 are considered overtime
    - the employee earns $18.25 per hour for regular hours and $27.78 per hour for overtime hours
    - ask for the employer's work hour and then save it as a variable "workhours"
        - we assume that this "workhours" is greater than 40
        - for example: the employee has worked 50 hours this week      
input:
    - one integer value for work hours
output (print in separate lines):
    - regular charge
    - overtime charge
    - total wages

1. assign the given values to the variables
    reg_hours = 40
    reg_rate = 18.25
    ov_rate = 27.78
2. calculate
    a. the overtime_hours
    b. the regular_wage
    c. the overtime_wage
3. calculate and print the total_wage

EXAMPLE
input: 50

Enter your work hours: 50
Regular Charge: 730.0
Overtime Charge: 277.80
Total wage: 1007.80
'''


#assigning values to variables
reg_hours = 40
reg_rate = 18.25
ov_rate = 27.78

workhours = input('Enter your work hours: ')

#calculate overtime_hours
overtime_hours = int(workhours) - 40

#calculate the regular_wage
regular_wage = reg_hours * reg_rate

#calculate the overtime_wage
overtime_wage = overtime_hours * ov_rate

#calculate the total_wage
total_wage = regular_wage + overtime_wage

print(f'Regular Charge: {float(regular_wage):.2f}')
print(f'Overtime Charge: {float(overtime_wage):.2f}')
print(f'Total wage: {float(total_wage):.2f}')
