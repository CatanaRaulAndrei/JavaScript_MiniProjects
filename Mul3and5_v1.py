# !/usr/bin/python3

# multiples of 5 and 3
def nsum(n):
    return n*(n+1)//2   

def mul(number):
    five_to= (number-1)//5
    three_to= (number-1)//3
    fiveteen_to=(number-1)//15
    
    five_sum= nsum(five_to)*5
    three_sum= nsum(three_to)*3
    fiveteen_sum= nsum(fiveteen_to)*15
    
    return five_sum + three_sum - fiveteen_sum
    
print(mul(1000))    
