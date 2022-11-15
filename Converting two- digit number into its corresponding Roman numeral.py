#Python program to convert number to roman numerals

n = int(input())
#Taking a 2 digit number from the user 

ten_digit = n // 10
#Taking the 10s digit number out
unit_digit = n % 10
#Taking the unit digit number out

#We will be handling each digit seperately 

if ten_digit <= 3 :
    
    for i in range(0,ten_digit):
        
        print('X',end="")

elif ten_digit == 4 :
    
    print('XL',end="")

elif ten_digit == 5 :
    
    print('L',end="")
    
elif ten_digit >= 6 and ten_digit <= 8 :
    
    print('L',end="")
    
    for i in range(5,ten_digit):
        
        print('X',end="")

elif ten_digit == 9 :
    
    print('XC',end="")
    


if unit_digit <= 3 :
    
    for i in range(0,unit_digit):
        
        print('I',end="")

elif unit_digit == 4 :
    
    print('IV',end="")

elif unit_digit == 5 :
    
    print('V',end="")
    
elif unit_digit >= 6 and unit_digit <= 8 :
    
    print('V',end="")
    
    for i in range(5,unit_digit):
        
        print('I',end="")

elif unit_digit == 9 :
    
    print('IX',end="")
