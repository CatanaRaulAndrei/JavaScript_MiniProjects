#!/usr/bin/python3

# Multiples of 5 and 3 

def mul(number1,number2):
    sum3=0
    sum5=0
    sum15=0
    for i in range(1,334):
            sum3+=i*number1
            
    for i in range(1,200):
            sum5+=i*number2 
            
    for i in range(1,67):
            sum15+=i*number2*3         
    
    return sum3+sum5-sum15

print(mul(3,5))
