'''
Calculating the sales price

Problem definition:
    - make a program that calculates the sales price.
    - the store sales the product with the particular amount of percent off price
Input: 
    - original price
    - discount rate(percentage)
Output:
    - original price
    - discount amount
    - final price
    
Steps:
1. input an integer value for the original price(dollar). Save it as a variable "original_price"
(use the same variable names to pass the test program)
2. input an integer value for the discount rate(percentage). Save it as a variable "rate"
3. calculate the discount amount(dollar). Save it as a variable "discount_amount"
4. calculate the final price. Save it as a variable "final_price"
5. print original price
6. print discount amount
7. print the final sale price 

EXAMPLE
input:      200
            20

output:     Original price: $200
            Discount amount: $40
            The final price: $160
'''
#input an integer value for the original price(dollar). Save it as a variable "original_price"
original_price = int(input('Original price: '))

#input an integer value for the discount rate(percentage). Save it as a variable "rate"
rate = int(input('Discount amount: '))

#calculate the discount amount(dollar). Save it as a variable "discount_amount"
discount_amount = original_price * rate / 100

#calculate the final price. Save it as a variable "final_price"
final_price = original_price - discount_amount


print('Original price: $' + str(original_price))
print('Discount amount: $' + str(float(discount_amount)))
print('The final price is: $' + str(float(final_price)))



