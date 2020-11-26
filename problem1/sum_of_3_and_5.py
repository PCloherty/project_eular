#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
#Find the sum of all the multiples of 3 or 5 below 1000.

def main():
    current = 1
    maxNumber = 1000
    multiples =[]
    
    
    while current < maxNumber:
        if ((current % 3 ==0) | (current % 5 ==0)):
            multiples.append(current)
            current = current+1
        else:
            current = current+1
    
        

        
    print(sum(multiples))





main()