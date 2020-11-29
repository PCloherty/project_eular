#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def main():
    #define variables
    counter=1
    #(below is a test version in order to watch the 20 concurrent evenly divisable numbers happen, in order to watch
    #remove the hash from the 2 print lines in the if statement and put a hash in front of the above counter)
    #counter=232792555
    concurrent=1
    number=1
    #outerloop
    while concurrent <20:
        #inner loop
        while number <=20:
            #find out if there is a remainder
            modulus=counter % number
            #if there isnt a remainder increment concurrent and number variables
            if(modulus==0):
                #print(f'counter={counter}, number={number}, modulus={modulus}, concurrent={concurrent}')
                concurrent=concurrent+1 
                number=number+1
                #if concurrent reaches 20 break the inner loop
                if (concurrent==20):
                    break
            #else reset concurrent and number to 1 as well as incrementing counter ready for the next loop
            else:
                #print(f'counter={counter}, number={number}, modulus={modulus}, broke concurrent streak')
                concurrent=1
                number=1
                counter=counter+1 
        break
    print(f'counter={counter}, number={number}, modulus={modulus}, concurrent={concurrent}')
    

main()