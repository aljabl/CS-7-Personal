'''
CALCULATING AN AVERAGE
Problem definition: Determine the average of a group of values:
    - input all three INTEGER values (user input) then divide the sum by the number of values
    - print the total and average(float) of the values
    
1. input the first integer value and assign it to the variable "val1"
2. input the second integer value and assign it to the variable "val2"
3. input the third integer value and assign it to the variable "val3"
4. get sum of all three values and assign it to the variable "total"
5. get average and save it as variable "average"
6. print three values in a line
7. print the total
8. print the average with two fractional digits (ex: 123.45)

EXAMPLE
input:      100
            90
            110

output:     Values: 100 90 110
            Total: 300
            Average: 100.00

print('Average: \t {0:.2f} '.format(avg))
or
print(f'Average: \t {avg:.2f}')
'''

#assign variables
val1 = input('First value: ')
val2 = input('Second value: ')
val3 = input('Third value: ')

#get sum of all three values and assign it to the variable "total"
total = (int(val1) + int(val2) + int(val3))

#get average and save it as variable "average"
average = int(total) / 3

#print three values in a line
print('Values: ', val1, val2, val3, sep=' ')

#print the total
print('Total: ', total)

#print the average with two fractional digits (ex: 123.45)
print(f'Average: {average:.2f}')