'''
STRING
Here is the original string.
    - original_str = 'Python Programming'
1. extract 'Python' from original string with index slicing
    - sub1 = original_str[index_slicing] #extract the first substring 'Python'
2. extract 'Programming' from original string with index slicing
    - sub2 = original_str[index_slicing] #extract the second substring 'Programming'
3. using the string concatenation ('+')
    - merge two substrings sub1 and sub2 and save it to variable "merged_str"
    - merge_str = sub2 + sub1
    'Programming Python'

EXAMPLE
input: none

output: Programming
        Python
        Programming Python 
'''

#assign variables
original_str = 'Python Programming'

#extract 'Python' from original string with index slicing
sub1 = original_str[:6]
print(sub1)

#extract 'Programming' from original string with index slicing
sub2 = original_str[7:18]
print(sub2)

#merge two substrings and save it to variable "merged_str"
merged_str = sub2 + ' ' + sub1

print(merged_str)
