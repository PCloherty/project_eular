# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def main():

    lowest_prime=2
    upper=600851475143
    prime_factors=[]

    
    while upper > 1 :
        if (upper % lowest_prime == 0):
            print(f'{upper}/{lowest_prime}={upper/lowest_prime}')
            prime_factors.append(lowest_prime)
            upper = upper/lowest_prime 
            if(upper == lowest_prime):
                break
        else:
            lowest_prime=lowest_prime+1
    print(f'The prime factors for 6000851475143 are:')
    for i in range(len(prime_factors)):
        print(f'{prime_factors[i]}')


main()