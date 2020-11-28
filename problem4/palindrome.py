# A palindromic number reads the same both ways. The largest palindrome made from the product
# of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
def main():
    #definitions
    x = 100
    y= 100
    normal=0
    reverse=0
    highest={'x_value':0,'y_value':0,'palindrome':0}

    print('Currently working please wait...')
    #outer loop  
    while x <= 1001:
        #innerloop
        while y <= 1001:
            #if the y loop reaches 1000, reset inner loop and increment once on outerloop
            if (y==1000):
                y=100
                x=x+1
            #if the x loop reaches 1000, break inner loop
            elif (x==1000):
                break
            
            #get number
            normal = x*y
            
            #turn the number into list of stings, reverse the list and join to get reverse number
            reverse=[str(i) for i in str(normal)]          
            y=y+1
            reverse.reverse()
            reverse="".join(reverse)
            #compare normal and reverse, if they are the same 
            if(int(normal) == int(reverse)):
                highest['x_value']=x
                highest['y_value']=y
                highest['palindrome']=int(normal)
        #break outerloop
        break
    print(f'Highest palindrome from two 3-digit numbers is {highest["palindrome"]} from {highest["x_value"]}*{highest["y_value"]}' )
    


main()